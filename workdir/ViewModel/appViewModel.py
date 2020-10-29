import numpy as np
from Model.camera import CameraModel
from Model.object import ObjectModel

referenceInCamera = np.array([12,-20,0,1])
referenceInObject = np.array([0, 10, -5, 1])

class ApplicationViewModel:

  def __init__(self):
    self.delegate = None
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
  
  # GUI EVENTS #########################################################################################################
  
  def onKeyboardPressed(self, key):
    if self._currentObject == OBJECTS[0][1]:
      if key == "KP_6":
        self._objectModel.translateX(1) # Go Right (X+)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_4":
        self._objectModel.translateX(-1) # Go Left (X-)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_8":
        self._objectModel.translateY(1) # Go On (Y+)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_2":
        self._objectModel.translateY(-1) # Go Back (Y-)
        self.delegate.worldViewShouldUpdate() 
      elif key == "KP_7":
        self._objectModel.translateXY("01") # Go On-Left (XY plane)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_9":
        self._objectModel.translateXY("11") # Go On-Right (XY plane)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_1":
        self._objectModel.translateXY("00") # Go Back-Left (XY plane)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_3":
        self._objectModel.translateXY("10") # Go Back-Right (XY plane)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_Add":
        self._objectModel.translateZ(1) # Go Up (Z+)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_Enter":
        self._objectModel.translateZ(-1) # Go Down (Z-)
        self.delegate.worldViewShouldUpdate()

    elif self._currentObject == OBJECTS[1][1]:
      if key == "KP_6":
        self._cameraModel.translateX(1) # Go Right (X+)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_4":
        self._cameraModel.translateX(-1) # Go Left (X-)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_8":
        self._cameraModel.translateY(1) # Go On (Y+)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_2":
        self._cameraModel.translateY(-1) # Go Back (Y-) 
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_7":
        self._cameraModel.translateXY("01") # Go On-Left (XY plane)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_9":
        self._cameraModel.translateXY("11") # Go On-Right (XY plane)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_1":
        self._cameraModel.translateXY("00") # Go Back-Left (XY plane)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_3":
        self._cameraModel.translateXY("10") # Go Back-Right (XY plane)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_Add":
        self._cameraModel.translateZ(1) # Go Up (Z+)
        self.delegate.worldViewShouldUpdate()
      elif key == "KP_Enter":
        self._cameraModel.translateZ(-1) # Go Down (Z-)
        self.delegate.worldViewShouldUpdate()
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

  