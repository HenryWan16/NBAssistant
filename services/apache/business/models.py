# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Index, Numeric, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class AwardsPrediction(db.Model):
    __tablename__ = 'awards_prediction'

    id = db.Column(db.BigInteger, primary_key=True)
    MVP = db.Column(db.String(100), nullable=False)
    eastern_champion = db.Column(db.String(100), nullable=False)
    western_champion = db.Column(db.String(100), nullable=False)
    final_champion = db.Column(db.String(100), nullable=False)


class EasternConferencePlayoffsTeam(db.Model):
    __tablename__ = 'eastern_conference_playoffs_team'

    Team_Name = db.Column(db.String(100), primary_key=True)
    Team_Ranking = db.Column(db.String(100), nullable=False)


class EveryGamePredictedResult(db.Model):
    __tablename__ = 'every_game_predicted_result'

    Date = db.Column(db.String(100), primary_key=True, nullable=False)
    Start_Time_ET = db.Column(db.String(100), nullable=False)
    Visitor_Team = db.Column(db.String(100), primary_key=True, nullable=False)
    Home_Team = db.Column(db.String(100), nullable=False)
    Predicted_Visitor_Score = db.Column(db.String(100), nullable=False)
    Predicted_Home_Score = db.Column(db.String(100), nullable=False)


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), index=True)
    gender = db.Column(db.String(6))
    photo = db.Column(db.String(200))
    position = db.Column(db.String(100))
    height = db.Column(db.String(5))
    weight = db.Column(db.BigInteger)
    points = db.Column(db.Numeric(11, 2))
    first_character = db.Column(db.String(1))
    description = db.Column(db.String(2000))
    created_at = db.Column(db.DateTime)


class Schedule(db.Model):
    __tablename__ = 'schedules'
    __table_args__ = (
        db.Index('date_visitor', 'date', 'visitor'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    date = db.Column(db.String(10))
    start_time_ET = db.Column(db.String(10))
    visitor = db.Column(db.String(100))
    home = db.Column(db.String(100))
    teamA_id = db.Column(db.BigInteger)
    teamA_score = db.Column(db.BigInteger)
    teamB_id = db.Column(db.BigInteger)
    teamB_score = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime)


class TeamPlayer(db.Model):
    __tablename__ = 'team_players'
    __table_args__ = (
        db.Index('player_in_team', 'team_id', 'player_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    team_id = db.Column(db.BigInteger)
    player_id = db.Column(db.BigInteger, index=True)
    created_at = db.Column(db.DateTime)


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), index=True)
    logo = db.Column(db.String(200))
    big_logo = db.Column(db.String(200))
    location = db.Column(db.String(200))
    stadium = db.Column(db.String(200))
    owner = db.Column(db.String(100))
    coach = db.Column(db.String(100))
    manager = db.Column(db.String(100))
    description = db.Column(db.String(2000))
    achievement = db.Column(db.String(2000))
    created_at = db.Column(db.DateTime)


class TeamsExtra(db.Model):
    __tablename__ = 'teams_extra'

    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    team_name = db.Column(db.String(100), primary_key=True, nullable=False)
    stadium = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    coach = db.Column(db.String(100), nullable=False)
    manager = db.Column(db.String(100), nullable=False)
    achievement = db.Column(db.String(100), server_default=db.FetchedValue())


class WesternConferencePlayoffsTeam(db.Model):
    __tablename__ = 'western_conference_playoffs_team'

    Team_Name = db.Column(db.String(100), primary_key=True)
    Team_Ranking = db.Column(db.String(100), nullable=False)
