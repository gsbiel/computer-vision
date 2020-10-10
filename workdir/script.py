import tkinter
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np
from dice import Dice 
import time


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
#     ax.set_aspect('auto')
    
    return 0

def on_key_press(event):
    print("you pressed {}".format(event.key))
    if currentAxis.get() == "X":
        if event.key == "right":
            dice.translateX(1)
            plot_faces(dice.faces, ax)
            fig.canvas.draw()
            time.sleep(0.05)
        if event.key == "left":
            dice.translateX(-1)
            plot_faces(dice.faces, ax)
            fig.canvas.draw()
            time.sleep(0.01)
        if event.key == "up":
            dice.translateZ(1)
            plot_faces(dice.faces, ax)
            fig.canvas.draw()
            time.sleep(0.01)
        if event.key == "down":
            dice.translateZ(-1)
            plot_faces(dice.faces, ax)
            fig.canvas.draw()
            time.sleep(0.01)            

    elif currentAxis.get() == "Y":
        if event.key == "right":
            dice.translateY(1)
            plot_faces(dice.faces, ax)
            fig.canvas.draw()
            time.sleep(0.05)
        if event.key == "left":
            dice.translateY(-1)
            plot_faces(dice.faces, ax)
            fig.canvas.draw()
            time.sleep(0.01)
        if event.key == "up":
            dice.translateZ(1)
            plot_faces(dice.faces, ax)
            fig.canvas.draw()
            time.sleep(0.01)
        if event.key == "down":
            dice.translateZ(-1)
            plot_faces(dice.faces, ax)
            fig.canvas.draw()
            time.sleep(0.01)

    elif currentAxis.get() == "Z":
        if event.key == "right" or event.key == "up":
            dice.translateZ(1)
            plot_faces(dice.faces, ax)
            fig.canvas.draw()
            time.sleep(0.05)
        if event.key == "left" or event.key == "down":
            dice.translateZ(-1)
            plot_faces(dice.faces, ax)
            fig.canvas.draw()
            time.sleep(0.01)

    key_press_handler(event, canvas, toolbar)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

root = tkinter.Tk()
root.wm_title("Trab1")

currentAxis = StringVar()
currentAxis.set("X")

left_frame = tkinter.Frame(root).pack(side = "left")

for text, mode in MODES:
    b = tkinter.Radiobutton(left_frame, text=text,
                    variable=currentAxis, value=mode, indicatoron=0)
    b.pack()

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1,1,1, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

canvas.mpl_connect("key_press_event", on_key_press)

button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

cube_definition = np.array([[0,0,0,1],[0,2,0,1],[2,0,0,1],[0,0,2,1]])
dice = Dice(cube_definition)

plot_faces(dice.faces, ax)
fig.canvas.draw()

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.



