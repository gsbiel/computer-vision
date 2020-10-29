import numpy as np
from Model.camera import CameraModel
from Model.object import ObjectModel

referenceInCamera = np.array([12,-20,0,1])
referenceInObject = np.array([0, 10, -5, 1])

class ApplicationViewModel:

  def __init__(self):
    self._cameraModel = CameraModel(
                                      np.array([referenceInCamera]), 
                                      np.array([[1,0,0,1],[0,1,0,1],[0,0,1,1]])
                                    )
    self._objectModel = ObjectModel(referenceInObject)
    return

  # GETTERS ############################################################################################################
  def get_objectMesh(self):
    return self._objectModel.get_objectVectors()
  
  def get_cameraMainPoint(self):
    return self._cameraModel.get_mainPoint()

  def get_cameraDirectionVectors(self):
    return self._cameraModel.get_directionVectors()
  
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

  