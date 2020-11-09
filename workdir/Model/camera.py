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

  def get_projectedObject(self):
    return np.copy(self._projectedObject)

  # SETTERS ##########################################################################################
  
  def setIntrinsicParams(self, f, sx, sy, stheta, ox, oy):
    self._intrinsicMatrix = np.array([
                                        [f*sx, f*stheta, ox],
                                        [ 0,     f*sy,   oy],
                                        [ 0,      0,      1]
                                    ])
    return

  # PUBLIC METHODS ###################################################################################
  
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
  