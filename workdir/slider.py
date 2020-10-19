import tkinter

class MySlider:
    def __init__(self, master, label, from_, to_, resolution):
        self.master = master
        self.label = label
        self.from_ = from_
        self.to_ = to_
        self.resolution = resolution
        self.buildComponent()
        return

    def buildComponent(self):
        self.container = tkinter.Frame(master=self.master)
        self.label = tkinter.Label(self.container, text=self.label, width=7).grid(row=0, column=0)
        self.slider = tkinter.Scale(self.container, from_=self.from_, to_=self.to_, orient=tkinter.HORIZONTAL, resolution=self.resolution).grid(row=0, column=1)
        return
    
    def pack(self):
        self.container.pack()
        return