from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

class Dice:

    def __init__(self, cube_definition):
        self.body = cube_definition
        self.generate_faces()
        return

    def translateX(self, dx=1):
        translation_matrix = np.array([[1,0,0,dx], [0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        self.generate_faces()
        return

    def translateY(self, dy=1):
        translation_matrix = np.array([[1,0,0,0], [0,1,0,dy],[0,0,1,0],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        self.generate_faces()
        return

    def translateZ(self, dz=1):
        translation_matrix = np.array([[1,0,0,0], [0,1,0,0],[0,0,1,dz],[0,0,0,1]])
        self.body = (translation_matrix.dot(self.body.transpose())).transpose()
        self.generate_faces()
        return

    def translateXY(self, code, d=1):
        if code == "00":
            translation_matrix = np.array([[1,0,0,-1*d], [0,1,0,-1*d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.generate_faces()
        elif code == "01":
            translation_matrix = np.array([[1,0,0,-1*d], [0,1,0,d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.generate_faces()
        elif code == "10":
            translation_matrix = np.array([[1,0,0,d], [0,1,0,-1*d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.generate_faces()
        elif code == "11":
            translation_matrix = np.array([[1,0,0,d], [0,1,0,d],[0,0,1,0],[0,0,0,1]])
            self.body = (translation_matrix.dot(self.body.transpose())).transpose()
            self.generate_faces()
        return
        
    def generate_faces(self):

        # cube_definition é passado em coordenadas homogêneas, preciso remover isso para poder plotar no eixo 3D.
        cube_definition_adjusted = []
        for point in self.body:
            cube_definition_adjusted.append(point[:-1])
            
        # Agora o plot segue normal
        cube_definition_array = [
            np.array(list(item))
            for item in cube_definition_adjusted
        ]

        points = []
        points += cube_definition_array
        vectors = [
            cube_definition_array[1] - cube_definition_array[0],
            cube_definition_array[2] - cube_definition_array[0],
            cube_definition_array[3] - cube_definition_array[0]
        ]

        points += [cube_definition_array[0] + vectors[0] + vectors[1]]
        points += [cube_definition_array[0] + vectors[0] + vectors[2]]
        points += [cube_definition_array[0] + vectors[1] + vectors[2]]
        points += [cube_definition_array[0] + vectors[0] + vectors[1] + vectors[2]]

        points = np.array(points)

        edges = [
            [points[0], points[3], points[5], points[1]],
            [points[1], points[5], points[7], points[4]],
            [points[4], points[2], points[6], points[7]],
            [points[2], points[6], points[3], points[0]],
            [points[0], points[2], points[4], points[1]],
            [points[3], points[6], points[7], points[5]]
        ]

        self.faces = Poly3DCollection(edges, linewidths=1, edgecolors='k', facecolors=['b','r','g','y','m','k'])
        
        return