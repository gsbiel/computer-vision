import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class WorldView:

  def __init__(self, parentView):
    self._fig = Figure(figsize=(7, 6), dpi=100)
    self._ax = self._fig.add_subplot(1,1,1, projection='3d')
    self._canvas = FigureCanvasTkAgg(self._fig, master=parentView)  # A tk.DrawingArea.
    self._canvas.draw()
    self._canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    # self._canvas.mpl_connect("key_press_event", on_key_press)
    return
