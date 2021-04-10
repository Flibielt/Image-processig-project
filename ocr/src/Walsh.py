import math

import numpy as np


class Walsh:
    def __init__(self, n):
        self.walsh_matrix = generate_walsh(n, n)
        self.walsh_size = n

    def generate_feature_vector(self, image):
        feature_vector = np.sum(np.multiply(image, self.walsh_matrix[:1].reshape(64, 64)))

        for i in range(1, self.walsh_size):
            feature_vector = np.append(feature_vector,
                                       np.sum(np.multiply(image, self.walsh_matrix[i:i + 1].reshape(64, 64))))


def generate_walsh(n, count):
    if n < count:
        print("count must be lower or equal with n")
        return

    walsh_size = n ** 2

    walsh_matrix = generate_walsh_matrix(walsh_size)
    return walsh_matrix[:count, :walsh_size]


def generate_walsh_matrix(n):
    if n < 1:
        print("n must be a positive number")
        return
    else:
        lg2 = int(math.log(n, 2))

        if 2 ** lg2 != n:
            print("n must be a power of 2")
            return

    walsh_matrix = np.array([[1]], dtype=int)

    for i in range(0, lg2):
        walsh_matrix = np.vstack((np.hstack((walsh_matrix, walsh_matrix)), np.hstack((walsh_matrix, -walsh_matrix))))

    return walsh_matrix
