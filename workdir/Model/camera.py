import numpy as np
from .rigidBody import RigidBodyModel

class CameraModel(RigidBodyModel):

  # INIT ######################################################################
  def __init__(self, p_0, p_1):
    self._p_0 = p_0
    self._p_1 = p_1
    self._initialBody = np.copy(p_1)
    self._translation_tracker = np.eye(4)
    self._intrinsicMatrix = np.array([])
    self._projection_matrix = np.array([
                                    [1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,1,0]
                                ])
    return

  # GETTERS ###################################################################
  def get_mainPoint(self):
    return self._p_0
  
  def get_directionVectors(self):
    return self._p_1

  def get_initialBody(self):
    return self._initialBody

  def get_translationTracker(self):
    return self._translation_tracker

  def get_intrinsicParams(self):
    return self._intrinsicMatrix

  def get_projectionMatrix(self):
    return self._projection_matrix

  # SETTERS ####################################################################

  