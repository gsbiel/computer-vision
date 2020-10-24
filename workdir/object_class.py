import numpy as np
from math import pi, cos, sin

class Object:

    def __init__(self, body_definition):
        self.body = body_definition

        # Keeps track of the transformations suffered by the object
        self.transformations_tracker = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.translation_tracker = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.rotation_tracker = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

        self.x_orientation = 0
        self.y_orientation = 0
        self.z_orientation = 0

        return

    def translateX(self, dx=1):
        translation_matrix = np.array([[1,0,0,dx], [0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        # print(self.body)
        self.trackTranslation(translation_matrix)
        return

    def translateY(self, dy=1):
        translation_matrix = np.array([[1,0,0,0], [0,1,0,dy],[0,0,1,0],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        # print(self.body)
        self.trackTranslation(translation_matrix)    
        return

    def translateZ(self, dz=1):
        translation_matrix = np.array([[1,0,0,0], [0,1,0,0],[0,0,1,dz],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()    
        self.trackTranslation(translation_matrix)    
        return

    def translateXY(self, code, d=1):
        if code == "00":
            translation_matrix = np.array([[1,0,0,-1*d], [0,1,0,-1*d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.trackTranslation(translation_matrix)
        elif code == "01":
            translation_matrix = np.array([[1,0,0,-1*d], [0,1,0,d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.trackTranslation(translation_matrix)
        elif code == "10":
            translation_matrix = np.array([[1,0,0,d], [0,1,0,-1*d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.trackTranslation(translation_matrix)
        elif code == "11":
            translation_matrix = np.array([[1,0,0,d], [0,1,0,d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.trackTranslation(translation_matrix)
        return

    def rotateX(self, angle):
        self.moveBackToInitialPosition()
        self.x_orientation = angle
        rotation_matrix = self.get_rotation(self.z_orientation, angle, self.y_orientation)
        rotadedBody = rotation_matrix.dot(self.body.transpose())
        translatedBody = self.translation_tracker.dot(rotadedBody).transpose()
        self.body = translatedBody
        self.trackRotation(rotation_matrix)
        return

    def rotateY(self, angle):
        self.moveBackToInitialPosition()
        self.y_orientation = angle
        rotation_matrix = self.get_rotation(self.z_orientation, self.x_orientation, angle)
        rotadedBody = rotation_matrix.dot(self.body.transpose())
        translatedBody = self.translation_tracker.dot(rotadedBody).transpose()
        self.body = translatedBody
        self.trackRotation(rotation_matrix)
        return

    def rotateZ(self, angle):
        self.moveBackToInitialPosition()
        self.z_orientation = angle
        rotation_matrix = self.get_rotation(angle, self.x_orientation, self.y_orientation)
        rotadedBody = rotation_matrix.dot(self.body.transpose())
        translatedBody = self.translation_tracker.dot(rotadedBody).transpose()
        self.body = translatedBody
        self.trackRotation(rotation_matrix)
        return

    def moveBackToInitialPosition(self):
        self.translateBackToInitialPosition()
        self.rotateBackToInitialPosition()
        return

    def translateBackToInitialPosition(self):
        transformation =  np.linalg.inv(self.translation_tracker)
        self.body = transformation.dot(self.body.transpose()).transpose()
        return

    def rotateBackToInitialPosition(self):
        rotation_matrix = self.get_rotation(-self.z_orientation, -self.x_orientation, -self.y_orientation)
        self.body = rotation_matrix.dot(self.body.transpose()).transpose()
        return

    def get_rotation(self, theta_degree, phi_degree, alpha_degree):
        theta = (theta_degree * pi)/180.0
        phi = (phi_degree * pi)/180.0
        alfa = (alpha_degree * pi)/180.0
        #Z
        rot = [
            [cos(theta), -sin(theta),  0,0],
            [sin(theta), cos(theta),   0,0],
            [    0,          0,        1,0],
            [    0,          0,        0,1]]

        #X
        rot = np.dot(rot,
                    [[1,    0,        0,     0],
                    [0, cos(phi),-sin(phi), 0],
                    [0, sin(phi), cos(phi), 0],
                    [0,    0,        0,     1]])
        #Y
        rot = np.dot(rot,
                    [[cos(alfa),   0, sin(alfa), 0],
                    [    0,       1,    0,      0],
                    [-sin(alfa),  0, cos(alfa), 0],
                    [    0,       0,    0,      1]])
        return rot

    def trackTranslation(self, translation_matrix):
        self.translation_tracker = translation_matrix.dot(self.translation_tracker)
        return

    def trackRotation(self, rotation_matrix):
        self.rotation_tracker = rotation_matrix
        return

