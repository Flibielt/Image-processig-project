import math

import numpy as np


class Walsh:
    def __init__(self):
        self.hadamard_matrix = generate_hadamard_matrix()

    def generate_feature_vector(self, image):
        walsh_matrix = self.get_walsh_matrix(0)
        feature_vector = np.sum(np.multiply(image, walsh_matrix))

        for i in range(1, 8):
            walsh_matrix = self.get_walsh_matrix(i)
            feature_vector = np.append(feature_vector, np.sum(np.multiply(image, walsh_matrix)))

        return feature_vector

    def get_walsh_matrix(self, n):
        walsh_matrix = self.hadamard_matrix[n].reshape(4, 4)
        resized_walsh_matrix = np.zeros((64, 64))

        for x in range(0, 64):
            for y in range(0, 64):
                orig_x = int(x / 16)
                orig_y = int(y / 16)
                if walsh_matrix[orig_x, orig_y] == 1:
                    resized_walsh_matrix[x, y] = -1
                else:
                    resized_walsh_matrix[x, y] = 1

        return resized_walsh_matrix.reshape(64, 64)


def generate_hadamard_matrix():
    lg2 = int(math.log(16, 2))

    hadamard_matrix = np.array([[1]], dtype=int)

    for i in range(0, lg2):
        hadamard_matrix = np.vstack((np.hstack((hadamard_matrix, hadamard_matrix)),
                                     np.hstack((hadamard_matrix, -hadamard_matrix))))

    needed_hadamard_matrix = hadamard_matrix[0:8, :]

    return needed_hadamard_matrix
