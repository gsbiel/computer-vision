import tkinter

from View.ViewComponents.camParamsView import CameraParamsView
from View.ViewComponents.objSelectorView import ObjectSelectorView
from View.ViewComponents.rotationControlsView import RotationControlsView

class ApplicationView:

  def __init__(self, viewModel, title="Trabalho 1"):
    # Master Frame
    self._master = tkinter.Tk()
    self._master.wm_title(title)
    self._master.configure(background="white")

    # Children frames
    self._left = tkinter.Frame(master=self._master)
    self._left.pack(side=tkinter.LEFT, expand=True, fill=tkinter.Y)

    self._center = tkinter.Frame(master=self._master)
    self._center.pack(side=tkinter.LEFT,expand=False)
    
    self._right = tkinter.Frame(master=self._master)
    self._right.pack(side=tkinter.LEFT,expand=False)

    # User controls
    self._objSelectorView = ObjectSelectorView(self._left, viewModel)
    self._rotationControlsView = RotationControlsView(self._left, viewModel)
    self._cameraParamsView = CameraParamsView(self._left, viewModel)
    
    self.registerForEvents(viewModel)
    return

  # GETTERS ####################################################################
  def get_masterView(self):
    return self._master

  def get_leftView(self):
    return self._left

  def get_centerView(self):
    return self._center

  def get_rightView(self):
    return self._right

  # METHODS ####################################################################
  def registerForEvents(self, viewModel):
    self._master.bind("<Key>", viewModel.onKeyboardPressed)
    return

  def startMainLoop(self):
    self._master.mainloop()
    return