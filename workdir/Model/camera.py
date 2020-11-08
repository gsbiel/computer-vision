import numpy as np
from .rigidBody import RigidBodyModel

class CameraModel(RigidBodyModel):

  # INIT ############################################################################################
  
  def __init__(self, p_0):
    super().__init__(p_0)
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
  
  # def get_initialBody(self):
  #   return np.copy(self._initialBody)

  def get_projectedObject(self):
    return np.copy(self._projectedObject)

  # def get_translationTracker(self):
  #   return np.copy(self._translation_tracker)

  # def get_intrinsicParams(self):
  #   return np.copy(self._intrinsicMatrix)

  # def get_projectionMatrix(self):
  #   return np.copy(self._projection_matrix)

  # SETTERS ##########################################################################################
  
  def setIntrinsicParams(self, f, sx, sy, stheta, ox, oy):
    self._intrinsicMatrix = np.array([
                                        [f*sx, f*stheta, ox],
                                        [ 0,     f*sy,   oy],
                                        [ 0,      0,      1]
                                    ])
    return

  # PUBLIC METHODS ###################################################################################
  
  # def translateX(self, withRespectTo="world", dx):
  #   super().translateX(withRespectTo, dx)
  #   return

  # def translateY(self, withRespectTo="world", dy):
  #   super().translateY(withRespectTo, dy)
  #   return

  # def translateZ(self, withRespectTo="world", dz):
  #   super().translateZ(withRespectTo, dz)
  #   return

  # def rotateX(self, withRespectTo="world", angle):
  #   self._body = np.copy(self._initialBody)
  #   self._x_orientation = angle
  #   rotation_matrix = super().get_rotation(self._z_orientation, angle, self._y_orientation)
  #   rotadedBody = rotation_matrix.dot(self._body.transpose())
  #   self._p_1 = rotadedBody.transpose()
  #   self._body = self._p_0
  #   return

  # def rotateY(self, withRespectTo="world", angle):
  #   self._body = np.copy(self._initialBody)
  #   self._y_orientation = angle
  #   rotation_matrix = super().get_rotation(self._z_orientation, self._x_orientation, angle)
  #   rotadedBody = rotation_matrix.dot(self._body.transpose())
  #   self._p_1 = rotadedBody.transpose()
  #   self._body = self._p_0
  #   return

  # def rotateZ(self, withRespectTo="world", angle):
  #   self._body = np.copy(self._initialBody)
  #   self._z_orientation = angle
  #   rotation_matrix = super().get_rotation(angle, self._x_orientation, self._y_orientation)
  #   rotadedBody = rotation_matrix.dot(self._body.transpose())
  #   self._p_1 = rotadedBody.transpose()
  #   self._body = self._p_0
  #   return

  def project(self, object):
    inverse_rotation = self._objBase.transpose() # transposta = inversa
    inverse_rotation = np.vstack([inverse_rotation,np.array([0,0,0,1])])
    inverse_translation = super().get_translation(
      -self._objRefPoint[0],
      -self._objRefPoint[1],
      -self._objRefPoint[2]
    )
    extrinsic_params_matrix = inverse_translation.dot(inverse_rotation)
    self._projectedObject = self._intrinsicMatrix.dot(
                              self._projection_matrix.dot(
                                extrinsic_params_matrix.dot(
                                  object.transpose()
                                )
                              )
                            ).transpose()
    z_coordinates = self._projectedObject[:, -1]
    z_coordinates = z_coordinates.reshape(len(z_coordinates),1)
    z_coordinates[z_coordinates==0] = 1
    self._projectedObject = np.divide(self._projectedObject, z_coordinates)
    return 
  