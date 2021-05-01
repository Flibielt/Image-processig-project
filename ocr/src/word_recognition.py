import sys

from .etalon import Etalon


def calculate_distance(word, etalon):
    distance = 0

    for i in range(0, len(word)):
        distance = distance + abs(word[i] - etalon[i])

    return distance


class WordRecognizing:
    def __init__(self):
        self.etalon = Etalon()
        self.etalon.create_etalon_matrix()

    def recognize_words(self, words):
        etalon_matrix = self.etalon.etalon_matrix
        text = ""

        for word in words:
            min_distance = sys.maxsize
            min_position = 0

            if word.text != " ":
                for i in range(0, len(etalon_matrix)):
                    distance = calculate_distance(word.feature_vector, etalon_matrix[i].feature_vector)

                    if distance < min_distance:
                        min_distance = distance
                        min_position = i

                word.text = etalon_matrix[min_position].text

        for word in words:
            text = text + word.text

        return text
