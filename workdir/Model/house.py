from .rigidBody import RigidBodyModel
import numpy as np

class HouseModel(RigidBodyModel):
  def __init__(self):
    self._house_points = np.loadtxt('./3DModel/house.xyz')
    self._x = self._house_points[:,0]
    self._y = self._house_points[:,1]
    self._z = self._house_points[:,2]
    body = np.array([self._x, self._y, self._z, np.ones(self._x.size)],dtype='float32').transpose()
    super().__init__(body)
    super().moveInitialPositionToFirstQuadrant(12,10,0)
    return





