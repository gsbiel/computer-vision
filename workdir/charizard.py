from object_class import Object
import numpy as np
from stl import mesh

path_to_obj = "./3DModel/myCharizard.stl"

reference_point = np.array([0, 10, -5, 1])

class Charizard(Object):

  def __init__(self):
    super().__init__(np.array([]), reference_point)
    self.charizard_mesh = mesh.Mesh.from_file("./3DModel/myCharizard.stl")

    self.x = self.charizard_mesh.x.flatten()
    self.y = self.charizard_mesh.y.flatten()
    self.z = self.charizard_mesh.z.flatten()

    self.body = np.array([self.x, self.y, self.z, np.ones(self.x.size)])
    self.body = self.body.transpose()
    self.initialBody = np.copy(self.body)

    self.generate_mesh()
    return

  def translateX(self, dx=1):
    super().translateX(dx)
    self.generate_mesh()
    return
  
  def translateY(self, dy=1):
    super().translateY(dy)
    self.generate_mesh()
    return

  def translateZ(self, dz=1):
    super().translateZ(dz)
    self.generate_mesh()
    return

  def translateXY(self, code):
    super().translateXY(code)
    self.generate_mesh()
    return

  def rotateX(self, angle):
    super().rotateX(angle)
    self.generate_mesh()
    return

  def rotateY(self, angle):
    super().rotateY(angle)
    self.generate_mesh()
    return

  def rotateZ(self, angle):
    super().rotateZ(angle)
    self.generate_mesh()
    return

  def generate_mesh(self):
    print("gerando mesh")
    body_input = self.body.transpose()
    x = body_input[0]
    y = body_input[1]
    z = body_input[2]
    zip_data = list(zip(x,y,z))
    data_array = np.array(zip_data)
    reshape = data_array.reshape(1572,3,3)
    self.vectors = reshape
    return

