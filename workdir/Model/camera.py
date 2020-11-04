import numpy as np
from .rigidBody import RigidBodyModel

class CameraModel(RigidBodyModel):

  # INIT ############################################################################################
  
  def __init__(self, p_0, p_1, reference_point):
    super().__init__(p_0, reference_point)
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
    self._projectedObject = np.array([])

    self.setIntrinsicParams(2,4.7,6.5,0.0,10.0,10.0)
    return

  # GETTERS #########################################################################################
  
  def get_mainPoint(self):
    return np.copy(self._p_0)
  
  def get_directionVectors(self):
    return np.copy(self._p_1)

  def get_initialBody(self):
    return np.copy(self._initialBody)

  def get_projectedObject(self):
    return np.copy(self._projectedObject)

  def get_translationTracker(self):
    return np.copy(self._translation_tracker)

  def get_intrinsicParams(self):
    return np.copy(self._intrinsicMatrix)

  def get_projectionMatrix(self):
    return np.copy(self._projection_matrix)

  # SETTERS ##########################################################################################
  
  def setIntrinsicParams(self, f, sx, sy, stheta, ox, oy):
    self._intrinsicMatrix = np.array([
                                        [f*sx, f*stheta, ox],
                                        [ 0,     f*sy,   oy],
                                        [ 0,      0,      1]
                                    ])
    return

  # PUBLIC METHODS ###################################################################################
  
  def translateX(self, dx):
    super().translateX(dx)
    self._p_0 = self._body
    return

  def translateY(self, dy):
    super().translateY(dy)
    self._p_0 = self._body
    return

  def translateZ(self, dz):
    super().translateZ(dz)
    self._p_0 = self._body
    return

  def translateXY(self, code, d=1):
    super().translateXY(code, d)
    self._p_0 = self._body
    return

  def rotateX(self, angle):
    self._body = np.copy(self._initialBody)
    self._x_orientation = angle
    rotation_matrix = super().get_rotation(self._z_orientation, angle, self._y_orientation)
    rotadedBody = rotation_matrix.dot(self._body.transpose())
    self._p_1 = rotadedBody.transpose()
    self._body = self._p_0
    return

  def rotateY(self, angle):
    self._body = np.copy(self._initialBody)
    self._y_orientation = angle
    rotation_matrix = super().get_rotation(self._z_orientation, self._x_orientation, angle)
    rotadedBody = rotation_matrix.dot(self._body.transpose())
    self._p_1 = rotadedBody.transpose()
    self._body = self._p_0
    return

  def rotateZ(self, angle):
    self._body = np.copy(self._initialBody)
    self._z_orientation = angle
    rotation_matrix = super().get_rotation(angle, self._x_orientation, self._y_orientation)
    rotadedBody = rotation_matrix.dot(self._body.transpose())
    self._p_1 = rotadedBody.transpose()
    self._body = self._p_0
    return

  def project(self, object):
    inverse_rotation = super().get_rotation(-self._z_orientation, -self._x_orientation, -self._y_orientation)
    inverse_translation = np.linalg.inv(self._translation_tracker)
    identity = np.eye(4)
    extrinsic_params_matrix = inverse_rotation.dot(inverse_translation.dot(identity))
    self._projectedObject = self._intrinsicMatrix.dot(self._projection_matrix.dot(extrinsic_params_matrix.dot(object.transpose()))).transpose()
    z_coordinates = self._projectedObject[:, -1]
    z_coordinates = z_coordinates.reshape(len(z_coordinates),1)
    z_coordinates[z_coordinates==0] = 1
    self._projectedObject = np.divide(self._projectedObject, z_coordinates)
    return 
  