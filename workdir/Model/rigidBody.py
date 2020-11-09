
import numpy as np
from math import pi, cos, sin

class RigidBodyModel:

  def __init__(self, body_definition):

    self._body = np.copy(body_definition)
    self._objRefPoint = self.__findCentraPoint(self._body)
    self._objBase = np.array([
                              [1.0, 0.0, 0.0],
                              [0.0, 1.0, 0.0],
                              [0.0, 0.0, 1.0],
                              [0.0, 0.0, 0.0],
                            ],dtype='float64')

    self._x_orientation_world = 0.0
    self._y_orientation_world = 0.0
    self._z_orientation_world = 0.0

    self._x_orientation_obj = 0.0
    self._y_orientation_obj = 0.0
    self._z_orientation_obj = 0.0

    return

  # GETTERS #####################################################################################################
  def get_referencePoint(self):
    return np.copy(self._objRefPoint)
  
  def get_objBase(self):
    return np.copy(self._objBase)
  
  def get_objBody(self):
    return np.copy(self._body)

  # PUBLIC METHODS #####################################################################################################
  def translateX(self, withRespectTo="WORLD", dx=1.0):
    translation_matrix = self.get_translation(dx,0.0,0.0)
    self.__transform(translation_matrix, withRespectTo)
    return

  def translateY(self, withRespectTo="WORLD", dy=1.0):
    translation_matrix = self.get_translation(0.0,dy,0.0)
    self.__transform(translation_matrix, withRespectTo)
    return

  def translateZ(self, withRespectTo="WORLD", dz=1.0):
    translation_matrix = self.get_translation(0.0,0.0,dz)
    self.__transform(translation_matrix, withRespectTo)
    return

  def rotateX(self, withRespectTo="WORLD", angle=0.0):
    dteta = 0.0
    if withRespectTo == "WORLD":
      dteta = angle - self._x_orientation_world 
      self._x_orientation_world = angle
    else:
      dteta = angle - self._x_orientation_obj 
      self._x_orientation_obj = angle
    rotation_matrix = self.get_rotation(0.0, dteta, 0.0)
    self.__transform(rotation_matrix, withRespectTo)
    return

  def rotateY(self, withRespectTo="WORLD", angle=0.0):
    dteta = 0.0
    if withRespectTo == "WORLD":
      dteta = angle - self._y_orientation_world 
      self._y_orientation_world = angle
    else:
      dteta = angle - self._y_orientation_obj 
      self._y_orientation_obj = angle
    rotation_matrix = self.get_rotation(0.0, 0.0, dteta)
    self.__transform(rotation_matrix, withRespectTo)
    return

  def rotateZ(self, withRespectTo="WORLD", angle=0.0):
    dteta = 0.0
    if withRespectTo == "WORLD":
      dteta = angle - self._z_orientation_world 
      self._z_orientation_world = angle
    else:
      dteta = angle - self._z_orientation_obj 
      self._z_orientation_obj = angle
    rotation_matrix = self.get_rotation(dteta, 0.0, 0.0)
    self.__transform(rotation_matrix, withRespectTo)
    return

  def get_translation(self, dx=0, dy=0, dz=0):
    return np.array([
                      [1.0, 0.0, 0.0,  dx],
                      [0.0, 1.0, 0.0,  dy],
                      [0.0, 0.0, 1.0,  dz],
                      [0.0, 0.0, 0.0, 1.0]
                    ], dtype='float64')

  def get_rotation(self, theta_degree, phi_degree, alpha_degree):
    theta = (theta_degree * pi)/180.0
    phi = (phi_degree * pi)/180.0
    alfa = (alpha_degree * pi)/180.0
    #Z
    rot = np.array([
        [cos(theta), -sin(theta),  0.0,0.0],
        [sin(theta), cos(theta),   0.0,0.0],
        [    0.0,          0.0,    1.0,0.0],
        [    0.0,          0.0,    0.0,1.0]],dtype='float64')

    #X
    rot = np.dot(rot, 
                  np.array( [[1.0,    0.0,     0.0,     0.0],
                            [ 0.0, cos(phi),-sin(phi),  0.0],
                            [ 0.0, sin(phi), cos(phi),  0.0],
                            [ 0.0,    0.0,     0.0,     1.0]],dtype='float64'))
    #Y
    rot = np.dot(rot,
                  np.array( [[cos(alfa),   0.0, sin(alfa), 0.0],
                            [    0.0,      1.0,    0.0,    0.0],
                            [-sin(alfa),   0.0, cos(alfa), 0.0],
                            [    0.0,      0.0,    0.0,    1.0]],dtype='float64'))
    return rot

  def moveInitialPositionToFirstQuadrant(self, dx,dy,dz):
    translation_matrix = self.get_translation(dx, dy, dz)
    self._body = translation_matrix.dot(self._body.transpose()).transpose()
    self._objRefPoint = self.__findCentraPoint(self._body)
    print(self._objRefPoint)
    return

  # PRIVATE METHODS ####################################################################################################

  def __transform(self, transformation, withRespectTo):
    if withRespectTo == "SELECTED_OBJECT":
      transform = self.__changeCoordinatesToReferentialInWorld().dot(
        transformation.dot(
          self.__changeCoordinatesToReferentialInObject()
        )
      )
      self._body = transform.dot(self._body.transpose()).transpose()
      self._objBase = transformation.dot(self._objBase)   
      self._objRefPoint = transform.dot(self._objRefPoint)
    else:
      self._body = (transformation.dot(self._body.transpose())).transpose()
      self._objBase = transformation.dot(self._objBase) 
      self._objRefPoint = transformation.dot(self._objRefPoint)

    # self._objRefPoint = self.__findCentraPoint(self._body)
    # print('Saindo de transform, objRefPoint:{ref}'.format(ref=self._objRefPoint))
    return

  def __changeCoordinatesToReferentialInObject(self):
    undoRotations = self._objBase.transpose()
    undoRotations = np.vstack([undoRotations,np.array([0,0,0,1])])
    undoTranslations = self.get_translation(
                                        -self._objRefPoint[0], #dx
                                        -self._objRefPoint[1], #dy
                                        -self._objRefPoint[2]) #dz
    return undoRotations.dot(undoTranslations)                             

  def __changeCoordinatesToReferentialInWorld(self):
    restoreRotations = np.copy(self._objBase)
    restoreRotations = np.c_[restoreRotations,np.array([0,0,0,1])]
    restoreTranslations = self.get_translation(
                                          self._objRefPoint[0], #dx
                                          self._objRefPoint[1], #dy
                                          self._objRefPoint[2]) #dz
    return restoreTranslations.dot(restoreRotations)

  def __findCentraPoint(self, obj):
      obj = obj.transpose()
      if obj.shape[0] > 1:
        """
        Se haver mais de 1 linha, trata-se de um objeto 3D
        """
        x_central = (max(obj[0,:]) + min(obj[0,:]))/2.0
        y_central = (max(obj[1,:]) + min(obj[1,:]))/2.0
        z_central = (max(obj[2,:]) + min(obj[2,:]))/2.0
        central_point = np.array([x_central,y_central,z_central,1.0]) 
        return central_point
      else:
        """
        Se haver apenas 1 linha, trata-se da câmera, que consiste de apenas 1 ponto
        """
        x_central = obj[0][0]
        y_central = obj[0][1]
        z_central = obj[0][2]
        central_point = np.array([x_central,y_central,z_central,1.0]) 
        return central_point
