import numpy as np

class ApplicationViewModel:

  def __init__(self):

    return

  
  # GUI EVENTS #################################################################
  
  def onKeyboardPressed(self, key):
    print('Key pressed: {value}'.format(value=key))
    return

  def selectedObjectChanged(self, currentObject):
    print('Object changed to: {value}'.format(value=currentObject))
    return

  def xOrientationChanged(self, orientation):
    print('X orientation changed to: {value}'.format(value=orientation))
    return

  def yOrientationChanged(self, orientation):
    print('Y orientation changed to: {value}'.format(value=orientation))
    return

  def zOrientationChanged(self, orientation):
    print('Z orientation changed to: {value}'.format(value=orientation))
    return

  def intrinsincParamsChanged(self, f, sx, sy, stheta, ox, oy):
    print('Intrinsic params changed to: {value}'.format(value=np.array([[f,sx,sy, stheta, ox, oy]]).transpose()))  
    return

  