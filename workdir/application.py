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


MODES = [
        ("x axis", "X"),
        ("y axis", "Y"),
        ("z axis", "Z"),
    ]

def plot_faces(faces,ax):
    
    ax.clear()
    ax.set_xlim3d([0.0, 15.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 15.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 15.0])
    ax.set_zlabel('Z')
    
    ax.add_collection3d(faces)

    return 0


def on_key_press(event):
    print("you pressed {}".format(event.keysym))
    if currentAxis.get() == "X":
        if event.keysym == "Right":
            dice.translateX(1)
            plot_faces(dice.faces, ax)
            camera.draw()
            fig.canvas.draw()
            time.sleep(0.05)
        if event.keysym == "Left":
            dice.translateX(-1)
            plot_faces(dice.faces, ax)
            camera.draw()
            fig.canvas.draw()
            time.sleep(0.01)
        if event.keysym == "Up":
            dice.translateZ(1)
            plot_faces(dice.faces, ax)
            camera.draw()
            fig.canvas.draw()
            time.sleep(0.01)
        if event.keysym == "Down":
            dice.translateZ(-1)
            plot_faces(dice.faces, ax)
            camera.draw()
            fig.canvas.draw()
            time.sleep(0.01)            

    elif currentAxis.get() == "Y":
        if event.keysym == "Right":
            dice.translateY(1)
            plot_faces(dice.faces, ax)
            camera.draw()
            fig.canvas.draw()
            time.sleep(0.05)
        if event.keysym == "Left":
            dice.translateY(-1)
            plot_faces(dice.faces, ax)
            camera.draw()
            fig.canvas.draw()
            time.sleep(0.01)
        if event.keysym == "Up":
            dice.translateZ(1)
            plot_faces(dice.faces, ax)
            camera.draw()
            fig.canvas.draw()
            time.sleep(0.01)
        if event.keysym == "Down":
            dice.translateZ(-1)
            plot_faces(dice.faces, ax)
            camera.draw()
            fig.canvas.draw()
            time.sleep(0.01)

    elif currentAxis.get() == "Z":
        if event.keysym == "Right" or event.keysym == "Up":
            dice.translateZ(1)
            plot_faces(dice.faces, ax)
            camera.draw()
            fig.canvas.draw()
            time.sleep(0.05)
        if event.keysym == "Left" or event.keysym == "Down":
            dice.translateZ(-1)
            plot_faces(dice.faces, ax)
            camera.draw()
            fig.canvas.draw()
            time.sleep(0.01)

    # key_press_handler(event, canvas)


def get_arrow(theta):
    x = np.cos(theta)
    y = np.sin(theta)
    z = 0
    u = np.sin(2*theta)
    v = np.sin(3*theta)
    w = np.cos(3*theta)
    return x,y,z,u,v,w



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

currentAxis = StringVar()
currentAxis.set("X")

for text, mode in MODES:
    b = tkinter.Radiobutton(left, text=text,
                    variable=currentAxis, value=mode, indicatoron=0)
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
camera = CameraAxis(ax)
plot_faces(dice.faces, ax)
camera.draw()
fig.canvas.draw()

master.mainloop()





