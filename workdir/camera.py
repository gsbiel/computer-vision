from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import numpy as np
from object_class import Object

class CameraAxis(Object):

    def __init__(self, p_0 = np.array([[0,0,0,1]]), p_1 = np.array([[1,0,0,1],[0,1,0,1],[0,0,1,1]])):
        super().__init__(p_0)
        self.p_0 = p_0
        self.p_1 = p_1
        self.translation_tracker = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        return

    def transform(self, transformation_matrix):
        super().transform(transformation_matrix)
        self.p_1 = (transformation_matrix.dot(self.p_1.transpose())).transpose()

    def rotateX(self, angle):
        self.body = np.vstack((self.p_1, self.p_0))
        super().rotateX(angle)
        self.p_0 = np.array([self.body[3,:]])
        self.p_1 = np.array([self.body[0,:], self.body[1,:], self.body[2,:]])
        self.body = self.p_0
        return

    def rotateY(self, angle):
        self.body = np.vstack((self.p_1, self.p_0))
        super().rotateY(angle)
        self.p_0 = np.array([self.body[3,:]])
        self.p_1 = np.array([self.body[0,:], self.body[1,:], self.body[2,:]])
        self.body = self.p_0
        return

    def rotateZ(self, angle):
        self.body = np.vstack((self.p_1, self.p_0))
        super().rotateZ(angle)
        self.p_0 = np.array([self.body[3,:]])
        self.p_1 = np.array([self.body[0,:], self.body[1,:], self.body[2,:]])
        self.body = self.p_0
        return




