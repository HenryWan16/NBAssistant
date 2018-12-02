import datetime


class Schedule:
    def __init__(self, date, start, visitor, home, teamA_id, teamA_score, teamB_id, teamB_score):
        self.date = date
        self.start_time_ET = start
        self.visitor = visitor
        self.home = home
        self.teamA_id = int(teamA_id)
        self.teamA_score = int(teamA_score)
        self.teamB_id = int(teamB_id)
        self.teamB_score = int(teamB_score)
        self.created_at = datetime.datetime.utcnow()


if __name__ == '__main__':
    schedule = Schedule("2019-10-23", "8:00p", "New Orleans Pelicans", "Houston Rockets", "1301", "34", "1531", "78")
    print(schedule.__dict__)