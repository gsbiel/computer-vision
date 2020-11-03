import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

class ProjectionView:
  def __init__(self, parentView, viewModel):
    self._masterView = parentView
    self._fig = Figure(figsize=(5, 4), dpi=100)
    self._ax = self._fig.add_subplot(1,1,1)
    # self._ax.set_xlim([0, 640])
    # self._ax.set_ylim([0, 640])
    # self._ax.set_xlim([-5000, 5000])
    # self._ax.set_ylim([-5000, 5000])
    self._canvas = FigureCanvasTkAgg(self._fig, master=self._masterView)  # A tk.DrawingArea.
    self._canvas.draw()
    self._canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=0)
    return

  # PUBLIC METHODS ###############################################################################
  def updateFigure(self, viewModel):
    self.__refreshFigure(self._ax)
    self.__drawProjection(viewModel)
    self.__updateCanvas()
    return

  # PRIVATE METHODS ###############################################################################

  def __drawProjection(self, viewModel):
    projection = viewModel.get_cameraProjection()
    self._ax.plot(projection[:,0], projection[:,1],'k')
    return

  def __refreshFigure(self, ax):
    self.__cleanFigure(ax)
    self.__set_axis_scale(ax)
    return
  
  def __cleanFigure(self, ax):
    ax.clear()
    return

  def __updateCanvas(self):
    self._fig.canvas.draw()
    time.sleep(0.01)
    return

  def __set_axis_scale(self, ax):
    # ax.set_xlim([0, 640])
    # ax.set_ylim([0, 640])
    # self._ax.set_xlim([-5000, 5000])
    # self._ax.set_ylim([-5000, 5000])
    return