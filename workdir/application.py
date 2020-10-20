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
import time
from mpl_toolkits.mplot3d import Axes3D

from slider import MySlider

OBJECTS = [
        ("Dice", "DICE"),
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

# DICE MOVEMENT EVENTS ##################################################################################################################

def diceGoRight():
    remove_dice_from_canvas()
    dice.translateX(1)
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas()
    return 

def diceGoLeft():
    remove_dice_from_canvas()
    dice.translateX(-1)
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas()
    return

def diceGoOn():
    remove_dice_from_canvas()
    dice.translateY(1)
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas()
    return

def diceGoBack():
    remove_dice_from_canvas()
    dice.translateY(-1)  
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas()
    return

def diceGoUpLeft():
    remove_dice_from_canvas()
    dice.translateXY("01")
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas()    
    return

def diceGoUpRight():
    remove_dice_from_canvas()
    dice.translateXY("11")
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas() 
    return

def diceGoDownLeft():
    remove_dice_from_canvas()
    dice.translateXY("00")
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas() 
    return

def diceGoDownRight():
    remove_dice_from_canvas()
    dice.translateXY("10")
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas() 
    return

def diceGoUp():
    remove_dice_from_canvas()
    dice.translateZ(1)
    draw_dice_on_canvas(dice.faces, ax)
    update_canvas()
    return

def diceGoDown():
    remove_dice_from_canvas()
    dice.translateZ(-1)
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

def draw_dice_on_canvas(faces,ax):
    ax.add_collection3d(faces)
    return

def remove_dice_from_canvas():
    ax.clear()
    set_axis_scale()
    draw_camera_on_canvas()
    return

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
    draw_dice_on_canvas(dice.faces, ax)
    return

def update_canvas():
    fig.canvas.draw()
    time.sleep(0.05)
    return

def set_axis_scale():
    ax.set_xlim3d([0.0, 10.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 10.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 10.0])
    ax.set_zlabel('Z')
    return

# EVENT HANDLERS ############################################################################################################################

def on_key_press(event):
    if currentObject.get() == "DICE":
        if event.keysym == "KP_6":
            diceGoRight()
        elif event.keysym == "KP_4":
            diceGoLeft()
        elif event.keysym == "KP_8":
            diceGoOn()
        elif event.keysym == "KP_2":
            diceGoBack()
        elif event.keysym == "KP_7":
            diceGoUpLeft()
        elif event.keysym == "KP_9":
            diceGoUpRight()
        elif event.keysym == "KP_1":
            diceGoDownLeft()
        elif event.keysym == "KP_3":
            diceGoDownRight()
        elif event.keysym == "KP_Add":
            diceGoUp()
        elif event.keysym == "KP_Enter":
            diceGoDown() 

    elif currentObject.get() == "CAMERA":
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
currentObject.set("DICE")

currentRotation = StringVar()
currentRotation.set("NONE")

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
x_rotation_slider = MySlider(rotation_selector_container,"X", 0, 360, 2)
x_rotation_slider.pack(pady=1)

y_rotation_slider = MySlider(rotation_selector_container,"Y", 0, 360, 2)
y_rotation_slider.pack(pady=1)

z_rotation_slider = MySlider(rotation_selector_container,"Z", 0, 360, 2)
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
f_slider = MySlider(intrinsic_params_container,"f", 0, 1000, 10)
f_slider.pack(pady=1)

sx_slider = MySlider(intrinsic_params_container,"sx", 0, 10, 0.1)
sx_slider.pack(pady=1)

sy_slider = MySlider(intrinsic_params_container,"sy", 0, 10, 0.1)
sy_slider.pack(pady=1)

s_theta_slider = MySlider(intrinsic_params_container,"s_theta", 0, 10, 0.1)
s_theta_slider.pack(pady=1)

ox_slider = MySlider(intrinsic_params_container,"ox", 0, 1000, 10)
ox_slider.pack(pady=1)

oy_slider = MySlider(intrinsic_params_container,"oy", 0, 100, 10)
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

# DRAW DICE AND CAMERA #############################################################################################################
cube_definition = np.array([[0,0,0,1],[0,2,0,1],[2,0,0,1],[0,0,2,1]])
dice = Dice(cube_definition)
set_axis_scale()
camera = CameraAxis()
draw_dice_on_canvas(dice.faces, ax)
draw_camera_on_canvas()
update_canvas()

# START MAIN LOOP #################################################################################################################
master.mainloop()





