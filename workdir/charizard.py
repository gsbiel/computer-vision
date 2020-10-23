from object_class import Object
import numpy as np
from stl import mesh

path_to_obj = "./3DModel/myCharizard.stl"

class Charizard(Object):

  def __init__(self):
    super().__init__(np.array([]))
    self.charizard_mesh = mesh.Mesh.from_file("./3DModel/myCharizard.stl")
    self.vectors = self.charizard_mesh.vectors

    self.x = self.charizard_mesh.x.flatten()
    self.y = self.charizard_mesh.y.flatten()
    self.z = self.charizard_mesh.z.flatten()

    self.body = np.array([self.x.T, self.y.T, self.z.T,np.ones(self.x.size)])
    return
