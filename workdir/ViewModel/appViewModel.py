import numpy as np
from Model.camera import CameraModel
from Model.object import ObjectModel
from Model.house import HouseModel

OBJECTS = [
  ("Object", "OBJECT"),
  ("Camera Axis", "CAMERA"),
]

referenceInCamera = np.array([0,0,0,1])
referenceInObject = np.array([0, 10, -5, 1])

class ApplicationViewModel:

  def __init__(self):
    self.delegate = None
    self._currentObject = OBJECTS[0][1]
    self._cameraModel = CameraModel(
                                      np.array([referenceInCamera]), 
                                      np.array([[1,0,0,1],[0,1,0,1],[0,0,1,1]]),
                                      referenceInCamera
                                    )
    self._objectModel = ObjectModel(referenceInObject)
    self._houseModel = HouseModel()

    return

  # GETTERS ############################################################################################################
  def get_objectMesh(self):
    return self._objectModel.get_objectVectors()

  def get_cameraMainPoint(self):
    return self._cameraModel.get_mainPoint()

  def get_cameraDirectionVectors(self):
    return self._cameraModel.get_directionVectors()

  def get_xyzPoints(self):
    return self._houseModel.get_points()

  def get_cameraProjection(self):
    return self._cameraModel.get_projectedObject()

  # GUI EVENTS #########################################################################################################
  
  def onKeyboardPressed(self, key):
    if self._currentObject == OBJECTS[0][1]:
      if key == "KP_6":
        self._objectModel.translateX(1) # Go Right (X+)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_4":
        self._objectModel.translateX(-1) # Go Left (X-)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_8":
        self._objectModel.translateY(1) # Go On (Y+)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_2":
        self._objectModel.translateY(-1) # Go Back (Y-)
        self.delegate.worldViewShouldUpdate() 
        self.__updateProjection()
      elif key == "KP_7":
        self._objectModel.translateXY("01") # Go On-Left (XY plane)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_9":
        self._objectModel.translateXY("11") # Go On-Right (XY plane)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_1":
        self._objectModel.translateXY("00") # Go Back-Left (XY plane)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_3":
        self._objectModel.translateXY("10") # Go Back-Right (XY plane)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_Add":
        self._objectModel.translateZ(1) # Go Up (Z+)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_Enter":
        self._objectModel.translateZ(-1) # Go Down (Z-)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()

    elif self._currentObject == OBJECTS[1][1]:
      if key == "KP_6":
        self._cameraModel.translateX(1) # Go Right (X+)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_4":
        self._cameraModel.translateX(-1) # Go Left (X-)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_8":
        self._cameraModel.translateY(1) # Go On (Y+)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_2":
        self._cameraModel.translateY(-1) # Go Back (Y-) 
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_7":
        self._cameraModel.translateXY("01") # Go On-Left (XY plane)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_9":
        self._cameraModel.translateXY("11") # Go On-Right (XY plane)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_1":
        self._cameraModel.translateXY("00") # Go Back-Left (XY plane)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_3":
        self._cameraModel.translateXY("10") # Go Back-Right (XY plane)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_Add":
        self._cameraModel.translateZ(1) # Go Up (Z+)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
      elif key == "KP_Enter":
        self._cameraModel.translateZ(-1) # Go Down (Z-)
        self.delegate.worldViewShouldUpdate()
        self.__updateProjection()
    return

  def selectedObjectChanged(self, currentObject):
    self._currentObject = currentObject
    return

  def xOrientationChanged(self, orientation):
    if self._currentObject == OBJECTS[0][1]:
      self._objectModel.rotateX(orientation)
    else:
      self._cameraModel.rotateX(orientation)

    self.delegate.worldViewShouldUpdate()
    self.__updateProjection()
    return

  def yOrientationChanged(self, orientation):
    if self._currentObject == OBJECTS[0][1]:
      self._objectModel.rotateY(orientation)
    else:
      self._cameraModel.rotateY(orientation)

    self.delegate.worldViewShouldUpdate()
    self.__updateProjection()
    return

  def zOrientationChanged(self, orientation):
    if self._currentObject == OBJECTS[0][1]:
      self._objectModel.rotateZ(orientation)
    else:
      self._cameraModel.rotateZ(orientation)

    self.delegate.worldViewShouldUpdate()
    self.__updateProjection()
    return

  def intrinsincParamsChanged(self, f, sx, sy, stheta, ox, oy):
    self._cameraModel.setIntrinsicParams(f,sx,sy,stheta,ox,oy) 
    self.__updateProjection()
    return

  def __updateProjection(self):
    self._cameraModel.project(self._objectModel.get_objectBody())
    self.delegate.projectionViewShouldUpdate() 
    return

  


  