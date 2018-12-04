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
  `manager` varchar(100) DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  `achievement` varchar(2000) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

# Dump of table teams_extra
# ------------------------------------------------------------

DROP TABLE IF EXISTS `teams_extra`;

CREATE TABLE `teams_extra` (
  `id` bigint(64) NOT NULL AUTO_INCREMENT,
  `team_name` VARCHAR(100) NOT NULL,
	`stadium` VARCHAR(100) NOT NULL,
	`owner` VARCHAR(100) NOT NULL,
	`coach` VARCHAR(100) NOT NULL,
	`manager` VARCHAR(100) NOT NULL,
	`achievement` VARCHAR(100) DEFAULT 'no achievement so far',
	PRIMARY KEY(`id`, `team_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

insert into teams_extra values (1, 'Los Angeles Lakers', 'Staples Center','Buss Family Trusts ','Luke Walton','Rob Pelinka','Sixteen times NBA champion');
insert into teams_extra values (2, 'Atlanta Hawks', 'State Farm Arena','Stephen Curry','Lloyd Pierce','Travis Schlenk','One time NBA champion');
insert into teams_extra values (3, 'Boston Celtics', 'TD Garden','Boston Basketball Partners','Brad Stevens','Danny Ainge','Seventeen time NBA champion, all time leader');
insert into teams_extra values (4, 'Brooklyn Nets', 'Barclays Center','Mikhail Prokhorov','Kenny Atkinson','Sean Marks','Two times NBA champion');
insert into teams_extra values (5, 'Charlotte Hornets', 'Spectrum Center','Michael Jordan','James Borrego','Mitch Kupchak','Ten times playoffs appearances');
insert into teams_extra values (6, 'Chicago Bulls', 'United Center','Jerry Reinsdorf','Jim Boylen','Gar Forman','Six times NBA champion');
insert into teams_extra values (7, 'Cleveland Cavaliers', 'Quicken Loans Arena','Dan Gilbert ','Larry Drew','Koby Altman','One time NBA champion');
insert into teams_extra values (8, 'Dallas Mavericks', 'American Airlines Center','Mark Cuban','Rick Carlisle','Donnie Nelson','One time NBA champion');
insert into teams_extra values (9, 'Denver Nuggets', 'Pepsi Center','Ann Walton Kroenke','Michael Malone','Art¨±ras Karnisovas', 'Thirty-three time playoffs appearances');
insert into teams_extra values (10, 'Detroit Pistons', 'Little Caesars Arena','Tom Gores','Dwane Casey','Ed Stefanski','Three times NBA champion');
insert into teams_extra values (11, 'Golden State Warriors', 'Oracle Arena','Joe Lacob','Steve Kerr','Bob Myers', 'Six times NBA champion');
insert into teams_extra values (12, 'Houston Rockets', 'Toyota Center','Tilman Fertitta','Mike DAntoni','Daryl Morey','Two times NBA champion');
insert into teams_extra values (13, 'Indiana Pacers', 'Bankers Life Fieldhouse','Herbert Simon','Nate McMillan','Chad Buchanan', 'Three times NBA champion');
insert into teams_extra values (14, 'Los Angeles Clippers', 'Staples Center','	Steve Ballmer','Doc Rivers','Michael Winger','Thirteen times playoffs appearances');
insert into teams_extra values (15, 'Memphis Grizzlies', '	FedExForum','Memphis Basketball, LLC','J. B. Bickerstaff','Chris Wallace','Ten times playoffs appearances');
insert into teams_extra values (16, 'Miami Heat', 'American Airlines Arena','Micky Arison','Erik Spoelstra','Andy Elisburg','Three times NBA champion');
insert into teams_extra values (17, 'Milwaukee Bucks', 'Fiserv Forum','Wes Edens','Mike Budenholzer','Jon Horst','One time NBA champion');
insert into teams_extra values (18, 'New Orleans Pelicans', 'Smoothie King Center','Gayle Benson','Alvin Gentry','Dell Demps','Seven time playoffs appearances');
insert into teams_extra values (19, 'New York Knicks', 'Madison Square Garden','Madison Square Garden Company','David Fizdale','Scott Perry','Two times NBA champion');
insert into teams_extra values (20, 'Oklahoma City Thunder', 'Chesapeake Energy Arena','Professional Basketball Club LLC','Billy Donovan','Sam Presti','One time NBA champion');
insert into teams_extra values (21, 'Orlando Magic', 'Amway Center','RDV Sports, Inc.','Steve Clifford','John Hammond','Forteen times playoffs appearances');
insert into teams_extra values (22, 'Philadelphia 76ers', 'Wells Fargo Center','Joshua Harris','Brett Brown','Elton Brand','Three Time NBA champion');
insert into teams_extra values (23, 'Phoenix Suns', 'Talking Stick Resort Arena','	Robert Sarver','Igor Kokoskov','Trevor Bukstein','Twenty-nine times playoffs appearances');
insert into teams_extra values (24, 'Portland Trail Blazers', 'Moda Center','Estate of Paul Allen','Terry Stotts','Neil Olshey','One time NBA champion');
insert into teams_extra values (25, 'Sacramento Kings', 'Golden 1 Center','Vivek Ranadive','Dave Joerger','Vlade Divac','One time NBA champion');
insert into teams_extra values (26, 'San Antonio Spurs', 'AT&T Center','Spurs Sports & Entertainment','Gregg Popovich','R. C. Buford','Five time NBA champion');
insert into teams_extra values (27, 'Toronto Raptors', 'Scotiabank Arena','Maple Leaf Sports & Entertainment','Nick Nurse','Bobby Webster','Ten times playoffs appearances');
insert into teams_extra values (28, 'Utah Jazz', 'Vivint Smart Home Arena','Jazz Basketball Investors, Inc','Quin Snyder','Dennis Lindsey','Twenty-nine times playoffs appearances');
insert into teams_extra values (29, 'Washington Wizards', 'Capital One Arena','Monumental Sports & Entertainment','Scott Brooks','Ernie Grunfeld','One time NBA champion');
insert into teams_extra values (30, 'Minnesota Timberwolves', 'Target Center','Glen Taylor','Tom Thibodeau','Scott Layden','Nine time playoffs appearances');

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
