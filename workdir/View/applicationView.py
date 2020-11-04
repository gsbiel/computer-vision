import tkinter

from ViewModel.appViewModelInterface import ApplicationViewModelInterface 
from View.ViewComponents.camParamsView import CameraParamsView
from View.ViewComponents.objSelectorView import ObjectSelectorView
from View.ViewComponents.referencesView import ReferencesView
from View.ViewComponents.rotationControlsView import RotationControlsView
from View.worldView import WorldView
from View.projectionView import ProjectionView


class ApplicationView(ApplicationViewModelInterface):

  def __init__(self, viewModel, title="Trabalho 1"):

    self._viewModel = viewModel

    # Master Frame
    self._master = tkinter.Tk()
    self._master.wm_title(title)
    self._master.configure(background="white")

    # Children frames
    self._top = tkinter.Frame(master=self._master)
    self._top.pack(side=tkinter.TOP, fill=tkinter.X)

    self._left = tkinter.Frame(master=self._master)
    self._left.pack(side=tkinter.LEFT,expand=True, fill=tkinter.Y)

    self._center = tkinter.Frame(master=self._master)
    self._center.pack(side=tkinter.LEFT,expand=False)
    
    self._right = tkinter.Frame(master=self._master)
    self._right.pack(side=tkinter.LEFT,expand=False)

    # Painel Elements
    self._referencesView = ReferencesView(self._top, viewModel)

    # User controls
    self._objSelectorView = ObjectSelectorView(self._left, viewModel)
    self._rotationControlsView = RotationControlsView(self._left, viewModel)
    self._cameraParamsView = CameraParamsView(self._left, viewModel)
    
    # Plotting Areas
    self._worldView = WorldView(self._center, viewModel)
    self._projectionView = ProjectionView(self._right, viewModel)

    self.registerForEvents(viewModel)
    return

  # GETTERS ################################################################################
  def get_masterView(self):
    return self._master

  def get_leftView(self):
    return self._left

  def get_centerView(self):
    return self._center

  def get_rightView(self):
    return self._right

  # METHODS ################################################################################
  def registerForEvents(self, viewModel):
    self._master.bind("<Key>", lambda event: viewModel.onKeyboardPressed(event.keysym))
    return

  def startMainLoop(self):
    self._master.mainloop()
    return

  # PROTOCOLS ##############################################################################
  def referencesViewShouldUpdate(self, obj, camera):
    self._referencesView.updateReferences(obj, camera)
    return
  
  def worldViewShouldUpdate(self):
    self._worldView.updateFigure(self._viewModel)
    return
  
  def projectionViewShouldUpdate(self):
    self._projectionView.updateFigure(self._viewModel)
    return