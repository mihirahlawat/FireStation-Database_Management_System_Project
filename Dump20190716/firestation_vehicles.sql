-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: firestation
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vehicles`
--

DROP TABLE IF EXISTS `vehicles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `vehicles` (
  `VEHICLE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `VEHICLE_NUM` varchar(45) NOT NULL,
  `VEHICLE_STATION` varchar(45) NOT NULL,
  `VEHICLE_TYPE` varchar(45) NOT NULL,
  `MODEL_NO` varchar(45) NOT NULL,
  `VEHICLE_STATUS` varchar(45) NOT NULL,
  `WATER_CAP` varchar(45) DEFAULT NULL,
  `PURCHASE` varchar(45) NOT NULL,
  PRIMARY KEY (`VEHICLE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicles`
--

LOCK TABLES `vehicles` WRITE;
/*!40000 ALTER TABLE `vehicles` DISABLE KEYS */;
INSERT INTO `vehicles` VALUES (70,'DL-8C-3884','10001','Fire Brigade','38xc4','In Use','4000','18-11-2015'),(71,'DL-5S-9366','10002','Fire Brigade','38xc4','In Use','4000','18-11-2015'),(72,'DL-6C-1220','10003','Fire Brigade','38xc4','In Use','4000','18-11-2015'),(73,'DL-8Q-9842','10004','Fire Brigade','38xc4','In Use','4000','18-11-2015'),(74,'DL-8X-8290','10005','Fire Brigade','38xc4','Not in use','4000','18-11-2015'),(75,'DL-8C-1120','10005','Fire Brigade','38xc4','In Use','4000','02-02-2019'),(76,'X-QWER','10001','Helicopter','F210 R/C','In Use','2100','24-03-2017'),(77,'DL-8X-9663','10001','Light 4-wheeler','Maruti Swift','In Use','0','25-12-2016'),(78,'DL-8C-1324','10004','Light 4-wheeler','Maruti Zen','In Use','0','23-05-2005');
/*!40000 ALTER TABLE `vehicles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-16 23:15:52
