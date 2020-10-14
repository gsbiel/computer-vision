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

OBJECTS = [
        ("Dice", "DICE"),
        ("Camera Axis", "CAMERA"),
    ]

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

def diceGoRight():
    print("Vai pra direita.")
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

def draw_dice_on_canvas(faces,ax):
    ax.add_collection3d(faces)
    return

def remove_dice_from_canvas():
    ax.clear()
    set_axis_scale()
    draw_camera_on_canvas()
    return

def draw_camera_on_canvas():
    camera.draw()
    return

def remove_camera_from_canvas():
    return

def update_canvas():
    fig.canvas.draw()
    time.sleep(0.05)
    return

def set_axis_scale():
    ax.set_xlim3d([0.0, 15.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 15.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 15.0])
    ax.set_zlabel('Z')
    return

def on_key_press(event):
    print("you pressed {}".format(event.keysym))

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
    
    return
            
master = Tk()
master.wm_title("Trab1")
master.configure(background="white")

master.bind("<Key>", on_key_press)

left = Frame(master=master)
left.pack(side=tkinter.LEFT, expand=False)
center = Frame(master=master)
center.pack(side=tkinter.LEFT,expand=True)
right = Frame(master=master)
right.pack(side=tkinter.LEFT,expand=False)

currentObject = StringVar()
currentObject.set("DICE")

for text, mode in OBJECTS:
    b = tkinter.Radiobutton(left, text=text,
                    variable=currentObject, value=mode, indicatoron=0)
    b.pack()

fig = Figure(figsize=(9, 6), dpi=100)
ax = fig.add_subplot(1,1,1, projection='3d')


canvas = FigureCanvasTkAgg(fig, master=center)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

canvas.mpl_connect("key_press_event", on_key_press)

fig_2 = Figure(figsize=(5, 4), dpi=100)
ax_2 = fig_2.add_subplot(1,1,1)
canvas_2 = FigureCanvasTkAgg(fig_2, master=right)  # A tk.DrawingArea.
canvas_2.draw()
canvas_2.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=0)


cube_definition = np.array([[0,0,0,1],[0,2,0,1],[2,0,0,1],[0,0,2,1]])
dice = Dice(cube_definition)

set_axis_scale()
camera = CameraAxis(ax)
draw_dice_on_canvas(dice.faces, ax)
draw_camera_on_canvas()
update_canvas()

master.mainloop()





