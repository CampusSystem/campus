-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: software_process
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activity`
--

DROP TABLE IF EXISTS `activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activity` (
  `activity_id` decimal(8,0) NOT NULL,
  `activity_name` varchar(20) DEFAULT NULL,
  `activity_des` text,
  `activity_begintime` timestamp NULL DEFAULT NULL,
  `activity_endtime` timestamp NULL DEFAULT NULL,
  `score` decimal(4,0) NOT NULL,
  PRIMARY KEY (`activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity`
--

LOCK TABLES `activity` WRITE;
/*!40000 ALTER TABLE `activity` DISABLE KEYS */;
INSERT INTO `activity` VALUES (1,'class','good class','2019-12-31 16:00:00','2020-04-30 16:00:00',20),(2,'learn','learn hard','2019-12-31 16:00:00','2020-04-30 16:00:00',15),(3,'play','play happy','2019-12-31 16:00:00','2020-04-30 16:00:00',2);
/*!40000 ALTER TABLE `activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `admin_id` decimal(8,0) NOT NULL,
  `admin_username` varchar(20) DEFAULT NULL,
  `admin_password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'Alice','100'),(2,'Cheshire','200'),(3,'White Rabbit','300');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `business`
--

DROP TABLE IF EXISTS `business`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `business` (
  `business_id` decimal(8,0) NOT NULL,
  `admin_id` decimal(8,0) DEFAULT NULL,
  `business_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`business_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business`
--

LOCK TABLES `business` WRITE;
/*!40000 ALTER TABLE `business` DISABLE KEYS */;
INSERT INTO `business` VALUES (1,1,'Clothes'),(2,2,'Smile'),(3,3,'Pocket Watch');
/*!40000 ALTER TABLE `business` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `integral_table`
--

DROP TABLE IF EXISTS `integral_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `integral_table` (
  `user_id` decimal(8,0) NOT NULL,
  `activity_id` decimal(8,0) NOT NULL,
  `itable_id` decimal(10,0) DEFAULT NULL,
  `application_time` timestamp NULL DEFAULT NULL,
  `finish_case` text,
  `application_content` text,
  `application_materials` text,
  `application_state` varchar(255) DEFAULT NULL,
  `note` text,
  PRIMARY KEY (`user_id`,`activity_id`),
  KEY `activity_id_FK1` (`activity_id`),
  CONSTRAINT `activity_id_FK1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`activity_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_id_FK1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='?????????';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `integral_table`
--

LOCK TABLES `integral_table` WRITE;
/*!40000 ALTER TABLE `integral_table` DISABLE KEYS */;
INSERT INTO `integral_table` VALUES (1,1,1,'2019-12-31 16:00:01','1','None','None','complete','exc'),(2,2,2,'2019-12-31 16:00:01','1','None','None','complete','exc'),(3,3,3,'2019-12-31 16:00:01','1','None','None','complete','exc');
/*!40000 ALTER TABLE `integral_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `p_id` decimal(8,0) NOT NULL,
  `admin_id` decimal(8,0) DEFAULT NULL,
  `p_name` varchar(50) DEFAULT NULL,
  `p_description` text,
  `p_price` float DEFAULT NULL,
  `p_place` varchar(256) DEFAULT NULL,
  `p_prodution_date` timestamp NULL DEFAULT NULL,
  `p_validity` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='?';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,1,'dress','pretty dress',1000,'house','2019-12-31 16:00:00','human'),(2,2,'ridicule','A big laugh',233,'tree','2019-12-31 16:00:00','all'),(3,3,'clock','Exquisite clock',888,'hole','2019-12-31 16:00:00','all');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productowner_table`
--

DROP TABLE IF EXISTS `productowner_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `productowner_table` (
  `p_id` decimal(8,0) NOT NULL,
  `business_id` decimal(8,0) NOT NULL,
  `p_number` decimal(8,0) DEFAULT NULL,
  PRIMARY KEY (`p_id`,`business_id`),
  KEY `business_id_PK1` (`business_id`),
  CONSTRAINT `business_id_PK1` FOREIGN KEY (`business_id`) REFERENCES `business` (`business_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `p_id_PK1` FOREIGN KEY (`p_id`) REFERENCES `product` (`p_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productowner_table`
--

LOCK TABLES `productowner_table` WRITE;
/*!40000 ALTER TABLE `productowner_table` DISABLE KEYS */;
INSERT INTO `productowner_table` VALUES (1,1,1),(2,2,2),(3,3,3);
/*!40000 ALTER TABLE `productowner_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publish`
--

DROP TABLE IF EXISTS `publish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `publish` (
  `admin_id` decimal(8,0) NOT NULL,
  `activity_id` decimal(8,0) NOT NULL,
  `publish_time` timestamp NULL DEFAULT NULL,
  `statement` text,
  PRIMARY KEY (`admin_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `publish_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`admin_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `publish_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`activity_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='?????';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publish`
--

LOCK TABLES `publish` WRITE;
/*!40000 ALTER TABLE `publish` DISABLE KEYS */;
INSERT INTO `publish` VALUES (3,1,'2019-12-31 16:00:00','JUST TAKING'),(3,2,'2019-12-31 16:00:00','JUST DOING'),(3,3,'2019-12-31 16:00:00','JUST PLAYING');
/*!40000 ALTER TABLE `publish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `p_id` decimal(8,0) NOT NULL,
  `user_id` decimal(8,0) NOT NULL,
  `tr_id` decimal(10,0) DEFAULT NULL,
  `tr_time` timestamp NULL DEFAULT NULL,
  `state` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`p_id`,`user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `product` (`p_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (2,1,1,'2020-01-01 16:00:00',1),(2,2,2,'2020-01-01 16:00:00',1),(2,3,3,'2020-01-01 16:00:00',1);
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` decimal(8,0) NOT NULL,
  `admin_id` decimal(8,0) DEFAULT NULL,
  `user_name` varchar(20) DEFAULT NULL,
  `user_password` varchar(16) DEFAULT NULL,
  `user_major` varchar(20) DEFAULT NULL,
  `user_class` varchar(20) DEFAULT NULL,
  `score` decimal(8,0) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,1,'Apple','ple','fruit','fruit1701',1000),(2,1,'Beaf','eaf','meat','meat1701',1000),(3,1,'Carrot','rot','vegetablr','vegetable1701',1000);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-19 22:00:11
