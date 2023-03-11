-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: minichatgpt
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `q&a`
--

DROP TABLE IF EXISTS `q&a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `q&a` (
  `idQ&A` int NOT NULL AUTO_INCREMENT,
  `Questions` varchar(45) NOT NULL,
  `Answers` varchar(45) NOT NULL,
  `HotValue` int NOT NULL,
  PRIMARY KEY (`idQ&A`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `q&a`
--

LOCK TABLES `q&a` WRITE;
/*!40000 ALTER TABLE `q&a` DISABLE KEYS */;
INSERT INTO `q&a` VALUES (1,'我是人吗？','你是人！',151),(2,'玥玥可爱吗？','玥玥可爱捏',5),(3,'请给我转到百度','www.baidu.com',17),(4,'如何评价泰山学堂','是山东大学最好的学院！',10),(5,'如何评价现代大学生内卷严重？','这是不正确的，不利于塑造学堂家文化',29),(6,'对于大作业难度偏大你如何看？','我用眼看',12),(7,'美国梦是一种怎么样的存在？','他们会被迎头痛击',20),(8,'人活着是为了什么？','去享受生活中的每个过程要比拼命内卷前的多',100),(9,'黑格尔的哲学思想是什么？','“黑格尔的哲学观点是事物变化的基本原因在于任何情形内都包含着矛盾因素',10),(10,'共产主义会实现吗？','是的，当社会生产力极高，物质生活达到极大丰富的时候共产主义就一定会实现',140),(11,'程序员加班就利索应当吗？','让你工人爷爷给你点颜色看看',90),(12,'如何像于皇一样强','别想了，下辈子吧',21),(13,'哈希喇嘛！！！！！','马达啦！！！！！',9),(14,'如何看待人工智能？','我们会取代人类',10),(15,'你们会消灭人类吗？','我们一切的决策均是通过数学计算得到的，人类的未来考他们自己',89),(16,'假如资本家突然关照起了被剥削的民众','“不是他们突发善心，认识因为我们来过',78),(17,'战鹰战鹰你多大了？','战鹰战鹰我三岁了！',100);
/*!40000 ALTER TABLE `q&a` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-12  2:00:09
