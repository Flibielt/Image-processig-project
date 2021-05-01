import sys

from .etalon import Etalon


def calculate_distance(character, etalon):
    distance = 0

    for i in range(0, len(character)):
        distance = distance + abs(character[i] - etalon[i])

    return distance


class CharacterRecognizing:
    def __init__(self):
        self.etalon = Etalon()
        self.etalon.create_etalon_matrix()

    def recognize_characters(self, characters):
        etalon_matrix = self.etalon.etalon_matrix
        text = ""

        for character in characters:
            min_distance = sys.maxsize
            min_position = 0

            if character.text != " ":
                for i in range(0, len(etalon_matrix)):
                    distance = calculate_distance(character.feature_vector, etalon_matrix[i].feature_vector)

                    if distance < min_distance:
                        min_distance = distance
                        min_position = i

                character.text = etalon_matrix[min_position].text

        for character in characters:
            text = text + character.text

        return text
