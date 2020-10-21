import numpy as np
from math import pi, cos, sin

class Object:

    def __init__(self, body_definition):
        self.body = body_definition

        # Keeps track of the transformations suffered by the object
        self.transformations_tracker = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        return

    def translateX(self, dx=1):
        translation_matrix = np.array([[1,0,0,dx], [0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        # print(self.body)
        self.track_transformation(translation_matrix)
        return

    def translateY(self, dy=1):
        translation_matrix = np.array([[1,0,0,0], [0,1,0,dy],[0,0,1,0],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        # print(self.body)
        self.track_transformation(translation_matrix)     
        return

    def translateZ(self, dz=1):
        translation_matrix = np.array([[1,0,0,0], [0,1,0,0],[0,0,1,dz],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()  
        self.track_transformation(translation_matrix)      
        return

    def translateXY(self, code, d=1):
        if code == "00":
            translation_matrix = np.array([[1,0,0,-1*d], [0,1,0,-1*d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.track_transformation(translation_matrix)
        elif code == "01":
            translation_matrix = np.array([[1,0,0,-1*d], [0,1,0,d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.track_transformation(translation_matrix)
        elif code == "10":
            translation_matrix = np.array([[1,0,0,d], [0,1,0,-1*d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.track_transformation(translation_matrix)
        elif code == "11":
            translation_matrix = np.array([[1,0,0,d], [0,1,0,d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.track_transformation(translation_matrix)
        return

    def transform(self, transformation_matrix):
        self.body = (transformation_matrix.dot(self.body.transpose())).transpose()
        return

    def rotateX(self, angle):
        backToOriginTransformation = np.linalg.inv(self.transformations_tracker)
        print('Transformação para origem: {matriz}'.format(matriz = backToOriginTransformation ))
        originBody = backToOriginTransformation.dot(self.body.transpose())
        rad_angle = (angle * pi)/180.0
        rotation_matrix = np.array([
                                    [1,     0,              0,                  0],
                                    [0, cos(rad_angle), (-1)*sin(rad_angle),    0],
                                    [0, sin(rad_angle), cos(rad_angle),         0],
                                    [0,     0,              0,                  1]
                                ])
        bodyRotatedAtOrigin = rotation_matrix.dot(originBody)
        rotatedBodyBackToCurrentPosition = (self.transformations_tracker.dot(bodyRotatedAtOrigin)).transpose()
        self.body = rotatedBodyBackToCurrentPosition
        # self.body = originBody.transpose()
        # print(self.body)
        self.track_transformation(rotation_matrix)
        return

    def rotateY(self, angle):
        backToOriginTransformation = np.linalg.inv(self.transformations_tracker)
        originBody = backToOriginTransformation.dot(self.body.transpose())
        rad_angle = (angle * pi)/180.0
        rotation_matrix = np.array([
                                    [cos(rad_angle),        0, sin(rad_angle),  0],
                                    [   0,                  1,      0,          0],
                                    [(-1)*sin(rad_angle),   0, cos(rad_angle),  0],
                                    [   0,                  0,      0,          1]
                                ])
        bodyRotatedAtOrigin = rotation_matrix.dot(originBody)
        rotatedBodyBackToCurrentPosition = (self.transformations_tracker.dot(bodyRotatedAtOrigin)).transpose()
        self.body = rotatedBodyBackToCurrentPosition
        # self.body = originBody.transpose()
        # print(self.body)
        self.track_transformation(rotation_matrix)
        return

    def rotateZ(self, angle):
        backToOriginTransformation = np.linalg.inv(self.transformations_tracker)
        originBody = backToOriginTransformation.dot(self.body.transpose())
        rad_angle = (angle * pi)/180.0
        rotation_matrix = np.array([
                                    [cos(rad_angle), (-1)*sin(rad_angle),   0, 0],
                                    [sin(rad_angle), cos(rad_angle),        0, 0],
                                    [      0,              0,               1, 0],
                                    [      0,              0,               0, 1]
                                ])
        bodyRotatedAtOrigin = rotation_matrix.dot(originBody)
        rotatedBodyBackToCurrentPosition = (self.transformations_tracker.dot(bodyRotatedAtOrigin)).transpose()
        self.body = rotatedBodyBackToCurrentPosition
        self.track_transformation(rotation_matrix)
        return

    def track_transformation(self, transformation):
        self.transformations_tracker = transformation.dot(self.transformations_tracker)
        return
