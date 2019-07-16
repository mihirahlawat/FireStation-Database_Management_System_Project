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
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `staff` (
  `STAFF_ID` int(11) NOT NULL AUTO_INCREMENT,
  `F_NAME` varchar(45) NOT NULL,
  `M_NAME` varchar(45) DEFAULT NULL,
  `L_NAME` varchar(45) NOT NULL,
  `GENDER` varchar(45) NOT NULL,
  `DOB` varchar(45) NOT NULL,
  `STAFF_CONTACT` varchar(45) NOT NULL,
  `STAFF_ADDR` varchar(100) NOT NULL,
  `STAFF_DESIG` varchar(45) NOT NULL,
  `DOJ` varchar(45) NOT NULL,
  `DOL` varchar(45) DEFAULT NULL,
  `STAFF_STATION` varchar(45) DEFAULT NULL,
  `SALARY` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`STAFF_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (99,'Rajyavardhan','Singh','Rathore','Male','25-07-1965','9876543210','Keshav Puram, Delhi','Station Head','02-10-1996','-','10001','15 Lac'),(100,'Jai','-','Bhagwan','Male','20-08-1974','9818803321','Ashok Vihar, Delhi','Station Head','16-08-1999','-','10002','14 Lac'),(101,'Yogesh','-','Singh','Male','04-01-1968','9012345678','Rohini, Delhi','Station Head','12-12-1998','-','10003','14 Lac'),(102,'Rakesh','-','Kumar','Male','25-12-1986','9784561230','Pitampura, Delhi','Driver Engineer','17-12-2005','','10001','10 Lac'),(103,'Deepak','-','Chaurasia','Male','05-01-1992','9869786920','Rohini, Delhi','Firefighter','15-09-2013','-','10001','6 Lac'),(104,'Mihir','-','Ahlawat','Male','18-11-1997','9650454505','Ashok Vihar, Delhi','Intern','30-05-2019','30-07-2019','10001','15k (per month)'),(105,'Swapnil','-','Jain','Male','19-04-1986','9638527410','Rohini, Delhi','Officer','01-07-2009','-','10004','10 Lac');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-16 23:15:54
