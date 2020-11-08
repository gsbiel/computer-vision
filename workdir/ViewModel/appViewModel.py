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
    self._currentReferenceIn = "world"
    self._cameraModel = CameraModel(np.array([referenceInCamera]))
    # self._objectModel = ObjectModel()
    self._houseModel = HouseModel()
    return

  # GETTERS ############################################################################################################
  def get_objectMesh(self):
    # return self._objectModel.get_objectVectors()
    return

  def get_cameraMainPoint(self):
    return self._cameraModel.get_referencePoint()

  def get_cameraDirectionVectors(self):
    return self._cameraModel.get_objBase()

  def get_xyzPoints(self):
    return self._houseModel.get_objBody()

  def get_cameraProjection(self):
    return self._cameraModel.get_projectedObject()

  # METHODS #########################################################################################################
  
  def refreshDisplays(self):
    self.delegate.referencesViewShouldUpdate(
                                              self._houseModel.get_referencePoint(),
                                              self._cameraModel.get_referencePoint()
                                            )
    return

  # GUI EVENTS #########################################################################################################
  
  def onKeyboardPressed(self, key):
    if self._currentObject == OBJECTS[0][1]:
      if key == "KP_6":
        # self._objectModel.translateX(self._currentReferenceIn, 1) # Go Right (X+)
        self._houseModel.translateX(self._currentReferenceIn, 1)
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()
      elif key == "KP_4":
        # self._objectModel.translateX(self._currentReferenceIn, -1) # Go Left (X-)
        self._houseModel.translateX(self._currentReferenceIn, -1)
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()
      elif key == "KP_8":
        # self._objectModel.translateY(self._currentReferenceIn, 1) # Go On (Y+)
        self._houseModel.translateY(self._currentReferenceIn, 1)
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()
      elif key == "KP_2":
        # self._objectModel.translateY(self._currentReferenceIn, -1) # Go Back (Y-)
        self._houseModel.translateY(self._currentReferenceIn, -1)
        self.delegate.worldViewShouldUpdate() 
        self.refreshDisplays()
        self.updateProjection()
      elif key == "KP_Add":
        # self._objectModel.translateZ(self._currentReferenceIn, 1) # Go Up (Z+)
        self._houseModel.translateZ(self._currentReferenceIn, 1)
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()
      elif key == "KP_Enter":
        # self._objectModel.translateZ(self._currentReferenceIn, -1) # Go Down (Z-)
        self._houseModel.translateZ(self._currentReferenceIn, -1)
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()

    elif self._currentObject == OBJECTS[1][1]:
      if key == "KP_6":
        self._cameraModel.translateX(self._currentReferenceIn, 1) # Go Right (X+)
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()
      elif key == "KP_4":
        self._cameraModel.translateX(self._currentReferenceIn, -1) # Go Left (X-)
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()
      elif key == "KP_8":
        self._cameraModel.translateY(self._currentReferenceIn, 1) # Go On (Y+)
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()
      elif key == "KP_2":
        self._cameraModel.translateY(self._currentReferenceIn, -1) # Go Back (Y-) 
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()
      elif key == "KP_Add":
        self._cameraModel.translateZ(self._currentReferenceIn, 1) # Go Up (Z+)
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()
      elif key == "KP_Enter":
        self._cameraModel.translateZ(self._currentReferenceIn, -1) # Go Down (Z-)
        self.delegate.worldViewShouldUpdate()
        self.refreshDisplays()
        self.updateProjection()
    return

  def selectedObjectChanged(self, currentObject):
    self._currentObject = currentObject
    return

  def selectedReferenceChanged(self, currentReference):
    self._currentReferenceIn = currentReference
    return

  def xOrientationChanged(self, orientation):
    if self._currentObject == OBJECTS[0][1]:
      # self._objectModel.rotateX(self._currentReferenceIn, orientation)
      self._houseModel.rotateX(self._currentReferenceIn, orientation)
    else:
      self._cameraModel.rotateX(self._currentReferenceIn, orientation)

    self.delegate.worldViewShouldUpdate()
    self.updateProjection()
    self.refreshDisplays()
    return

  def yOrientationChanged(self, orientation):
    if self._currentObject == OBJECTS[0][1]:
      # self._objectModel.rotateY(self._currentReferenceIn, orientation)
      self._houseModel.rotateY(self._currentReferenceIn, orientation)
    else:
      self._cameraModel.rotateY(self._currentReferenceIn, orientation)

    self.delegate.worldViewShouldUpdate()
    self.updateProjection()
    self.refreshDisplays()
    return

  def zOrientationChanged(self, orientation):
    if self._currentObject == OBJECTS[0][1]:
      # self._objectModel.rotateZ(self._currentReferenceIn, orientation)
      self._houseModel.rotateZ(self._currentReferenceIn, orientation)
    else:
      self._cameraModel.rotateZ(self._currentReferenceIn, orientation)

    self.delegate.worldViewShouldUpdate()
    self.updateProjection()
    self.refreshDisplays()
    return

  def intrinsincParamsChanged(self, f, sx, sy, stheta, ox, oy):
    self._cameraModel.setIntrinsicParams(f,sx,sy,stheta,ox,oy) 
    self.updateProjection()
    return

  def updateProjection(self):
    # self._cameraModel.project(self._objectModel.get_objectBody())
    self._cameraModel.project(self._houseModel.get_objBody())
    self.delegate.projectionViewShouldUpdate() 
    return

  


  