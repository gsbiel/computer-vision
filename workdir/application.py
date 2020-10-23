import tkinter
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np
from dice import Dice 
from camera import CameraAxis
from charizard import Charizard
import time
from mpl_toolkits.mplot3d import Axes3D

from slider import MySlider

OBJECTS = [
        ("Dice", "OBJECT"),
        ("Camera Axis", "CAMERA"),
    ]

ROTATIONS = [
    ("Rotate X","ROTATE_X"),
    ("Rotate Y","ROTATE_Y"),
    ("Rotate Z","ROTATE_Z"),
    ("No Rotation","NONE"),
]

AXIS_COLORS = [
    "b", # color for x-axis
    "g", # color for z-axis
    "r"  # color for y-axis
]

STYLING_PARAMETERS = {
    "container_pady":20,
}

x_current_orientation = 0
y_current_orientation = 0
z_current_orientation = 0

# CHARIZARD MOVEMENT EVENTS ##################################################################################################################

def charizardGoRight():
    remove_charizard_from_canvas()
    charizard.translateX(1)
    draw_charizard_on_canvas()
    update_canvas()
    return 

def charizardGoLeft():
    remove_charizard_from_canvas()
    charizard.translateX(-1)
    draw_charizard_on_canvas()
    update_canvas()
    return

def charizardGoOn():
    remove_charizard_from_canvas()
    charizard.translateY(1)
    draw_charizard_on_canvas()
    update_canvas()
    return

def charizardGoBack():
    remove_charizard_from_canvas()
    charizard.translateY(-1)  
    draw_charizard_on_canvas()
    update_canvas()
    return

def charizardGoUpLeft():
    remove_charizard_from_canvas()
    charizard.translateXY("01")
    draw_charizard_on_canvas()
    update_canvas()    
    return

def charizardGoUpRight():
    remove_charizard_from_canvas()
    charizard.translateXY("11")
    draw_charizard_on_canvas()
    update_canvas() 
    return

def charizardGoDownLeft():
    remove_charizard_from_canvas()
    charizard.translateXY("00")
    draw_charizard_on_canvas()
    update_canvas() 
    return

def charizardGoDownRight():
    remove_charizard_from_canvas()
    charizard.translateXY("10")
    draw_charizard_on_canvas()
    update_canvas() 
    return

def charizardGoUp():
    remove_charizard_from_canvas()
    charizard.translateZ(1)
    draw_charizard_on_canvas()
    update_canvas()
    return

def charizardGoDown():
    remove_charizard_from_canvas()
    charizard.translateZ(-1)
    draw_charizard_on_canvas()
    update_canvas()
    return

# DICE MOVEMENT EVENTS ##################################################################################################################

def diceRotateX(angle):
    remove_dice_from_canvas()
    dice.rotateX(angle)
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas()
    return

def diceRotateY(angle):
    remove_dice_from_canvas()
    dice.rotateY(angle)
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas()
    return

def diceRotateZ(angle):
    remove_dice_from_canvas()
    dice.rotateZ(angle)
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas()
    return

# CAMERA MOVEMENT EVENTS ##################################################################################################################

def cameraGoRight():
    remove_camera_from_canvas()
    camera.translateX(1)
    draw_camera_on_canvas()
    update_canvas()
    return

def cameraGoLeft():
    remove_camera_from_canvas()
    camera.translateX(-1)
    draw_camera_on_canvas()
    update_canvas()
    return

def cameraGoOn():
    remove_camera_from_canvas()
    camera.translateY(1)
    draw_camera_on_canvas()
    update_canvas()
    return

def cameraGoBack():
    remove_camera_from_canvas()
    camera.translateY(-1)
    draw_camera_on_canvas()
    update_canvas()
    return

def cameraGoUpLeft():
    remove_camera_from_canvas()
    camera.translateXY("01")
    draw_camera_on_canvas()
    update_canvas()
    return

