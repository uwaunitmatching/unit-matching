DROP TABLE IF EXISTS `app_units`;
CREATE TABLE `app_units` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uni_id` int(11) NOT NULL,
  `unit_code` varchar(20) DEFAULT NULL,
  `unit_name` varchar(300) DEFAULT NULL,
  `unit_desc` varchar(5000) DEFAULT NULL,
  `unit_text` varchar(400) DEFAULT NULL,
  `ISBN` int(11) DEFAULT NULL,
  `Keywords` varchar(5000) DEFAULT NULL,
  `Positive` varchar(5000) DEFAULT NULL,
  `unit_link` varchar(2084) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30111 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `app_university`;
CREATE TABLE `app_university` (
  `id` int(11) AUTO_INCREMENT,
  `uni_name` varchar(255) NOT NULL,
  `city` varchar(25) DEFAULT NULL,
  `country` varchar(25) DEFAULT NULL,
  `region` varchar(25) DEFAULT NULL,
  `times_ranking` varchar(12) DEFAULT NULL,
  `uni_link` varchar(2084) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=182 DEFAULT CHARSET=utf8;

INSERT INTO `app_university` VALUES (NULL, 'University of Western Australia', 'Perth', 'Australia','Australia', NULL, 'handbooks.uwa.edu.au')