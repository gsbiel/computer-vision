import numpy as np
from stl import mesh

from .rigidBody import RigidBodyModel

path_to_obj = "./3DModel/myCharizard.stl"

class ObjectModel(RigidBodyModel):

  def __init__(self, reference_point=np.array([0,0,0,1])):
    super().__init__(np.array([]), reference_point)

    # Charizard
    self._object_mesh = mesh.Mesh.from_file("./3DModel/myCharizard.stl")

    self._x = self._object_mesh.x.flatten()
    self._y = self._object_mesh.y.flatten()
    self._z = self._object_mesh.z.flatten()

    self._body = np.array([self._x, self._y, self._z, np.ones(self._x.size)])
    self._body = self._body.transpose()
    self._initialBody = np.copy(self._body)

    super().moveInitialPositionToFirstQuadrant(15,5,20)

    self._vectors = np.array([])
    self.__generate_mesh()
    return

  # GETTERS ###########################################################################################################
  def get_objectVectors(self):
    return np.copy(self._vectors)

  def get_objectBody(self):
    return np.copy(self._body)

  # PUBLIC METHODS ####################################################################################################

  def translateX(self, dx=1):
    super().translateX(dx)
    self.__generate_mesh()
    return
  
  def translateY(self, dy=1):
    super().translateY(dy)
    self.__generate_mesh()
    return

  def translateZ(self, dz=1):
    super().translateZ(dz)
    self.__generate_mesh()
    return

  def translateXY(self, code):
    super().translateXY(code)
    self.__generate_mesh()
    return

  def rotateX(self, angle):
    super().rotateX(angle)
    self.__generate_mesh()
    return

  def rotateY(self, angle):
    super().rotateY(angle)
    self.__generate_mesh()
    return

  def rotateZ(self, angle):
    super().rotateZ(angle)
    self.__generate_mesh()
    return

  # PRIVATE METHODS ####################################################################################################

  def __generate_mesh(self):
    body_input = self._body.transpose()
    x = body_input[0]
    y = body_input[1]
    z = body_input[2]
    zip_data = list(zip(x,y,z))
    data_array = np.array(zip_data)
    reshape = data_array.reshape(1572,3,3)
    self._vectors = reshape
    return



