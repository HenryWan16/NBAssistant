from config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dataset import connect
from players import Player
from schedules import Schedule
from teams import Team
from teams import TeamPlayer
import time


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
            print("Teams crawler (logo): " + logo)
            team_url = "https://www.basketball-reference.com/teams/" + temp[-2] + "/"
            team_urls.append(team_url)
            # debug log:
            print("Teams crawler (description): " + team_url)

        # location
        for team_url in team_urls:
            self.driver.get(team_url)
            try:
                location_element = self.driver.find_element_by_xpath("//div[@id='meta']/div[2]/p[1]")
                location = location_element.text
                team_locations.append(location)
                # debug log
                print("Team crawler (location): " + location)
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
            print("Upsert team (name) successfully! " + team_full_names[i])


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
            print("Schedule crawler (date): " + date_str)

        # start_time_ET
        schedules_start_time_ET_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//td[@data-stat='game_start_time']")
        for start_time_ET in schedules_start_time_ET_elements:
            start_time_ET_str = start_time_ET.text
            schedule_start_time_ETs.append(start_time_ET_str)
            # debug log
            print("Schedule crawler (start_time_ET): " + start_time_ET_str)

        # visitor
        visitors_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//td[@data-stat='visitor_team_name']")
        for visitor in visitors_elements:
            visitor_str = visitor.text
            schedule_visitors.append(visitor_str)
            # debug log
            print("Schedule crawler (visitor): " + visitor_str)

        # visitor_score
        visitors_score_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//td[@data-stat='visitor_pts']")
        for visitor_score in visitors_score_elements:
            visitor_score_str = visitor_score.text
            schedule_visitors_score.append(visitor_score_str)
            # debug log
            print("Schedule crawler (visitor_score): " + visitor_score_str)

        # home
        homes_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//td[@data-stat='home_team_name']")
        for home in homes_elements:
            home_str = home.text
            schedule_homes.append(home_str)
            # debug log
            print("Schedule crawler (home): " + home_str)

        # home_score
        homes_score_elements = self.driver.find_elements(By.XPATH, "//table[@id='schedule']//tbody//td[@data-stat='home_pts']")
        for home_score in homes_score_elements:
            home_score_str = home_score.text
            schedule_homes_score.append(home_score_str)
            # debug log
            print("Schedule crawler (home_score): " + home_score_str)

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
            print("Upsert schedule (date and visitor_name) successfully! " + schedule_dates[i] + " " + schedule_visitors[i])

    def get_players_info(self, players_url, character):
        url = players_url + str(character)
        self.driver.get(url)
        player_names = []
        player_descriptions = []
        player_photos = []
        player_positions = []
        player_heights = []
        player_weights = []
        player_teams = []
        player_points = []

        # name
        players_name_elements = self.driver.find_elements(By.XPATH, "//table[@id='players']//tbody//tr/th/a")
        for player_name in players_name_elements:
            player_name_str = player_name.text
            player_names.append(player_name_str)
            # debug log
            print("Player clawler (name): " + player_name_str)

        # photo and description
        players_tag_elements = self.driver.find_elements(By.XPATH, "//table[@id='players']//tbody//tr/th")
        for player_tag in players_tag_elements:
            tag = player_tag.get_attribute("data-append-csv")
            photo = "https://d2cwpp38twqe55.cloudfront.net/req/201811081/images/players/" + tag + ".jpg"
            player_photos.append(photo)
            # debug log
            print("Player clawler (photo): " + photo)

            description = url + "/" + tag + ".html"
            player_descriptions.append(description)
            # debug log
            print("Player clawler (description): " + description)

        # position
        players_pos_elements = self.driver.find_elements(By.XPATH, "//table[@id='players']//tbody//tr/td[@data-stat='pos']")
        for player_pos in players_pos_elements:
            player_pos_str = player_pos.text
            player_positions.append(player_pos_str)
            # debug log
            print("Player clawler (position): " + player_pos_str)

        # height
        players_height_elements = self.driver.find_elements(By.XPATH, "//table[@id='players']//tbody//tr/td[@data-stat='height']")
        for player_height in players_height_elements:
            player_height_str = player_height.text
            player_heights.append(player_height_str)
            # debug log
            print("Player clawler (height): " + player_height_str)

        # weight
        players_weight_elements = self.driver.find_elements(By.XPATH, "//table[@id='players']//tbody//tr/td[@data-stat='weight']")
        for player_weight in players_weight_elements:
            player_weight_str = player_weight.text
            player_weights.append(player_weight_str)
            # debug log
            print("Player clawler (weight): " + player_weight_str)

        # team and point
        for player_desc in player_descriptions:
            self.driver.get(player_desc)
            try:
                team_name_element = self.driver.find_element_by_xpath("//div[@id='meta']//div[2]/p[5]/a")
                team_name_str = team_name_element.text
                player_teams.append(team_name_str)
                # debug log
                print("Player clawler (player's team name): " + team_name_str)
            except NoSuchElementException:
                player_teams.append(None)
                # debug log
                print("Player clawler (player's team name): No team")
            try:
                point_element = self.driver.find_element_by_xpath("//div[@class='stats_pullout']//div[@class='p1']/div[2]/p[2]")
                point_str = point_element.text
                player_points.append(point_str)
                # debug log
                print("Player clawler (points): " + point_str)
            except NoSuchElementException:
                player_points.append(None)
                # debug log
                print("Player clawler (points): No point currently")

        # i = 5
        # print(player_names[i])
        # print(player_descriptions[i])
        # print(player_photos[i])
        # print(player_positions[i])
        # print(player_heights[i])
        # print(player_weights[i])
        # print(player_teams[i])
        # print(player_points[i])
        player_table_handler = db['players']
        team_table_handler = db['teams']
        team_players_table_handler = db['team_players']
        for i in range(0, len(player_names)):
            player = Player(name=player_names[i], gender='Male',
                            photo=player_photos[i], position=player_positions[i],
                            height=player_heights[i], weight=player_weights[i],
                            points=player_points[i], description=player_descriptions[i])
            player_json = player.__dict__
            player_table_handler.upsert(player_json, ['name'])
            # debug log
            print("Upsert player (name) successfully! " + player_names[i])

            player = player_table_handler.find_one(name=player_names[i])
            player_id = player['id']

            if not player_teams[i]:
                continue
            team = team_table_handler.find_one(name=player_teams[i])
            team_id = team['id']
            team_player = TeamPlayer(team_id, player_id)
            team_player_json = team_player.__dict__
            team_players_table_handler.upsert(team_player_json, ['player_id'])
            # debug log
            print("Upsert team_player (team_id, player_id) successfully! " + str(team_id) + " " + str(player_id))

    def update_players_info(self, players_url, character, target_year):
        url = players_url + str(character)
        self.driver.get(url)
        last_year_element = self.driver.find_element_by_xpath("//table[@id='players']//tbody//td[@data-stat='year_max']")
        last_year = int(last_year_element.text)
        if last_year >= target_year:
            self.get_players_info(players_url, character)

    def craw(self):
        self.get_teams_info(configuration.BASIC_URL)
        years = [2019, 2018, 2017, 2016, 2015]
        months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
        for year in years:
            for month in months:
                self.get_schedules_info(configuration.SCHEDULES_URL, year, month)
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for c in characters:
            self.get_players_info(configuration.PLAYERS_URL, c)

# unit test
if __name__ == '__main__':
    web_crawler = WebCrawler()
    web_crawler.craw()
    web_crawler.driver.close()
    web_crawler.driver.quit()