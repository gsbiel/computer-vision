import tkinter

STYLING_PARAMETERS = {
  "label_width":14
}

class ReferencesView:

  def __init__(self, parentFrame, viewModel):
    self._master = parentFrame
    self.__buildComponent()
    return

  def __buildComponent(self):
    self._rootContainer = tkinter.Frame(master = self._master)

    self._objectContainer = tkinter.Frame(master = self._rootContainer)
    self._objectContainer.pack()

    self._cameraContainer = tkinter.Frame(master = self._rootContainer)
    self._cameraContainer.pack()
    
    self._objValueString = tkinter.StringVar()
    self._objValueString.set("(x1,y1,z1)")

    self._cameraValueString = tkinter.StringVar()
    self._cameraValueString.set("(x1,y2,z2)")

    # OBJECT
    self._objectLabel = tkinter.Label(
                                        self._objectContainer,
                                        text="Object",
                                        width=STYLING_PARAMETERS["label_width"]
                                      ).grid(row=0,column=0)
    self._objectValue = tkinter.Label(
                                        self._objectContainer,
                                        textvariable=self._objValueString,
                                        width=STYLING_PARAMETERS["label_width"]
                                      ).grid(row=0,column=1)
    
    # CAMERA
    self._cameraLabel = tkinter.Label(
                                        self._cameraContainer,
                                        text="Camera",
                                        width=STYLING_PARAMETERS["label_width"]
                                      ).grid(row=0,column=0)
    self._cameraValue = tkinter.Label(
                                        self._cameraContainer,
                                        textvariable=self._cameraValueString,
                                        width=STYLING_PARAMETERS["label_width"]
                                      ).grid(row=0,column=1)

    self.pack()
    
    return

  def pack(self, pady=1, padx=1):
    self._rootContainer.pack(expand=True, fill=tkinter.X)
    return

  def updateReferences(self, obj, cam):
    if obj is not None:
      self._objValueString.set('({x}, {y}, {z})'.format(
                                                          x='{0:.2f}'.format(obj[0]), 
                                                          y='{0:.2f}'.format(obj[1]), 
                                                          z='{0:.2f}'.format(obj[2])
                                                        ))
    if cam is not None:
      self._cameraValueString.set('({x}, {y}, {z})'.format(
                                                            x='{0:.2f}'.format(cam[0]), 
                                                            y='{0:.2f}'.format(cam[1]), 
                                                            z='{0:.2f}'.format(cam[2])
                                                          ))
    return