def cameraGoUpRight():
    remove_camera_from_canvas()
    camera.translateXY("11")
    draw_camera_on_canvas()
    update_canvas()
    return

def cameraGoDownLeft():
    remove_camera_from_canvas()
    camera.translateXY("00")
    draw_camera_on_canvas()
    update_canvas()
    return

def cameraGoDownRight():
    remove_camera_from_canvas()
    camera.translateXY("10")
    draw_camera_on_canvas()
    update_canvas()
    return

def cameraGoUp():
    remove_camera_from_canvas()
    camera.translateZ(1)
    draw_camera_on_canvas()
    update_canvas()
    return

def cameraGoDown():
    remove_camera_from_canvas()
    camera.translateZ(-1)
    draw_camera_on_canvas()
    update_canvas()
    return

# CANVAS FUNCTIONS ##########################################################################################################################

def draw_camera_on_canvas():
    for index in range(camera.p_1.shape[0]):
        ax.quiver(
            camera.body[0][0], 
            camera.body[0][1], 
            camera.body[0][2], 
            camera.p_1[index][0], 
            camera.p_1[index][1], 
            camera.p_1[index][2], 
            length=2, 
            normalize=True, 
            color=AXIS_COLORS[index]
        )
    return

def remove_camera_from_canvas():
    ax.clear()
    set_axis_scale()
    draw_charizard_on_canvas()
    return

def draw_charizard_on_canvas():
    # Plot and render the faces of the object
    # ax.add_collection3d(Poly3DCollection(charizard.body))
    # Plot the contours of the faces of the object
    # ax.add_collection3d(Line3DCollection(charizard.body, colors='k', linewidths=0.2, linestyles='-'))
    body_data = charizard.body.transpose()
    ax.plot(body_data[0,:],body_data[1,:],body_data[2,:],'r')
    return

def remove_charizard_from_canvas():
    ax.clear()
    set_axis_scale()
    draw_camera_on_canvas()
    return

def update_canvas():
    fig.canvas.draw()
    time.sleep(0.05)
    return

def set_axis_scale():
    # ax.set_xlim3d([0.0, 10.0])
    ax.set_xlim3d([-15.0, 15.0])
    ax.set_xlabel('X')

    # ax.set_ylim3d([0.0, 10.0])
    ax.set_ylim3d([-5.0, 25.0])
    ax.set_ylabel('Y')

    # ax.set_zlim3d([0.0, 10.0])
    ax.set_zlim3d([-20.0, 10.0])
    ax.set_zlabel('Z')
    return

def set_axes_equal(ax, charizard):
    #Make axes of 3D plot have equal scale so that spheres appear as spheres,
    #cubes as cubes, etc..  This is one possible solution to Matplotlib's
    #ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    #Input
    #  ax: a matplotlib axis, e.g., as output from plt.gca().
    ax.auto_scale_xyz(charizard.body[0,:],charizard.body[1,:],charizard.body[2,:])

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

# EVENT HANDLERS ############################################################################################################################

def on_key_press(event):
    if currentObject.get() == OBJECTS[0][1]:
        if event.keysym == "KP_6":
            charizardGoRight()
        elif event.keysym == "KP_4":
            charizardGoLeft()
        elif event.keysym == "KP_8":
            charizardGoOn()
        elif event.keysym == "KP_2":
            charizardGoBack()
        elif event.keysym == "KP_7":
            charizardGoUpLeft()
        elif event.keysym == "KP_9":
            charizardGoUpRight()
        elif event.keysym == "KP_1":
            charizardGoDownLeft()
        elif event.keysym == "KP_3":
            charizardGoDownRight()
        elif event.keysym == "KP_Add":
            charizardGoUp()
        elif event.keysym == "KP_Enter":
            charizardGoDown() 

    elif currentObject.get() == OBJECTS[1][1]:
            if event.keysym == "KP_6":
                cameraGoRight()
            elif event.keysym == "KP_4":
                cameraGoLeft()
            elif event.keysym == "KP_8":
                cameraGoOn()
            elif event.keysym == "KP_2":
                cameraGoBack()
            elif event.keysym == "KP_7":
                cameraGoUpLeft()
            elif event.keysym == "KP_9":
                cameraGoUpRight()
            elif event.keysym == "KP_1":
                cameraGoDownLeft()
            elif event.keysym == "KP_3":
                cameraGoDownRight()
            elif event.keysym == "KP_Add":
                cameraGoUp()
            elif event.keysym == "KP_Enter":
                cameraGoDown()   
    return

