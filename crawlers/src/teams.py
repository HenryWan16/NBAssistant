import datetime


class Team:
    def __init__(self, name, logo, location, description):
        self.name = name
        self.logo = logo
        self.location = location
        self.description = description
        self.created_at = datetime.datetime.utcnow()


class TeamPlayer:
    def __init__(self, team_id, player_id):
        self.team_id = team_id
        self.player_id = player_id
        self.created_at = datetime.datetime.utcnow()


if __name__ == '__main__':
    team = Team("Houston Rockets", "logo_tiny_url", "Houston", "https://en.wikipedia.org/wiki/Houston_Rockets")
    print(team.__dict__)
    team_player = TeamPlayer(1321, 1201)
    print(team_player.__dict__)