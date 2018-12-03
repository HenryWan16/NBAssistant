from decimal import Decimal
import datetime


class Player:
    def __init__(self, name, gender, photo, position, height, weight, points, first_character, description):
        self.name = name
        self.gender = gender
        self.photo = photo
        self.position = position
        self.height = height
        self.weight = int(weight) if weight else None
        self.points = Decimal(points) if points else None
        self.first_character = first_character
        self.description = description
        self.created_at = datetime.datetime.utcnow()


if __name__ == '__main__':
    player = Player("King", "Male", "XXXXXXX", "G", "6-5", "255", "24.8", "y", "XXX")
    print(player.__dict__)