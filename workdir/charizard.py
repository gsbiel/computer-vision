from object_class import Object
import numpy as np
from stl import mesh

path_to_obj = "./3DModel/myCharizard.stl"

class Charizard(Object):

  def __init__(self):
    super().__init__(np.array([]))
    self.charizard_mesh = mesh.Mesh.from_file("./3DModel/myCharizard.stl")
    # self.vectors = self.charizard_mesh.vectors
    self.x = self.charizard_mesh.x.flatten()
    self.y = self.charizard_mesh.y.flatten()
    self.z = self.charizard_mesh.z.flatten()

    self.body = np.array([self.x, self.y, self.z, np.ones(self.x.size)])
    print('Body: {shape}'.format(shape = self.body.shape))
    self.body = self.body.transpose()
    # self.generate_mesh()
    return

  def generate_mesh(self):
    data = np.concatenate((self.x, self.y), axis=0)
    data = np.concatenate((data, self.z), axis=0)
    self.vectors = mesh.Mesh(data, remove_empty_areas=False)
    return
