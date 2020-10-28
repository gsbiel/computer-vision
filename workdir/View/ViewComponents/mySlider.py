import tkinter

STYLING_PARAMETERS = {
  "label_width":7
}

class MySlider:
    def __init__(self, master, value, label, from_, to_, resolution):
        self.master = master
        self.label = label
        self.value = value
        self.from_ = from_
        self.to_ = to_
        self.resolution = resolution
        self.buildComponent()
        return

    def buildComponent(self):
        self.container = tkinter.Frame(master=self.master)

        self.label = tkinter.Label(
                                    self.container, 
                                    text=self.label, 
                                    width=STYLING_PARAMETERS["label_width"]
                                  ).grid(row=0, column=0)

        self.slider = tkinter.Scale(
                                      self.container, 
                                      variable=self.value, 
                                      from_=self.from_, 
                                      to_=self.to_, 
                                      orient=tkinter.HORIZONTAL, 
                                      resolution=self.resolution
                                    ).grid(row=0, column=1)
        return
    
    def pack(self, pady=1, padx=1):
        self.container.pack(padx=padx, pady=pady)
        return