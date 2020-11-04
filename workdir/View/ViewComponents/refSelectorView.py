import tkinter

OBJECTS = [
  ("Selected object", "SELECTED_OBJECT"),
  ("World", "WORLD"),
]

STYLING_PARAMETERS = {
  "masterFrame_pady":5,
  "masterFrame_padx":30,
  "labelView_width":16,
  "buttons_width": 15,
}

class ReferenceSelectorView:

  def __init__(self, parentView, viewModel):

    # Keeps track of the current selected object
    self._selectedReference = tkinter.StringVar()
    self._selectedReference.set(OBJECTS[0][1])

    # Master frame
    self._masterFrame = tkinter.Frame(parentView)
    self._masterFrame.pack(
                            padx=STYLING_PARAMETERS['masterFrame_padx'],
                            pady=STYLING_PARAMETERS['masterFrame_pady']
                          )

    # Label
    self._viewLabel = tkinter.Label(  
                                      self._masterFrame, 
                                      text="Reference on", 
                                      width=STYLING_PARAMETERS["labelView_width"]
                                    )
    self._viewLabel.pack()

    # Buttons
    for text, mode in OBJECTS:
      button = tkinter.Radiobutton( 
                                    self._masterFrame, 
                                    text=text,
                                    variable=self._selectedReference, 
                                    value=mode, 
                                    indicatoron=0, 
                                    width=STYLING_PARAMETERS["buttons_width"]
                                  )
      button.pack(pady=1)
    
    self.__registerForEvents(viewModel)

    return

  # PRIVATE METHODS ############################################################
  def __registerForEvents(self, viewModel):
    self._selectedReference.trace("w", lambda *args: viewModel.selectedReferenceChanged(self._selectedReference.get()))
    return

  

  

  