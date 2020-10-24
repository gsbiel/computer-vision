from stl import mesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d  
from math import pi,cos,sin

def generate_vectors(x, y, z):
    zip_data = list(zip(x,y,z))
    data_array = np.array(zip_data)
    reshape = data_array.reshape(1572,3,3)
    return reshape

def set_axes_equal(ax):
    #Make axes of 3D plot have equal scale so that spheres appear as spheres,
    #cubes as cubes, etc..  This is one possible solution to Matplotlib's
    #ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    #Input
    #  ax: a matplotlib axis, e.g., as output from plt.gca().
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

    return


your_mesh = mesh.Mesh.from_file("./3DModel/myCharizard.stl")

# Get the x, y, z coordinates contained in the mesh structure that are the 
# vertices of the triangular faces of the object
x = your_mesh.x.flatten()
y = your_mesh.y.flatten()
z = your_mesh.z.flatten()

# print(x[:10])
# print(list(zip(x,y,z))[:20])
# for tuple in zip(x,y,z):
#     print(tuple)
generate_vectors(x,y,z)
# Get the vectors that define the triangular faces that form the 3D object
# obj_vectors = your_mesh.vectors
obj_vectors = generate_vectors(x,y,z)

print("Dimensão da malha")
print(obj_vectors.shape)
print(obj_vectors[:3])

# Create the 3D object from the x,y,z coordinates and add the additional array of ones to 
# represent the object using homogeneous coordinates
obj_3d = np.array([x.T,y.T,z.T,np.ones(x.size)])

###################################################
# Plotting the 3D vertices of the triangular faces
###################################################

# Create a new plot
# fig = plt.figure(figsize=[10,10])
# axes0 = plt.axes(projection='3d')

# Plot the points drawing the lines
# axes0.plot(obj_3d[0,:],obj_3d[1,:],obj_3d[2,:],'r')
# set_axes_equal(axes0)

###################################################
# Plotting the 3D triangular faces of the object
###################################################

# Create a new plot
fig = plt.figure(figsize=[10,10])
axes1 = plt.axes(projection='3d')

# Plot and render the faces of the object
axes1.add_collection3d(art3d.Poly3DCollection(obj_vectors))
# Plot the contours of the faces of the object
axes1.add_collection3d(art3d.Line3DCollection(obj_vectors, colors='k', linewidths=0.2, linestyles='-'))

# Set axes and their aspect
axes1.auto_scale_xyz(obj_3d[0,:],obj_3d[1,:],obj_3d[2,:])
set_axes_equal(axes1)
# Show the plots 
plt.show()