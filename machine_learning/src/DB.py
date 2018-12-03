import mysql.connector
from mysql.connector import errorcode
import pandas as pd

eastern_conference_playoffs_teams_name = ["Toronto Raptors" , "Milwaukee Bucks", "Boston Celtics", "Indiana Pacers",
                                     "Detroit Pistons", "Orlando Magic", "Philadelphia 76ers", "Charlotte Hornets" ]
western_conference_playoffs_teams_name = ["Denver Nuggets", "Oklahoma City Thunder", "Memphis Grizzlies", "Los Angeles Clippers",
                                     "Golden State Warriors", "Los Angeles Lakers", "Portland Trail Blazers", "Houston Rockets"]
predicted = pd.read_csv("Predicted.csv")
# records_to_insert = [ (2,'Jon','2018-01-11', 26) ,
#                          (3,'Jane','2017-12-11', 27),
#                          (4,'Bill','2018-03-23', 26) ]
#    sql_insert_query = """ INSERT INTO python_users (id, name, birth_date, age)
#                        VALUES (%s,%s,%s,%s) """
#    cursor = connection.cursor(prepared=True)
#    #used executemany to insert 3 rows
#    result  = cursor.executemany(sql_insert_query, records_to_insert)
#    connection.commit()
#    print (cursor.rowcount, "Record inserted successfully into python_users table")


try:
  mydb = mysql.connector.connect(user='root', password='Woshirmz777haha',
                              host='127.0.0.1',database = 'predictions')

  cursor = mydb.cursor()
  cursor.execute("TRUNCATE TABLE eastern_conference_playoffs_team")
  i = 0
  while i < len(eastern_conference_playoffs_teams_name):
      sql_insert_query_eastern_playoffs = """ INSERT INTO `eastern_conference_playoffs_team` (`Team_Name`, `Team_Ranking`) VALUES (%s,%s)"""
      val = (eastern_conference_playoffs_teams_name[i], i+1)
      result = cursor.execute(sql_insert_query_eastern_playoffs, val)
      i += 1

  cursor.execute("TRUNCATE TABLE western_conference_playoffs_team")
  j = 0
  while j < len(eastern_conference_playoffs_teams_name):
      sql_insert_query_western_playoffs = """ INSERT INTO `western_conference_playoffs_team` (`Team_Name`, `Team_Ranking`) VALUES (%s,%s)"""
      val = (western_conference_playoffs_teams_name[j], j+1)
      result = cursor.execute(sql_insert_query_western_playoffs, val)
      j += 1
  # result = cursor.execute(sql_insert_query_eastern_playoffs, eastern_conference_playoffs_teams_name)
  cursor.execute("TRUNCATE TABLE awards_prediction")
  sql_insert_query_awards_prediction = """ INSERT INTO `awards_prediction` (`MVP`,`eastern_champion`, `western_champion`,`final_champion`) VALUES (%s,%s,%s,%s)"""
  mvp = "Giannis Antetokounmpo"
  east_champ = "Toronto Raptors"
  west_champ = "Golden State Warriors"
  final_champ = "Golden State Warriors"
  val = (mvp, east_champ, west_champ, final_champ)
  result = cursor.execute(sql_insert_query_awards_prediction, val)

  cursor.execute("TRUNCATE TABLE every_game_predicted_result")
  sql_insert_query_game = """ INSERT INTO `every_game_predicted_result` (`Date`,`Start_Time_ET`, `Visitor_Team`,`Home_Team`,
  `Predicted_Visitor_Score`,`Predicted_Home_Score`) VALUES (%s,%s,%s,%s,%s,%s)"""
  for index, row in predicted.iterrows():
      date = row["Date"]
      start_time = row["Start Time(ET)"]
      visitor_team = row["Visitor Team"]
      home_team = row["Home Team"]
      visitor_score = row["Visitor Predicted Score"]
      home_score = row["Home Predicted Score"]
      val = (date, start_time, visitor_team, home_team, visitor_score, home_score)
      result = cursor.execute(sql_insert_query_game, val)
  mydb.commit()

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
  else:
    print(err)
else:
  print("Connected to dblalallala")
  cursor = mydb.cursor()
  cursor.execute("Select database();")
  record = cursor.fetchone()
  print("You connected to - ", record)