def rotate_x_handler(current_orientation):
    rotation_angle = x_rotation_value.get() - current_orientation
    # print('Current orientation: {value}'.format(value=current_orientation))
    # print('New orientation: {value}'.format(value=x_rotation_value.get()))
    # print('Rotate {value}'.format(value=rotation_angle))
    if currentObject.get() == OBJECTS[0][1]:
        diceRotateX(rotation_angle)
    global x_current_orientation 
    x_current_orientation  = x_rotation_value.get()
    return

def rotate_y_handler(current_orientation):
    rotation_angle = y_rotation_value.get() - current_orientation
    # print('Current orientation: {value}'.format(value=current_orientation))
    # print('New orientation: {value}'.format(value=y_rotation_value.get()))
    # print('Rotate {value}'.format(value=(y_rotation_value.get() - current_orientation)))
    if currentObject.get() == OBJECTS[0][1]:
        diceRotateY(rotation_angle)
    global y_current_orientation 
    y_current_orientation  = y_rotation_value.get()
    return

def rotate_z_handler(current_orientation):
    rotation_angle = z_rotation_value.get() - current_orientation
    # print('Current orientation: {value}'.format(value=current_orientation))
    # print('New orientation: {value}'.format(value=y_rotation_value.get()))
    # print('Rotate {value}'.format(value=(y_rotation_value.get() - current_orientation)))
    if currentObject.get() == OBJECTS[1][1]:
        diceRotateZ(rotation_angle)
    global z_current_orientation 
    z_current_orientation  = z_rotation_value.get()
    return

# APP's ENTRY POINT  ###########################################################################################################################         
master = Tk()
master.wm_title("Trab1")
master.configure(background="white")

master.bind("<Key>", on_key_press)

left = Frame(master=master)
left.pack(side=tkinter.LEFT, expand=False, fill=tkinter.Y)
center = Frame(master=master)
center.pack(side=tkinter.LEFT,expand=True)
right = Frame(master=master)
right.pack(side=tkinter.LEFT,expand=False)

currentObject = StringVar()
currentObject.set(OBJECTS[0][1])

currentRotation = StringVar()
currentRotation.set("NONE")

x_rotation_value = tkinter.IntVar()
x_rotation_value.set(0)
x_rotation_value.trace("w", lambda *args: rotate_x_handler(x_current_orientation))

y_rotation_value = tkinter.IntVar()
y_rotation_value.set(0)
y_rotation_value.trace("w", lambda *args: rotate_y_handler(y_current_orientation))

z_rotation_value = tkinter.IntVar()
z_rotation_value.set(0)
z_rotation_value.trace("w", lambda *args: rotate_z_handler(z_current_orientation))

f_value = tkinter.IntVar()
f_value.set(0)

sx_value = tkinter.IntVar()
sx_value.set(0)

sy_value = tkinter.IntVar()
sy_value.set(0)

stheta_value = tkinter.IntVar()
stheta_value.set(0)

ox_value = tkinter.IntVar()
ox_value.set(0)

oy_value = tkinter.IntVar()
oy_value.set(0)

# TOGGLE BUTTONS - DICE AND CAMERA SELECTORS ######################################################################################

# Container
object_selector_container = tkinter.Frame(left)
object_selector_container.pack(pady=STYLING_PARAMETERS['container_pady'])

