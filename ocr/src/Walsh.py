import math

import numpy as np


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
