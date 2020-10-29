
import numpy as np
from math import pi, cos, sin

class RigidBodyModel:

  def __init__(self, body_definition, reference):

    # This property stays unchanged
    self._initialBody = np.copy(body_definition)
    self._body = np.copy(body_definition)

    self._axis_reference = reference
    self._ref_x = reference[0]
    self._ref_y= reference[1]
    self._ref_z = reference[2]

    # Matrix that converts coordinates from world's referential to object's referential
    self._fromWorldToObjectReferentialMatrix = np.array([
                                        [1, 0, 0, (-1)*self._ref_x],
                                        [0, 1, 0, (-1)*self._ref_y],
                                        [0, 0, 1, (-1)*self._ref_z],
                                        [0, 0, 0,         1        ]
                                    ])

    self._fromObjectToWorldReferentialMatrix = np.linalg.inv(self._fromWorldToObjectReferentialMatrix)

    # Keeps track of the translations suffered by the object
    self._translation_tracker = np.array([
                                            [1,0,0,0],
                                            [0,1,0,0],
                                            [0,0,1,0],
                                            [0,0,0,1]
                                        ])

    self._x_orientation = 0
    self._y_orientation = 0
    self._z_orientation = 0

    return

  # PUBLIC METHODS #####################################################################################################
  def translateX(self, dx=1):
    translation_matrix = np.array([[1,0,0,dx], [0,1,0,0],[0,0,1,0],[0,0,0,1]])
    self._body = (translation_matrix.dot(self._body.transpose())).transpose()
    self.__trackTranslation(translation_matrix)
    return

  def translateY(self, dy=1):
    translation_matrix = np.array([[1,0,0,0], [0,1,0,dy],[0,0,1,0],[0,0,0,1]])
    self._body = (translation_matrix.dot(self._body.transpose())).transpose()
    self.__trackTranslation(translation_matrix)    
    return

  def translateZ(self, dz=1):
    translation_matrix = np.array([[1,0,0,0], [0,1,0,0],[0,0,1,dz],[0,0,0,1]])
    self._body = (translation_matrix.dot(self._body.transpose())).transpose()    
    self.__trackTranslation(translation_matrix)    
    return

  def translateXY(self, code, d=1):
    if code == "00":
        translation_matrix = np.array([[1,0,0,-1*d], [0,1,0,-1*d],[0,0,1,0],[0,0,0,1]])
        self._body = (translation_matrix.dot(self._body.transpose())).transpose()
        self.__trackTranslation(translation_matrix)
    elif code == "01":
        translation_matrix = np.array([[1,0,0,-1*d], [0,1,0,d],[0,0,1,0],[0,0,0,1]])
        self._body = (translation_matrix.dot(self._body.transpose())).transpose()
        self.__trackTranslation(translation_matrix)
    elif code == "10":
        translation_matrix = np.array([[1,0,0,d], [0,1,0,-1*d],[0,0,1,0],[0,0,0,1]])
        self._body = (translation_matrix.dot(self._body.transpose())).transpose()
        self.__trackTranslation(translation_matrix)
    elif code == "11":
        translation_matrix = np.array([[1,0,0,d], [0,1,0,d],[0,0,1,0],[0,0,0,1]])
        self._body = (translation_matrix.dot(self._body.transpose())).transpose()
        self.__trackTranslation(translation_matrix)
    return

  def rotateX(self, angle):
    # Abordagem corpo imutável na origem
    self._body = np.copy(self._initialBody)
    self.__changeCoordinatesToReferentialInObject()
    self._x_orientation = angle
    rotation_matrix = self.get_rotation(self._z_orientation, angle, self._y_orientation)
    rotadedBody = rotation_matrix.dot(self._body.transpose())
    translatedBody = self._translation_tracker.dot(rotadedBody).transpose()
    self._body = translatedBody
    self.__changeCoordinatesToReferentialInWorld()
    return

  def rotateY(self, angle):
    # Abordagem corpo imutável na origem
    self._body = np.copy(self._initialBody)
    self.__changeCoordinatesToReferentialInObject()
    self._y_orientation = angle
    rotation_matrix = self.get_rotation(self._z_orientation, self._x_orientation, angle)
    rotadedBody = rotation_matrix.dot(self._body.transpose())
    translatedBody = self._translation_tracker.dot(rotadedBody).transpose()
    self._body = translatedBody
    self.__changeCoordinatesToReferentialInWorld()
    return

  def rotateZ(self, angle):
    # Abordagem corpo imutável na origem
    self._body = np.copy(self._initialBody)
    self.__changeCoordinatesToReferentialInObject()
    self._z_orientation = angle
    rotation_matrix = self.get_rotation(angle, self._x_orientation, self._y_orientation)
    rotadedBody = rotation_matrix.dot(self._body.transpose())
    translatedBody = self._translation_tracker.dot(rotadedBody).transpose()
    self._body = translatedBody
    self.__changeCoordinatesToReferentialInWorld()
    return

  # PRIVATE METHODS ####################################################################################################

  def __changeCoordinatesToReferentialInObject(self):
    self._body = self._fromWorldToObjectReferentialMatrix.dot(self._initialBody.transpose()).transpose()
    return

  def __changeCoordinatesToReferentialInWorld(self):
    self._body = self._fromObjectToWorldReferentialMatrix.dot(self._body.transpose()).transpose()
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

  def __trackTranslation(self, translation_matrix):
    self._translation_tracker = translation_matrix.dot(self._translation_tracker)
    self._fromWorldToObjectReferentialMatrix = np.linalg.inv(translation_matrix).dot(self._fromWorldToObjectReferentialMatrix)
    self._fromObjectToWorldReferentialMatrix = np.linalg.inv(self._fromWorldToObjectReferentialMatrix)
    return


