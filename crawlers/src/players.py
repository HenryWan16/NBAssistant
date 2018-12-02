from decimal import Decimal
import datetime


class Player:
    def __init__(self, name, gender, photo, position, height, weight, points, description):
        self.name = name
        self.gender = gender
        self.photo = photo
        self.position = position
        self.height = height
        self.weight = int(weight)
        self.points = Decimal(points)
        self.description = description
        self.created_at = datetime.datetime.utcnow()


if __name__ == '__main__':
    player = Player("King", "Male", "XXXXXXX", "G", "6-5", "255", "24.8", "XXX")
    print(player.__dict__)