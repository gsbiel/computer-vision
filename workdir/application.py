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
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return 

def charizardGoLeft():
    remove_charizard_from_canvas()
    charizard.translateX(-1)
    draw_charizard_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def charizardGoOn():
    remove_charizard_from_canvas()
    charizard.translateY(1)
    draw_charizard_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def charizardGoBack():
    remove_charizard_from_canvas()
    charizard.translateY(-1)  
    draw_charizard_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def charizardGoUpLeft():
    remove_charizard_from_canvas()
    charizard.translateXY("01")
    draw_charizard_on_canvas()
    update_canvas()  
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())  
    return

def charizardGoUpRight():
    remove_charizard_from_canvas()
    charizard.translateXY("11")
    draw_charizard_on_canvas()
    update_canvas() 
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def charizardGoDownLeft():
    remove_charizard_from_canvas()
    charizard.translateXY("00")
    draw_charizard_on_canvas()
    update_canvas() 
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def charizardGoDownRight():
    remove_charizard_from_canvas()
    charizard.translateXY("10")
    draw_charizard_on_canvas()
    update_canvas() 
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def charizardGoUp():
    remove_charizard_from_canvas()
    charizard.translateZ(1)
    draw_charizard_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def charizardGoDown():
    remove_charizard_from_canvas()
    charizard.translateZ(-1)
    draw_charizard_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def charizardRotateX(angle):
    remove_charizard_from_canvas()
    charizard.rotateX(angle)
    draw_charizard_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def charizardRotateY(angle):
    remove_charizard_from_canvas()
    charizard.rotateY(angle)
    draw_charizard_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def charizardRotateZ(angle):
    remove_charizard_from_canvas()
    charizard.rotateZ(angle)
    draw_charizard_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

# CAMERA MOVEMENT EVENTS ##################################################################################################################

def cameraGoRight():
    remove_camera_from_canvas()
    camera.translateX(1)
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraGoLeft():
    remove_camera_from_canvas()
    camera.translateX(-1)
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraGoOn():
    remove_camera_from_canvas()
    camera.translateY(1)
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraGoBack():
    remove_camera_from_canvas()
    camera.translateY(-1)
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraGoUpLeft():
    remove_camera_from_canvas()
    camera.translateXY("01")
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraGoUpRight():
    remove_camera_from_canvas()
    camera.translateXY("11")
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraGoDownLeft():
    remove_camera_from_canvas()
    camera.translateXY("00")
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraGoDownRight():
    remove_camera_from_canvas()
    camera.translateXY("10")
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraGoUp():
    remove_camera_from_canvas()
    camera.translateZ(1)
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraGoDown():
    remove_camera_from_canvas()
    camera.translateZ(-1)
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraRotateX(angle):
    remove_camera_from_canvas()
    camera.rotateX(angle)
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraRotateY(angle):
    remove_camera_from_canvas()
    camera.rotateY(angle)
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
    return

def cameraRotateZ(angle):
    remove_camera_from_canvas()
    camera.rotateZ(angle)
    draw_camera_on_canvas()
    update_canvas()
    project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get())
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
    ax.add_collection3d(Poly3DCollection(charizard.vectors))
    # Plot the contours of the faces of the object
    ax.add_collection3d(Line3DCollection(charizard.vectors, colors='k', linewidths=0.2, linestyles='-'))
    # body_data = charizard.body.transpose()
    # ax.plot(body_data[0,:],body_data[1,:],body_data[2,:],'r')
    return

def remove_charizard_from_canvas():
    ax.clear()
    set_axis_scale()
    draw_camera_on_canvas()
    return

def update_canvas():
    fig.canvas.draw()
    time.sleep(0.01)
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

def selectedObjectChanged(object):
    if object == OBJECTS[0][1] :
        x_rotation_value.set(charizard.x_orientation)
        y_rotation_value.set(charizard.y_orientation)
        z_rotation_value.set(charizard.z_orientation)
    else:
        x_rotation_value.set(camera.x_orientation)
        y_rotation_value.set(camera.y_orientation)
        z_rotation_value.set(camera.z_orientation)
    return

