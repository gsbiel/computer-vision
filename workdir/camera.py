from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import numpy as np
from object_class import Object

reference_point = np.array([12,-20,0,1])
class CameraAxis(Object):

    def __init__(self, p_0 = np.array([reference_point]), p_1 = np.array([[1,0,0,1],[0,1,0,1],[0,0,1,1]])):
        super().__init__(p_0, reference_point)
        self.p_0 = p_0
        self.p_1 = p_1
        self.initialBody = np.copy(p_1)

        self.translation_tracker = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.intrinsicMatrix = np.array([])
        self.projectionMatrix = np.array([])
        self.extrinsicMatrix = np.array([])
        return

    def transform(self, transformation_matrix):
        super().transform(transformation_matrix)
        self.p_1 = (transformation_matrix.dot(self.p_1.transpose())).transpose()

    def translateX(self, dx):
        super().translateX(dx)
        self.p_0 = self.body
        return

    def translateY(self, dy):
        super().translateY(dy)
        self.p_0 = self.body
        return

    def translateZ(self, dz):
        super().translateZ(dz)
        self.p_0 = self.body
        return

    def translateXY(self, code, d=1):
        super().translateXY(code, d)
        self.p_0 = self.body
        return

    def rotateX(self, angle):
        self.body = np.copy(self.initialBody)
        self.x_orientation = angle
        rotation_matrix = super().get_rotation(self.z_orientation, angle, self.y_orientation)
        rotadedBody = rotation_matrix.dot(self.body.transpose())
        self.p_1 = rotadedBody.transpose()
        self.body = self.p_0
        return

    def rotateY(self, angle):
        self.body = np.copy(self.initialBody)
        self.y_orientation = angle
        rotation_matrix = super().get_rotation(self.z_orientation, self.x_orientation, angle)
        rotadedBody = rotation_matrix.dot(self.body.transpose())
        self.p_1 = rotadedBody.transpose()
        self.body = self.p_0
        return

    def rotateZ(self, angle):
        self.body = np.copy(self.initialBody)
        self.z_orientation = angle
        rotation_matrix = super().get_rotation(angle, self.x_orientation, self.y_orientation)
        rotadedBody = rotation_matrix.dot(self.body.transpose())
        self.p_1 = rotadedBody.transpose()
        self.body = self.p_0
        return




