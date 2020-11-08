import numpy as np
from stl import mesh

from .rigidBody import RigidBodyModel

path_to_obj = "./3DModel/myCharizard.stl"

class ObjectModel(RigidBodyModel):

  def __init__(self):
    # Charizard
    self._object_mesh = mesh.Mesh.from_file("./3DModel/myCharizard.stl")

    self._x = self._object_mesh.x.flatten()
    self._y = self._object_mesh.y.flatten()
    self._z = self._object_mesh.z.flatten()

    body = np.array([self._x, self._y, self._z, np.ones(self._x.size)],dtype='float32')
    body = body.transpose()

    super().__init__(np.copy(body))

    # super().moveInitialPositionToFirstQuadrant(15,5,20)

    self._vectors = np.array([])
    self.__generate_mesh()
    return

  # GETTERS ###########################################################################################################
  def get_objectVectors(self):
    return np.copy(self._vectors)

  # PUBLIC METHODS ####################################################################################################

  def translateX(self, withRespectTo="world", dx=1):
    super().translateX(withRespectTo, dx)
    self.__generate_mesh()
    return
  
  def translateY(self, withRespectTo="world", dy=1):
    super().translateY(withRespectTo, dy)
    self.__generate_mesh()
    return

  def translateZ(self, withRespectTo="world", dz=1):
    super().translateZ(withRespectTo, dz)
    self.__generate_mesh()
    return

  def rotateX(self, withRespectTo="world", angle=0):
    super().rotateX(withRespectTo, angle)
    self.__generate_mesh()
    return

  def rotateY(self, withRespectTo="world", angle=0):
    super().rotateY(withRespectTo, angle)
    self.__generate_mesh()
    return

  def rotateZ(self, withRespectTo="world", angle=0):
    super().rotateZ(withRespectTo, angle)
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



