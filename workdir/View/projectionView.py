import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ProjectionView:
  def __init__(self, parentView):
    self._masterView = parentView
    self._fig = Figure(figsize=(5, 4), dpi=100)
    self._ax = self._fig.add_subplot(1,1,1)
    self._ax.set_xlim([0, 640])
    self._ax.set_ylim([640, 0])
    self._canvas = FigureCanvasTkAgg(self._fig, master=self._masterView)  # A tk.DrawingArea.
    self._canvas.draw()
    self._canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=0)
    return