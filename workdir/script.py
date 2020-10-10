import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

import numpy as np

def get_cube_faces(cube_definition):
    
    # cube_definition é passado em coordenadas homogêneas, preciso remover isso para poder plotar no eixo 3D.
    cube_definition_adjusted = []
    for point in cube_definition:
        cube_definition_adjusted.append(point[:-1])
         
    # Agora o plot segue normal
    cube_definition_array = [
        np.array(list(item))
        for item in cube_definition_adjusted
    ]

    points = []
    points += cube_definition_array
    vectors = [
        cube_definition_array[1] - cube_definition_array[0],
        cube_definition_array[2] - cube_definition_array[0],
        cube_definition_array[3] - cube_definition_array[0]
    ]

    points += [cube_definition_array[0] + vectors[0] + vectors[1]]
    points += [cube_definition_array[0] + vectors[0] + vectors[2]]
    points += [cube_definition_array[0] + vectors[1] + vectors[2]]
    points += [cube_definition_array[0] + vectors[0] + vectors[1] + vectors[2]]

    points = np.array(points)

    edges = [
        [points[0], points[3], points[5], points[1]],
        [points[1], points[5], points[7], points[4]],
        [points[4], points[2], points[6], points[7]],
        [points[2], points[6], points[3], points[0]],
        [points[0], points[2], points[4], points[1]],
        [points[3], points[6], points[7], points[5]]
    ]

    faces = Poly3DCollection(edges, linewidths=1, edgecolors='k', facecolors=['b','r','g','y','m','k'])
    
    return faces

def plot_faces(faces,ax):
    
    ax.clear()
    ax.set_xlim3d([0.0, 15.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 15.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 15.0])
    ax.set_zlabel('Z')
    
    ax.add_collection3d(faces)
#     ax.set_aspect('auto')
    
    return 0
   
def translate(body,dx, dy, dz):
    translation_matrix = np.array([[1,0,0,dx], [0,1,0,dy],[0,0,1,dz],[0,0,0,1]])
    translated_body = translation_matrix.dot(body)
    return translated_body.transpose()


root = tkinter.Tk()
root.wm_title("Trab1")

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1,1,1, projection='3d')
cube_definition = np.array([[0,0,0,1],[0,2,0,1],[2,0,0,1],[0,0,2,1]])
faces = get_cube_faces(cube_definition)
plot_faces(faces,ax)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect("key_press_event", on_key_press)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)
tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
