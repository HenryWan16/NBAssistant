from config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dataset import connect
from players import Player
from schedules import Schedule
from teams import Team
from teams import TeamPlayer
import logging


configuration = Config()
db = connect(configuration.SQLALCHEMY_DATABASE_URI)
month_dict = {
    'october': "10",
    'november': "11",
    'december': "12",
    'january': "01",
    'february': "02",
    'march': "03",
    'april': "04"
}


class WebCrawler:
    def __init__(self):
        if configuration.CHROME_HEAD_LESS:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            self.driver = webdriver.Chrome(chrome_options=options)
        else:
            self.driver = webdriver.Chrome()
        if configuration.IMPLICIT_WAIT:
            self.driver.implicitly_wait(configuration.IMPLICIT_WAIT_TIME)
        self.wait = WebDriverWait(self.driver, configuration.WAIT_TIME)
        # self.wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)), configuration.WAIT_TIME)
        configuration.log_init()
        self.logger = logging.getLogger()

    def get_teams_info(self, basic_url):
        url = basic_url + "teams"
        self.driver.get(url)
        team_logos = []
        team_full_names = []
        team_locations = []
        team_urls = []

        # full_name and logo
        teams_hrefs_elements = self.driver.find_elements(By.XPATH, "//table[@id='teams_active']//tbody//th/a")
        for team_href_element in teams_hrefs_elements:
            current_team_url = team_href_element.get_attribute("href")
            team_full_names.append(team_href_element.text)
            temp = current_team_url.split("/")
            logo = "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/" + temp[-2] + ".png"
            team_logos.append(logo)
            # debug log:
            self.logger.debug("Teams crawler (logo): " + logo)
            team_url = "https://www.basketball-reference.com/teams/" + temp[-2] + "/"
            team_urls.append(team_url)
            # debug log:
            self.logger.debug("Teams crawler (description): " + team_url)

        # location
        for team_url in team_urls:
            self.driver.get(team_url)
            try:
                location_element = self.driver.find_element_by_xpath("//div[@id='meta']/div[2]/p[1]")
                location = location_element.text
                team_locations.append(location)
                # debug log
                self.logger.debug("Team crawler (location): " + location)
            except NoSuchElementException:
                team_locations.append(None)

        # i = 12
        # print(team_full_names[i])
        # print(team_logos[i])
        # print(team_locations[i])
        # print(team_urls[i])
        team_table_handler = db['teams']
        for i in range(0, len(team_full_names)):
            team = Team(name=team_full_names[i], logo=team_logos[i], location=team_locations[i], description=team_urls[i])
            team_json = team.__dict__
            team_table_handler.upsert(team_json, ['name'])
            # info log
            self.logger.debug("Upsert team (name) successfully! " + team_full_names[i])


    def get_schedules_info(self, schedules_url, year, month):
        url = schedules_url + "NBA_" + str(year) + "_games-" + month + ".html"
        self.driver.get(url)
        schedule_dates = []
        schedule_start_time_ETs = []
        schedule_visitors = []
        schedule_visitors_score = []
        schedule_homes = []
        schedule_homes_score = []

        # date
        schedules_date_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//th/a")
        for schedule in schedules_date_elements:
            raw_text = schedule.text
            day = raw_text.split(",")[1].split()[-1]
            date_str = str(year) + "-" + month_dict[month] + "-" + day
            schedule_dates.append(date_str)
            # debug log
            self.logger.debug("Schedule crawler (date): " + date_str)

        # start_time_ET
        schedules_start_time_ET_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//td[@data-stat='game_start_time']")
        for start_time_ET in schedules_start_time_ET_elements:
            start_time_ET_str = start_time_ET.text
            schedule_start_time_ETs.append(start_time_ET_str)
            # debug log
            self.logger.debug("Schedule crawler (start_time_ET): " + start_time_ET_str)

        # visitor
        visitors_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//td[@data-stat='visitor_team_name']")
        for visitor in visitors_elements:
            visitor_str = visitor.text
            schedule_visitors.append(visitor_str)
            # debug log
            self.logger.debug("Schedule crawler (visitor): " + visitor_str)

        # visitor_score
        visitors_score_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//td[@data-stat='visitor_pts']")
        for visitor_score in visitors_score_elements:
            visitor_score_str = visitor_score.text
            schedule_visitors_score.append(visitor_score_str)
            # debug log
            self.logger.debug("Schedule crawler (visitor_score): " + visitor_score_str)

        # home
        homes_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//td[@data-stat='home_team_name']")
        for home in homes_elements:
            home_str = home.text
            schedule_homes.append(home_str)
            # debug log
            self.logger.debug("Schedule crawler (home): " + home_str)

        # home_score
        homes_score_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//td[@data-stat='home_pts']")
        for home_score in homes_score_elements:
            home_score_str = home_score.text
            schedule_homes_score.append(home_score_str)
            # debug log
            self.logger.debug("Schedule crawler (home_score): " + home_score_str)

        # i = 5
        # print(schedule_dates[i])
        # print(schedule_start_time_ETs[i])
        # print(schedule_homes[i])
        # print(schedule_homes_score[i])
        # print(schedule_visitors[i])
        # print(schedule_visitors_score[i])
        team_table_handler = db['teams']
        schedule_table_handler = db['schedules']
        for i in range(0, len(schedule_dates)):
            visitor = team_table_handler.find_one(name=schedule_visitors[i])
            visitor_id = visitor['id']
            team = team_table_handler.find_one(name=schedule_homes[i])
            home_id = team['id']
            schedule = Schedule(date=schedule_dates[i], start=schedule_dates[i],
                                visitor=schedule_visitors[i], home=schedule_homes[i],
                                teamA_id=visitor_id, teamA_score=schedule_visitors_score[i],
                                teamB_id=home_id, teamB_score=schedule_homes_score[i])
            schedule_json = schedule.__dict__
            schedule_table_handler.upsert(schedule_json, ['date', 'visitor'])
            # info log
            self.logger.info("Upsert schedule (date and visitor_name) successfully! " + schedule_dates[i] + " " + schedule_visitors[i])

    def get_players_info(self, players_url, character, target_year):
        url = players_url + str(character)
        self.driver.get(url)

        # to_year length
        players_to_year_elements = self.driver.find_elements(By.XPATH,
                                                             "//table[@id='players']//tbody//tr/td[@data-stat='year_max']")
        n = len(players_to_year_elements)
        for i in range(0, n):
            self.driver.get(url)

            # to_year
            try:

                player_to_year_element = self.driver.find_element_by_xpath("(//table[@id='players']//tbody//tr/td[@data-stat='year_max'])[" + str(i) + "]")
            except NoSuchElementException:
                continue
            player_to_year = int(player_to_year_element.text)
            if player_to_year < target_year:
                continue

            try:
                player_name_element = self.driver.find_element_by_xpath("(//table[@id='players']//tbody//tr/th//a)[" + str(i) + "]")
            except NoSuchElementException:
                continue
            player_name = player_name_element.text
            # debug log
            self.logger.debug("Player clawler (name): " + player_name)

            # photo and description
            try:
                player_tag_element = self.driver.find_element_by_xpath("(//table[@id='players']//tbody//tr/th)[" + str(i) + "]")
            except NoSuchElementException:
                continue
            tag = player_tag_element.get_attribute("data-append-csv")
            player_photo = "https://d2cwpp38twqe55.cloudfront.net/req/201811081/images/players/" + tag + ".jpg"
            player_description = url + "/" + tag + ".html"

            # position
            try:
                player_position_element = self.driver.find_element_by_xpath("(//table[@id='players']//tbody//tr/td[@data-stat='pos'])[" + str(i) + "]")
            except NoSuchElementException:
                continue
            player_position = player_position_element.text
            # debug log
            self.logger.debug("Player clawler (position): " + player_position)

            # height
            try:
                player_height_element = self.driver.find_element_by_xpath("(//table[@id='players']//tbody//tr/td[@data-stat='height'])[" + str(i) + "]")
            except NoSuchElementException:
                continue
            player_height = player_height_element.text
            # debug log
            self.logger.debug("Player clawler (height): " + player_height)

            # weight
            try:
                player_weight_element = self.driver.find_element_by_xpath("(//table[@id='players']//tbody//tr/td[@data-stat='weight'])[" + str(i) + "]")
            except NoSuchElementException:
                continue
            player_weight = player_weight_element.text
            # debug log
            self.logger.debug("Player clawler (weight): " + player_weight)

            # team and points
            self.driver.get(player_description)
            try:
                # a special way to find xpath
                team_name_element = self.driver.find_element_by_xpath("//div[@id='meta']//a[contains(@href, 'teams')]")
                player_team = team_name_element.text
            except NoSuchElementException:
                player_team = None
            # debug log
            self.logger.debug("Player name: " + str(player_name) + "Player clawler (player's team name): " + str(player_team))
            try:
                # self.wait.until(EC.presence_of_element_located(
                #     (By.XPATH, "//div[@class='stats_pullout']//div[@class='p1']/div[2]/p[2]")),
                #     configuration.WAIT_TIME)
                player_points_element = self.driver.find_element_by_xpath("//div[@class='stats_pullout']//div[@class='p1']/div[2]/p[2]")
                player_points = player_points_element.text
            except NoSuchElementException:
                player_points = None
            # debug log
            self.logger.debug("Player name: " + str(player_name) + "Player clawler (player's points): " + str(player_points))

            # insert into player table and team_player table
            player_table_handler = db['players']
            team_table_handler = db['teams']
            team_players_table_handler = db['team_players']
            player = Player(name=player_name, gender='Male',
                            photo=player_photo, position=player_position,
                            height=player_height, weight=player_weight,
                            points=player_points, first_character=character,
                            description=player_description)
            player_json = player.__dict__
            player_table_handler.upsert(player_json, ['name'])
            # info log
            self.logger.info("Upsert player (name) successfully! " + str(player_name))

            player = player_table_handler.find_one(name=player_name)
            player_id = player['id']

            if not player_team:
                continue
            team = team_table_handler.find_one(name=player_team)
            if team:
                team_id = team['id']
                team_player = TeamPlayer(team_id, player_id)
                team_player_json = team_player.__dict__
                team_players_table_handler.upsert(team_player_json, ['player_id'])
                # info log
                self.logger.info("Upsert team_player (team_id, player_id) successfully! " + str(team_id) + " " + str(player_id))

    def craw(self):
        self.get_teams_info(configuration.BASIC_URL)
        years = [2019, 2018]
        months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
        for year in years:
            for month in months:
                self.get_schedules_info(configuration.SCHEDULES_URL, year, month)
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for c in characters:
            self.get_players_info(configuration.PLAYERS_URL, c, configuration.TARGET_YEAR)

# unit test
if __name__ == '__main__':
    web_crawler = WebCrawler()
    web_crawler.craw()
    web_crawler.driver.close()
    web_crawler.driver.quit()