import numpy as np
from Model.object import ObjectModel

class ApplicationViewModel:

  def __init__(self):
    self._objectModel = ObjectModel(referenceInObject)
    return

  # GETTERS ############################################################################################################
  def get_objectMesh(self):
    return self._objectModel.get_objectVectors()
  
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

  