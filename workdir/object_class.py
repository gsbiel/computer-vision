import numpy as np

class Object:

    def __init__(self, body_definition):
        self.body = body_definition
        return

    def translateX(self, dx=1):
        translation_matrix = np.array([[1,0,0,dx], [0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        return

    def translateY(self, dy=1):
        translation_matrix = np.array([[1,0,0,0], [0,1,0,dy],[0,0,1,0],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()     
        return

    def translateZ(self, dz=1):
        translation_matrix = np.array([[1,0,0,0], [0,1,0,0],[0,0,1,dz],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()        
        return

    def translateXY(self, code, d=1):
        if code == "00":
            translation_matrix = np.array([[1,0,0,-1*d], [0,1,0,-1*d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        elif code == "01":
            translation_matrix = np.array([[1,0,0,-1*d], [0,1,0,d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        elif code == "10":
            translation_matrix = np.array([[1,0,0,d], [0,1,0,-1*d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        elif code == "11":
            translation_matrix = np.array([[1,0,0,d], [0,1,0,d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        return