# Label
object_selector_label = tkinter.Label(object_selector_container, text="Select Object", width=16)
object_selector_label.pack()

# Buttons
for text, mode in OBJECTS:
    b = tkinter.Radiobutton(object_selector_container, text=text,
                    variable=currentObject, value=mode, indicatoron=0, width=15)
    b.pack(pady=1)

# RADIO BUTTONS - ROTATION SELECTORS #############################################################################################
# Container
rotation_selector_container = tkinter.Frame(left)
rotation_selector_container.pack(pady=STYLING_PARAMETERS['container_pady'])

# Label
rotation_selector_label = tkinter.Label(rotation_selector_container, text="Rotation Controls", width=17)
rotation_selector_label.pack()

# Sliders
x_rotation_slider = MySlider(rotation_selector_container, x_rotation_value, "X", 0, 360, 2)
x_rotation_slider.pack(pady=1)

y_rotation_slider = MySlider(rotation_selector_container, y_rotation_value, "Y", 0, 360, 2)
y_rotation_slider.pack(pady=1)

z_rotation_slider = MySlider(rotation_selector_container, z_rotation_value, "Z", 0, 360, 2)
z_rotation_slider.pack(pady=1)

# Radio Buttons TROQUEI PELOS SLIDERS
# for text, mode in ROTATIONS:
#     c = tkinter.Radiobutton(rotation_selector_container, text=text,
#                     variable=currentRotation, value=mode, indicatoron=1, width=15)
#     c.pack(pady=1)

# SLIDERS - INTRINSIC PARAMETERS ##################################################################################################
# Container
intrinsic_params_container = tkinter.Frame(left)
intrinsic_params_container.pack(pady=STYLING_PARAMETERS['container_pady'])

# Label
intrinsic_params_label = tkinter.Label(intrinsic_params_container, text="Intrinsic Params", width=17)
intrinsic_params_label.pack()

# Sliders
f_slider = MySlider(intrinsic_params_container, f_value, "f", 0, 1000, 10)
f_slider.pack(pady=1)

sx_slider = MySlider(intrinsic_params_container, sx_value,"sx", 0, 10, 0.1)
sx_slider.pack(pady=1)

sy_slider = MySlider(intrinsic_params_container, sy_value,"sy", 0, 10, 0.1)
sy_slider.pack(pady=1)

s_theta_slider = MySlider(intrinsic_params_container, stheta_value,"s_theta", 0, 10, 0.1)
s_theta_slider.pack(pady=1)

ox_slider = MySlider(intrinsic_params_container, ox_value, "ox", 0, 1000, 10)
ox_slider.pack(pady=1)

oy_slider = MySlider(intrinsic_params_container, oy_value, "oy", 0, 100, 10)
oy_slider.pack(pady=1)

# 3D PLOTTING AREA ##################################################################################################################
fig = Figure(figsize=(9, 6), dpi=100)
ax = fig.add_subplot(1,1,1, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=center)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
canvas.mpl_connect("key_press_event", on_key_press)

# 2D PLOTTING AREA ##################################################################################################################
fig_2 = Figure(figsize=(5, 4), dpi=100)
ax_2 = fig_2.add_subplot(1,1,1)
canvas_2 = FigureCanvasTkAgg(fig_2, master=right)  # A tk.DrawingArea.
canvas_2.draw()
canvas_2.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=0)

# CREATE OBJECTS #############################################################################################################
# DICE
# cube_definition = np.array([[0,0,0,1],[0,2,0,1],[2,0,0,1],[0,0,2,1]])
# dice = Dice(cube_definition)

# CAMERA
camera = CameraAxis()
# Charizard
charizard = Charizard()

set_axis_scale()
# set_axes_equal(ax, charizard)
# DRAW OBJECTS #############################################################################################################
draw_camera_on_canvas()
draw_charizard_on_canvas()

update_canvas()
# START MAIN LOOP #################################################################################################################
master.mainloop()





