import numpy as np
from math import pi, cos, sin

class Object:

    def __init__(self, body_definition, reference):

        # This property stays unchanged
        self.initialBody = np.copy(body_definition)
        self.body = np.copy(body_definition)

        self.axis_reference = reference
        ref_x = reference[0]
        ref_y= reference[1]
        ref_z = reference[2]

        # Matrix that converts coordinates from world's referential to object's referential
        self.fromWorldToObjectReferentialMatrix = np.array([
                                            [1, 0, 0, (-1)*ref_x],
                                            [0, 1, 0, (-1)*ref_y],
                                            [0, 0, 1, (-1)*ref_z],
                                            [0, 0, 0,      1    ]
                                        ])

        self.fromObjectToWorldReferentialMatrix = np.linalg.inv(self.fromWorldToObjectReferentialMatrix)

        # Keeps track of the translations suffered by the object
        self.translation_tracker = np.array([
                                                [1,0,0,0],
                                                [0,1,0,0],
                                                [0,0,1,0],
                                                [0,0,0,1]
                                            ])

        self.x_orientation = 0
        self.y_orientation = 0
        self.z_orientation = 0

        return

    def translateX(self, dx=1):
        translation_matrix = np.array([[1,0,0,dx], [0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        self.trackTranslation(translation_matrix)
        return

    def translateY(self, dy=1):
        translation_matrix = np.array([[1,0,0,0], [0,1,0,dy],[0,0,1,0],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()
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
        # Abordagem corpo imutável na origem
        self.body = np.copy(self.initialBody)
        self.changeCoordinatesToReferentialInObject()
        self.x_orientation = angle
        rotation_matrix = self.get_rotation(self.z_orientation, angle, self.y_orientation)
        rotadedBody = rotation_matrix.dot(self.body.transpose())
        translatedBody = self.translation_tracker.dot(rotadedBody).transpose()
        self.body = translatedBody
        self.changeCoordinatesToReferentialInWorld()
        return

    def rotateY(self, angle):
        # Abordagem corpo imutável na origem
        self.body = np.copy(self.initialBody)
        self.changeCoordinatesToReferentialInObject()
        self.y_orientation = angle
        rotation_matrix = self.get_rotation(self.z_orientation, self.x_orientation, angle)
        rotadedBody = rotation_matrix.dot(self.body.transpose())
        translatedBody = self.translation_tracker.dot(rotadedBody).transpose()
        self.body = translatedBody
        self.changeCoordinatesToReferentialInWorld()
        return

    def rotateZ(self, angle):
        # Abordagem corpo imutável na origem
        self.body = np.copy(self.initialBody)
        self.changeCoordinatesToReferentialInObject()
        self.z_orientation = angle
        rotation_matrix = self.get_rotation(angle, self.x_orientation, self.y_orientation)
        rotadedBody = rotation_matrix.dot(self.body.transpose())
        translatedBody = self.translation_tracker.dot(rotadedBody).transpose()
        self.body = translatedBody
        self.changeCoordinatesToReferentialInWorld()
        return

    def changeCoordinatesToReferentialInObject(self):
        self.body = self.fromWorldToObjectReferentialMatrix.dot(self.initialBody.transpose()).transpose()
        return

    def changeCoordinatesToReferentialInWorld(self):
        self.body = self.fromObjectToWorldReferentialMatrix.dot(self.body.transpose()).transpose()
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
        self.fromWorldToObjectReferentialMatrix = np.linalg.inv(translation_matrix).dot(self.fromWorldToObjectReferentialMatrix)
        self.fromObjectToWorldReferentialMatrix = np.linalg.inv(self.fromWorldToObjectReferentialMatrix)
        return


