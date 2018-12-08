import sys
import logging


class Config:
    HOST_IP = "10.250.196.180"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://twist:twist@" + HOST_IP + ":3307/nbassistant"
    TOP20_TEAMS = ["Golden State Warriors", "Boston Celtics", "Houston Rockets", "Philadelphia 76ers",
                   "Toronto Raptors", "Oklahoma City Thunder", "Utah Jazz", "Denver Nuggets",
                   "Los Angeles Lakers", "Portland Trail Blazers", "Indiana Pacers",
                   "New Orleans Pelicans", "San Antonio Spurs", "Washington Wizards",
                   "Minnesota Timberwolves", "Milwaukee Bucks", "Los Angeles Clippers",
                   "Memphis Grizzlies", "Dallas Mavericks", "Miami Heat"]
    TOP20_PLAYERS = ["LeBron James", "Kevin Durant", "Kawhi Leonard", "Anthony Davis", "Stephen Curry",
                     "Giannis Antetokounmpo", "James Harden", "Russell Westbrook", "Kyrie Irving",
                     "Klay Thompson", "Damian Lillard", "Chris Paul", "Joel Embiid", "Paul George",
                     "Jimmy Butler", "Ben Simmons", "Karl-Anthony Towns",
                     "Victor Oladipo", "Donovan Mitchell", "CJ McCollum"]

    LOG_LEVEL = logging.DEBUG
    LOG_FILE = ""
    LOG_RW_MODE = "w"

    def log_init(self):
        if self.LOG_FILE == "":
            logging.basicConfig(
                level=self.LOG_LEVEL,
                stream=sys.stdout
            )
        else:
            logging.basicConfig(
                level=self.LOG_LEVEL,
                filename=self.LOG_FILE,
                filemode=self.LOG_RW_MODE
            )