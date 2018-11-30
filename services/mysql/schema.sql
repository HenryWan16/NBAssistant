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
  `height` decimal(11,2) DEFAULT NULL,
  `weight` decimal(11,2) DEFAULT NULL,
  `points` decimal(11,2) DEFAULT NULL,
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
  `start_time_ET` timestamp NULL DEFAULT NULL,
  `visitor` varchar(100) DEFAULT NULL,
  `home` varchar(100) DEFAULT NULL,
  `teamA_id` bigint(64) DEFAULT NULL,
  `teamB_id` bigint(64) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `start_time_ET` (`start_time_ET`)
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
  KEY `team_id` (`team_id`),
  KEY `player_id` (`player_id`)
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




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
