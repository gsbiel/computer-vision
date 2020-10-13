from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class CameraAxis:

    def __init__(self, ax):
        self.ax = ax

    def draw(self):
        self.ax.quiver(0, 0, 0, 1, 0, 0, length=2, normalize=True, color="g")
        self.ax.quiver(0, 0, 0, 0, 1, 0, length=2, normalize=True, color="b")
        self.ax.quiver(0, 0, 0, 0, 0, 1, length=2, normalize=True, color="r")