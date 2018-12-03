import pandas as pd
from collections import defaultdict


standing = pd.read_csv("2018-2019_standings.csv")
standing.columns = ["Rank", "Team", "Overall", "Home",
                    "Road", "Team Points Per Game",
                    "Opponent Points Per Game"]
gameResult = pd.read_csv("2018-2019_Data.csv", parse_dates=["Date"])
gameResult.columns = ['Date', 'Start Time(ET)', 'Visitor Team', 'Visitor Score','Home Team',
                'Home Score', 'Box Score', 'OT', 'Attendance', 'Notes']
gameResult['Home Team Win'] = gameResult['Home Score'] > gameResult['Visitor Score']
n_games = gameResult["Home Score"].count()
n_homewins = gameResult["Home Team Win"].sum()
league_home_win_percentage = n_homewins / n_games
league_team_score_point_average = standing["Team Points Per Game"].mean()
league_team_lose_point_average = standing["Opponent Points Per Game"].mean()
# print(league_team_score_point_average)
# print(league_team_lose_point_average)
# print(n_games)
# print(n_homewins)
# print(league_home_win_percentage)
# this year 60% home wins
home_percentage = defaultdict(float)
road_percentage = defaultdict(float)
for index, row in standing.iterrows():
    team = row["Team"]
    homeRecord = row["Home"]
    numberOfHomeWins = int(homeRecord.split('-')[0])
    numberOfHomeLoses = int(homeRecord.split('-')[1])
    # print(numberOfHomeWins)
    roadRecord = row["Road"]
    numberOfRoadWins = int(roadRecord.split('-')[0])
    numberOfRoadLoses = int(roadRecord.split('-')[1])
    home_percentage[team] = numberOfHomeWins / (numberOfHomeWins + numberOfHomeLoses)
    road_percentage[team] = numberOfRoadWins / (numberOfRoadWins + numberOfRoadLoses)

count = 0
gameResult["Home Predicted Score"] = 0
gameResult["Visitor Predicted Score"] = 0
score_point = defaultdict()
lose_point = defaultdict()
for index, row in standing.iterrows():
    team = row["Team"]
    score_point[team] = row["Team Points Per Game"]
    lose_point[team] = row["Opponent Points Per Game"]
for index, row in gameResult.iterrows():
    home_team = row["Home Team"]
    visitor_team = row["Visitor Team"]
    factor = (league_home_win_percentage - 0.5) * 2 + (home_percentage[home_team] - road_percentage[visitor_team])
    row["Home Predicted Score"] = (1 + 0.5 * factor) * score_point[home_team] * \
                        lose_point[visitor_team] / league_team_lose_point_average
    row["Visitor Predicted Score"] = score_point[visitor_team] * \
                           lose_point[home_team] / league_team_lose_point_average / (1 + 0.5 * factor)

    # gameResult.set_value(index,"Home Predicted Score",(1 + 0.5 * factor) * score_point[home_team] * \
    #                     lose_point[visitor_team] / league_team_lose_point_average)
    # gameResult.set_value(index,"Visitor Predicted Score",(1 + 0.5 * factor) * score_point[visitor_team] * \
    #                        lose_point[home_team] / league_team_lose_point_average)
    if ((row["Home Predicted Score"] > row["Visitor Predicted Score"]) & (row['Home Score'] > row['Visitor Score'])):
        count += 1
    if ((row["Home Predicted Score"] <= row["Visitor Predicted Score"]) & (row['Home Score'] <= row['Visitor Score'])):
        count += 1
    gameResult.loc[index] = row
print(count / n_games)
# this year predicting accuracy 71.4%
numberOfWinsForEachTeam = defaultdict(int)
def countWins(team):
    count = 0
    for index, row in gameResult.iterrows():
        if((row["Home Team"] == team) & (row["Home Predicted Score"] > row["Visitor Predicted Score"])):
            count += 1
        if((row["Visitor Team"] == team) & (row["Home Predicted Score"] <= row["Visitor Predicted Score"])):
            count += 1
    numberOfWinsForEachTeam[team] = count
for index, row in standing.iterrows():
    team = row["Team"]
    countWins(team)
    # print(team)
    # print(numberOfWinsForEachTeam[team])
    # use a heap here to create the list for both eastern and western conference
# based on the output and get the playoffs team for each conference
eastern_conference_playoffs_teams_name = ["Toronto Raptors" , "Milwaukee Bucks", "Boston Celtics", "Indiana Pacers",
                                     "Detroit Pistons", "Orlando Magic", "Philadelphia 76ers", "Charlotte Hornets" ]
western_conference_playoffs_teams_name = ["Denver Nuggets", "Oklahoma City Thunder", "Memphis Grizzlies", "Los Angeles Clippers",
                                     "Golden State Warriors", "Los Angeles Lakers", "Portland Trail Blazers", "Houston Rockets"]
eastern_conference_playoffs_teams = ["TOR", "MIL", "BOS", "IND",
                                     "DET", "ORL", "PHI", "CHO"]

western_conference_playoffs_teams = ["DEN", "OKC", "MEM", "LAC",
                                     "GSW", "LAL", "POR", "HOU"]
player_statistics = pd.read_csv("2018-2019_playerAdvancedStatistic.csv")
# PER is known as player efficiency rating
player_statistics.columns = ["Player", "Position", "Age", "Team",
                             "Game Played", "Minutes Played", "PER"]
player_statistics["Minutes Per Game"] = player_statistics["Minutes Played"] / player_statistics["Game Played"]
print(player_statistics.head())
MVP_Candidate_PER_Requirement = 25.0
MVP_Candidate_Minutes_Requirement = 32.0
maxPER = 0
MVP_Player = ""
for index, row in player_statistics.iterrows():
    player = row["Player"]
    team = row["Team"]
    playerPER = row["PER"]
    minutes = row["Minutes Played"]
    if ((minutes >= MVP_Candidate_Minutes_Requirement) & (playerPER >= MVP_Candidate_PER_Requirement)
    & ((team in western_conference_playoffs_teams) | (team in eastern_conference_playoffs_teams))):
        if playerPER > maxPER:
            maxPER = playerPER
            MVP_Player = player

print(MVP_Player)




