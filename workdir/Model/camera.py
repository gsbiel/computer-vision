import numpy as np
from .rigidBody import RigidBodyModel

CAMERA_PARAMS = {
  "f": 30,
  "sx":6.9,
  "sy":5.1,
  "s_theta":0.0,
  "ox":310,
  "oy":410
}

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

    self.setIntrinsicParams(
                              CAMERA_PARAMS["f"],
                              CAMERA_PARAMS["sx"],
                              CAMERA_PARAMS["sy"],
                              CAMERA_PARAMS["s_theta"],
                              CAMERA_PARAMS["ox"],
                              CAMERA_PARAMS["oy"]
                            )
    return

  # GETTERS #########################################################################################

  def get_projectedObject(self):
    return np.copy(self._projectedObject)

  def get_intrinsicParams(self):
    return {
      "f": self._f,
      "sx": self._sx,
      "sy": self._sy,
      "stheta": self._stheta,
      "ox": self._ox,
      "oy": self._oy
    }
    
  # SETTERS ##########################################################################################
  
  def setIntrinsicParams(self, f, sx, sy, stheta, ox, oy):
    self._f = f
    self._sx = sx
    self._sy = sy
    self._stheta = stheta
    self._ox = ox
    self._oy = oy
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
  