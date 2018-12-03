# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.24)
# Database: nbassistant
# Generation Time: 2018-11-30 01:24:10 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table players
# ------------------------------------------------------------

DROP TABLE IF EXISTS `players`;

CREATE TABLE `players` (
  `id` bigint(64) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `position` varchar(100) DEFAULT NULL,
  `height` varchar(5) DEFAULT NULL,
  `weight` bigint(64) DEFAULT NULL,
  `points` decimal(11,2) DEFAULT NULL,
  `first_character` varchar(1) DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table schedules
# ------------------------------------------------------------

DROP TABLE IF EXISTS `schedules`;

CREATE TABLE `schedules` (
  `id` bigint(64) NOT NULL AUTO_INCREMENT,
  `date` varchar(10) DEFAULT NULL,
  `start_time_ET` varchar(10) DEFAULT NULL,
  `visitor` varchar(100) DEFAULT NULL,
  `home` varchar(100) DEFAULT NULL,
  `teamA_id` bigint(64) DEFAULT NULL,
  `teamA_score` bigint(64) DEFAULT NULL,
  `teamB_id` bigint(64) DEFAULT NULL,
  `teamB_score` bigint(64) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `date_visitor` (`date`, `visitor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table team_players
# ------------------------------------------------------------

DROP TABLE IF EXISTS `team_players`;

CREATE TABLE `team_players` (
  `id` bigint(64) NOT NULL AUTO_INCREMENT,
  `team_id` bigint(64) DEFAULT NULL,
  `player_id` bigint(64) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `player_in_team` (`team_id`,`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table teams
# ------------------------------------------------------------

DROP TABLE IF EXISTS `teams`;

CREATE TABLE `teams` (
  `id` bigint(64) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `logo` varchar(200) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `stadium` varchar(200) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  `coach` varchar(100) DEFAULT NULL,
  `manager` varchar(200) DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  `achievement` varchar(2000) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

# Dump of table awards_prediction
# ------------------------------------------------------------

DROP TABLE IF EXISTS `awards_prediction`;

CREATE TABLE `awards_prediction` (
  `id` bigint(64) NOT NULL AUTO_INCREMENT,
  `MVP` varchar(100) NOT NULL,
  `eastern_champion` varchar(100) NOT NULL,
  `western_champion` varchar(100) NOT NULL,
  `final_champion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table eastern_conference_playoffs_team
# ------------------------------------------------------------

DROP TABLE IF EXISTS `eastern_conference_playoffs_team`;

CREATE TABLE `eastern_conference_playoffs_team` (
  `Team_Name` varchar(100) NOT NULL,
  `Team_Ranking` varchar(100) NOT NULL,
  PRIMARY KEY (`Team_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table every_game_predicted_result
# ------------------------------------------------------------

DROP TABLE IF EXISTS `every_game_predicted_result`;

CREATE TABLE `every_game_predicted_result` (
  `Date` varchar(100) NOT NULL,
  `Start_Time_ET` varchar(100) NOT NULL,
  `Visitor_Team` varchar(100) NOT NULL,
  `Home_Team` varchar(100) NOT NULL,
  `Predicted_Visitor_Score` varchar(100) NOT NULL,
  `Predicted_Home_Score` varchar(100) NOT NULL,
  PRIMARY KEY (`Date`, `Visitor_Team`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table western_conference_playoffs_team
# ------------------------------------------------------------

DROP TABLE IF EXISTS `western_conference_playoffs_team`;

CREATE TABLE `western_conference_playoffs_team` (
  `Team_Name` varchar(100) NOT NULL,
  `Team_Ranking` varchar(100) NOT NULL,
  PRIMARY KEY (`Team_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
