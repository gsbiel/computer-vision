import tkinter
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

OBJECT_STYLING = {
  "colors":"k",
  "lineWidth":0.2,
  "linestyles":"-"
}

class WorldView:

  def __init__(self, parentView, viewModel):
    self._masterView = parentView
    self._fig = Figure(figsize=(7, 6), dpi=100)
    self._ax = self._fig.add_subplot(1,1,1, projection='3d')
    self._canvas = FigureCanvasTkAgg(self._fig, master=self._masterView)  # A tk.DrawingArea.
    self._canvas.draw()
    self._canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    self.updateObject(viewModel.get_objectMesh())
    return

  # PUBLIC METHODS #############################################################
  def updateCamera(self, cameraBody):
    # self.__resetFigure(self._ax)
    return

  def updateObject(self, objectVectors):
    self.__refreshFigure(self._ax)
    self.__drawObject(self._ax, objectVectors)
    self.__updateCanvas()
    return

  # PRIVATE METHODS ####################################################################################################
  def __updateCanvas(self):
    self._fig.canvas.draw()
    time.sleep(0.01)
    return
  
  def __drawObject(self, ax, objectVectors):
    ax.add_collection3d(Poly3DCollection(objectVectors))
    ax.add_collection3d(Line3DCollection(
                                          objectVectors, 
                                          colors = OBJECT_STYLING["colors"], 
                                          linewidths= OBJECT_STYLING["lineWidth"], 
                                          linestyles= OBJECT_STYLING["linestyles"], 
                                        ))
    return

  def __refreshFigure(self, ax):
    self.__cleanFigure(ax)
    self.__set_axis_scale(ax)
    return

  def __set_axis_scale(self, ax):
    # X axis
    ax.set_xlim3d([-15.0, 15.0])
    ax.set_xlabel('X')
    # Y axis
    ax.set_ylim3d([-5.0, 25.0])
    ax.set_ylabel('Y')
    # Z axis
    ax.set_zlim3d([-20.0, 10.0])
    ax.set_zlabel('Z')
    return

  def __cleanFigure(self, ax):
    ax.clear()
    return
