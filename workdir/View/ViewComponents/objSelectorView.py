import tkinter

OBJECTS = [
  ("Object", "OBJECT"),
  ("Camera Axis", "CAMERA"),
]

STYLING_PARAMETERS = {
  "masterFrame_pady":20,
  "labelView_width":16,
  "buttons_width": 15,
}

class ObjectSelectorView:

  def __init__(self, parentView, viewModel):

    # Keeps track of the current selected object
    self._selectedObject = tkinter.StringVar()
    self._selectedObject.set(OBJECTS[0][1])

    # Master frame
    self._masterFrame = tkinter.Frame(parentView)
    self._masterFrame.pack(pady=STYLING_PARAMETERS['masterFrame_pady'])

    # Label
    self._viewLabel = tkinter.Label(  
                                      self._masterFrame, 
                                      text="Select Object", 
                                      width=STYLING_PARAMETERS["labelView_width"]
                                    )
    self._viewLabel.pack()

    # Buttons
    for text, mode in OBJECTS:
      button = tkinter.Radiobutton( 
                                    self._masterFrame, 
                                    text=text,
                                    variable=self._selectedObject, 
                                    value=mode, 
                                    indicatoron=0, 
                                    width=STYLING_PARAMETERS["buttons_width"]
                                  )
      button.pack(pady=1)
    
    self.__registerForEvents(viewModel)

    return

  # PRIVATE METHODS ############################################################
  def __registerForEvents(self, viewModel):
    self._selectedObject.trace("w", lambda *args: viewModel.selectedObjectChanged(self._selectedObject.get()))
    return

  

  

  