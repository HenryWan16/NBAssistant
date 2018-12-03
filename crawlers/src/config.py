import sys
import logging


class Config:
    # testing SQL ip is 127.0.0.1:3307
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://twist:twist@mysql/nbassistant'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://twist:twist@127.0.0.1:3307/nbassistant'
    WAIT_TIME = 5
    TARGET_YEAR = 2017
    BASIC_URL = "https://www.basketball-reference.com/"
    PLAYERS_URL = "https://www.basketball-reference.com/players/"
    SCHEDULES_URL = "https://www.basketball-reference.com/leagues/"
    CHROME_HEAD_LESS = True
    IMPLICIT_WAIT = True
    IMPLICIT_WAIT_TIME = 5
    LOG_LEVEL = logging.DEBUG
    LOG_FILE = "crawlers.log"
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

