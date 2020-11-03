from .rigidBody import RigidBodyModel
import numpy as np

class HouseModel(RigidBodyModel):
  def __init__(self):
    self._house_points = np.loadtxt('./3DModel/house.xyz')
    self._x = self._house_points[:,0]
    self._y = self._house_points[:,1]
    self._z = self._house_points[:,2]
    body = np.array([self._x, self._y, self._z, np.ones(self._x.size)]).transpose()
    reference_point = self.__find_central_point(body)
    super().__init__(body, reference_point)
    super().moveInitialPositionToFirstQuadrant(12,10,0)
    return

  def get_points(self):
    return np.copy(self._body)

  def __find_central_point(self, obj):
    x_central = (max(obj[0,:]) + min(obj[0,:]))/2
    y_central = (max(obj[1,:]) + min(obj[1,:]))/2
    z_central = (max(obj[2,:]) + min(obj[2,:]))/2
    central_point = np.array([x_central,y_central,z_central,1]) 
    return central_point