def rotate_x_handler(current_orientation):
    rotation_angle = x_rotation_value.get()
    # print('Current orientation: {value}'.format(value=current_orientation))
    # print('New orientation: {value}'.format(value=x_rotation_value.get()))
    # print('Rotate {value}'.format(value=rotation_angle))
    if currentObject.get() == OBJECTS[0][1]:
        charizardRotateX(rotation_angle)
    else:
        cameraRotateX(rotation_angle)
    return

def rotate_y_handler(current_orientation):
    rotation_angle = y_rotation_value.get()
    # print('Current orientation: {value}'.format(value=current_orientation))
    # print('New orientation: {value}'.format(value=y_rotation_value.get()))
    # print('Rotate {value}'.format(value=(y_rotation_value.get() - current_orientation)))
    if currentObject.get() == OBJECTS[0][1]:
        charizardRotateY(rotation_angle)
    else:
        cameraRotateY(rotation_angle)
    return

def rotate_z_handler(current_orientation):
    rotation_angle = z_rotation_value.get()
    # print('Current orientation: {value}'.format(value=current_orientation))
    # print('New orientation: {value}'.format(value=y_rotation_value.get()))
    # print('Rotate {value}'.format(value=(y_rotation_value.get() - current_orientation)))
    if currentObject.get() == OBJECTS[0][1]:
        charizardRotateZ(rotation_angle)
    else:
        cameraRotateZ(rotation_angle)
    return

def project_object(f, sx, sy, stheta, ox, oy):
    camera.setIntrinsicParams(f, sx, sy, stheta, ox, oy)
    projection = camera.project(charizard.body)
    plotProjectionOnFigure(projection)
    return

def plotProjectionOnFigure(projection):
    ax_2.clear()
    ax_2.set_xlim([0, 5000])
    ax_2.set_ylim([5000, 0])
    ax_2.plot(projection[:,0], projection[:,1],'k.')
    fig_2.canvas.draw()
    time.sleep(0.01)
    return
    

# APP's ENTRY POINT  ###########################################################################################################################         
master = Tk()
master.wm_title("Trab1")
master.configure(background="white")

master.bind("<Key>", on_key_press)

left = Frame(master=master)
left.pack(side=tkinter.LEFT, expand=True, fill=tkinter.Y)
center = Frame(master=master)
center.pack(side=tkinter.LEFT,expand=False)
right = Frame(master=master)
right.pack(side=tkinter.LEFT,expand=False)

currentObject = StringVar()
currentObject.set(OBJECTS[0][1])
# currentObject.trace("w", lambda *args: selectedObjectChanged(currentObject.get()))

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
f_value.set(350)

sx_value = tkinter.DoubleVar()
sx_value.set(3.5)

sy_value = tkinter.DoubleVar()
sy_value.set(5.3)

stheta_value = tkinter.DoubleVar()
stheta_value.set(0)

ox_value = tkinter.IntVar()
ox_value.set(99)

oy_value = tkinter.IntVar()
oy_value.set(177)

f_value.trace("w", lambda *args: project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get()))
sx_value.trace("w", lambda *args: project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get()))
sy_value.trace("w", lambda *args: project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get()))
stheta_value.trace("w", lambda *args: project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get()))
ox_value.trace("w", lambda *args: project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get()))
oy_value.trace("w", lambda *args: project_object(f_value.get(), sx_value.get(), sy_value.get(), stheta_value.get(), ox_value.get(), oy_value.get()))

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

ox_slider = MySlider(intrinsic_params_container, ox_value, "ox", 0, 640, 10)
ox_slider.pack(pady=1)

oy_slider = MySlider(intrinsic_params_container, oy_value, "oy", 0, 480, 10)
oy_slider.pack(pady=1)

# 3D PLOTTING AREA ##################################################################################################################
fig = Figure(figsize=(7, 6), dpi=100)
ax = fig.add_subplot(1,1,1, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=center)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
canvas.mpl_connect("key_press_event", on_key_press)

# 2D PLOTTING AREA ##################################################################################################################
fig_2 = Figure(figsize=(5, 4), dpi=100)
ax_2 = fig_2.add_subplot(1,1,1)
ax_2.set_xlim([0, 640])
ax_2.set_ylim([640, 0])
canvas_2 = FigureCanvasTkAgg(fig_2, master=right)  # A tk.DrawingArea.
canvas_2.draw()
canvas_2.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=0)

# CREATE OBJECTS #############################################################################################################

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







