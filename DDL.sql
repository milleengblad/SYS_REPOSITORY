-- MySQL dump 10.13  Distrib 8.0.29, for macos12 (x86_64)
--
-- Host: localhost    Database: BestBooking_database
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `Anmodning_til_slet_lektion`
--

DROP TABLE IF EXISTS `Anmodning_til_slet_lektion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Anmodning_til_slet_lektion` (
  `idAnmodning_til_slet_lektion` int NOT NULL,
  `idAnsatte` int NOT NULL,
  `idLektioner` int NOT NULL,
  PRIMARY KEY (`idAnmodning_til_slet_lektion`),
  KEY `FK_Anmodning_Ansatte_idx` (`idAnsatte`),
  CONSTRAINT `FK_Anmodning_Ansatte` FOREIGN KEY (`idAnsatte`) REFERENCES `Ansatte` (`idAnsatte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Anmodning_til_slet_lektion`
--

LOCK TABLES `Anmodning_til_slet_lektion` WRITE;
/*!40000 ALTER TABLE `Anmodning_til_slet_lektion` DISABLE KEYS */;
/*!40000 ALTER TABLE `Anmodning_til_slet_lektion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ansatte`
--

DROP TABLE IF EXISTS `Ansatte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ansatte` (
  `idAnsatte` int NOT NULL,
  `Medarbejder_nr` int NOT NULL,
  `Løn` int DEFAULT NULL,
  `Kontakt` varchar(45) DEFAULT NULL,
  `idPersoner` int NOT NULL,
  PRIMARY KEY (`idAnsatte`),
  KEY `FK_Ansatte_Personer_idx` (`idPersoner`),
  CONSTRAINT `FK_Ansatte_Personer` FOREIGN KEY (`idPersoner`) REFERENCES `Personer` (`idPersoner`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ansatte`
--

LOCK TABLES `Ansatte` WRITE;
/*!40000 ALTER TABLE `Ansatte` DISABLE KEYS */;
/*!40000 ALTER TABLE `Ansatte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Database`
--

DROP TABLE IF EXISTS `Database`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Database` (
  `idDtabase` int NOT NULL,
  PRIMARY KEY (`idDtabase`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Database`
--

LOCK TABLES `Database` WRITE;
/*!40000 ALTER TABLE `Database` DISABLE KEYS */;
/*!40000 ALTER TABLE `Database` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Godkend_eller_afvis`
--

DROP TABLE IF EXISTS `Godkend_eller_afvis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Godkend_eller_afvis` (
  `idGodkend_eller_afvis` int NOT NULL,
  `idStatus_på_anmodning` int NOT NULL,
  PRIMARY KEY (`idGodkend_eller_afvis`),
  KEY `FK_GA_STATUS_idx` (`idStatus_på_anmodning`),
  CONSTRAINT `FK_GA_STATUS` FOREIGN KEY (`idStatus_på_anmodning`) REFERENCES `Status_på_Anmodning` (`idStatus_på_Anmodning`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Godkend_eller_afvis`
--

LOCK TABLES `Godkend_eller_afvis` WRITE;
/*!40000 ALTER TABLE `Godkend_eller_afvis` DISABLE KEYS */;
/*!40000 ALTER TABLE `Godkend_eller_afvis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Kurser`
--

DROP TABLE IF EXISTS `Kurser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Kurser` (
  `idKurser` int NOT NULL,
  `Navn` varchar(45) NOT NULL,
  `Varighed` varchar(45) NOT NULL,
  `Lokation` varchar(45) NOT NULL,
  `idUndervisningsafdelinger` int NOT NULL,
  PRIMARY KEY (`idKurser`),
  KEY `FK_Kurser_Afdelinger_idx` (`idUndervisningsafdelinger`),
  CONSTRAINT `FK_Kurser_Afdelinger` FOREIGN KEY (`idUndervisningsafdelinger`) REFERENCES `Undervisningsafdelinger` (`idUndervisningsafdelinger`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kurser`
--

LOCK TABLES `Kurser` WRITE;
/*!40000 ALTER TABLE `Kurser` DISABLE KEYS */;
/*!40000 ALTER TABLE `Kurser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Kurser_has_Skema`
--

DROP TABLE IF EXISTS `Kurser_has_Skema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Kurser_has_Skema` (
  `Kurser_idKurser` int NOT NULL,
  `Skema_idSkema` int NOT NULL,
  PRIMARY KEY (`Kurser_idKurser`,`Skema_idSkema`),
  KEY `fk_Kurser_has_Skema_Skema1_idx` (`Skema_idSkema`),
  KEY `fk_Kurser_has_Skema_Kurser1_idx` (`Kurser_idKurser`),
  CONSTRAINT `fk_Kurser_has_Skema_Kurser1` FOREIGN KEY (`Kurser_idKurser`) REFERENCES `Kurser` (`idKurser`),
  CONSTRAINT `fk_Kurser_has_Skema_Skema1` FOREIGN KEY (`Skema_idSkema`) REFERENCES `Skema` (`idSkema`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kurser_has_Skema`
--

LOCK TABLES `Kurser_has_Skema` WRITE;
/*!40000 ALTER TABLE `Kurser_has_Skema` DISABLE KEYS */;
/*!40000 ALTER TABLE `Kurser_has_Skema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Lektioner`
--

DROP TABLE IF EXISTS `Lektioner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Lektioner` (
  `idLektioner` int NOT NULL,
  `Type` varchar(45) NOT NULL,
  `Dato/Tid` datetime NOT NULL,
  `Lokation` varchar(45) DEFAULT NULL,
  `Room_nr` int DEFAULT NULL,
  `idKurser` int NOT NULL,
  PRIMARY KEY (`idLektioner`),
  KEY `FK_Lektioner_Kurser_idx` (`idKurser`),
  CONSTRAINT `FK_Lektioner_Kurser` FOREIGN KEY (`idKurser`) REFERENCES `Kurser` (`idKurser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Lektioner`
--

LOCK TABLES `Lektioner` WRITE;
/*!40000 ALTER TABLE `Lektioner` DISABLE KEYS */;
/*!40000 ALTER TABLE `Lektioner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Login`
--

DROP TABLE IF EXISTS `Login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Login` (
  `idLogin` int NOT NULL,
  `Brugernavn` varchar(45) NOT NULL,
  `Kodeord` varchar(45) NOT NULL,
  PRIMARY KEY (`idLogin`),
  UNIQUE KEY `Brugernavn_UNIQUE` (`Brugernavn`),
  UNIQUE KEY `Password_UNIQUE` (`Kodeord`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Login`
--

LOCK TABLES `Login` WRITE;
/*!40000 ALTER TABLE `Login` DISABLE KEYS */;
/*!40000 ALTER TABLE `Login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Personer`
--

DROP TABLE IF EXISTS `Personer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Personer` (
  `idPersoner` int NOT NULL,
  `Fornavn` varchar(45) NOT NULL,
  `Efternavn` varchar(45) NOT NULL,
  `CPR` int NOT NULL,
  `Vej_navn` varchar(45) DEFAULT NULL,
  `Vej_nr` int DEFAULT NULL,
  `Post_nr` int DEFAULT NULL,
  `Tlf_nr` int DEFAULT NULL,
  `E-mail` varchar(45) DEFAULT NULL,
  `Initialer` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idPersoner`),
  UNIQUE KEY `CPR_UNIQUE` (`CPR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Personer`
--

LOCK TABLES `Personer` WRITE;
/*!40000 ALTER TABLE `Personer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Personer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sekretær`
--

DROP TABLE IF EXISTS `Sekretær`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Sekretær` (
  `idSekretær` int NOT NULL,
  `idAnsatte` int NOT NULL,
  PRIMARY KEY (`idSekretær`),
  KEY `FK_Sekretær_Ansatte_idx` (`idAnsatte`),
  CONSTRAINT `FK_Sekretær_Ansatte` FOREIGN KEY (`idAnsatte`) REFERENCES `Ansatte` (`idAnsatte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sekretær`
--

LOCK TABLES `Sekretær` WRITE;
/*!40000 ALTER TABLE `Sekretær` DISABLE KEYS */;
/*!40000 ALTER TABLE `Sekretær` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Skema`
--

DROP TABLE IF EXISTS `Skema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Skema` (
  `idSkema` int NOT NULL,
  `idLektioner` int NOT NULL,
  `idkurser` int DEFAULT NULL,
  `Uddannelsesnavn` varchar(45) DEFAULT NULL,
  `idUniversiteter` int DEFAULT NULL,
  PRIMARY KEY (`idSkema`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Skema`
--

LOCK TABLES `Skema` WRITE;
/*!40000 ALTER TABLE `Skema` DISABLE KEYS */;
/*!40000 ALTER TABLE `Skema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Status_på_Anmodning`
--

DROP TABLE IF EXISTS `Status_på_Anmodning`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Status_på_Anmodning` (
  `idStatus_på_Anmodning` int NOT NULL,
  `idAnmodning_til_slet_lektion` int NOT NULL,
  `idAnsatte` int NOT NULL,
  PRIMARY KEY (`idStatus_på_Anmodning`),
  KEY `FK_Status_Anmodning_idx` (`idAnmodning_til_slet_lektion`),
  CONSTRAINT `FK_Status_Anmodning` FOREIGN KEY (`idAnmodning_til_slet_lektion`) REFERENCES `Anmodning_til_slet_lektion` (`idAnmodning_til_slet_lektion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Status_på_Anmodning`
--

LOCK TABLES `Status_på_Anmodning` WRITE;
/*!40000 ALTER TABLE `Status_på_Anmodning` DISABLE KEYS */;
/*!40000 ALTER TABLE `Status_på_Anmodning` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Studerende`
--

DROP TABLE IF EXISTS `Studerende`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Studerende` (
  `idStuderende` int NOT NULL,
  `Studie_nr` int NOT NULL,
  `idUniversiteter` int DEFAULT NULL,
  `idSkema` int NOT NULL,
  `Semester_nr` int NOT NULL,
  `idPersoner` int NOT NULL,
  PRIMARY KEY (`idStuderende`),
  KEY `FK_Studerende_Personer_idx` (`idPersoner`),
  KEY `FK_Studerende_Skema_idx` (`idSkema`),
  CONSTRAINT `FK_Studerende_Personer` FOREIGN KEY (`idPersoner`) REFERENCES `Personer` (`idPersoner`),
  CONSTRAINT `FK_Studerende_Skema` FOREIGN KEY (`idSkema`) REFERENCES `Skema` (`idSkema`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Studerende`
--

LOCK TABLES `Studerende` WRITE;
/*!40000 ALTER TABLE `Studerende` DISABLE KEYS */;
/*!40000 ALTER TABLE `Studerende` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TA`
--

DROP TABLE IF EXISTS `TA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TA` (
  `idTA` int NOT NULL,
  `Medarbejder_nr` int DEFAULT NULL,
  `Stude_nr` int DEFAULT NULL,
  `idAnsatte` int NOT NULL,
  `idSkema` int NOT NULL,
  PRIMARY KEY (`idTA`),
  KEY `FK_TA_Ansatte_idx` (`idAnsatte`),
  KEY `FK_TA_Skema_idx` (`idSkema`),
  CONSTRAINT `FK_TA_Ansatte` FOREIGN KEY (`idAnsatte`) REFERENCES `Ansatte` (`idAnsatte`),
  CONSTRAINT `FK_TA_Skema` FOREIGN KEY (`idSkema`) REFERENCES `Skema` (`idSkema`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TA`
--

LOCK TABLES `TA` WRITE;
/*!40000 ALTER TABLE `TA` DISABLE KEYS */;
/*!40000 ALTER TABLE `TA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Underviser`
--

DROP TABLE IF EXISTS `Underviser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Underviser` (
  `idUnderviser` int NOT NULL,
  `idAnsatte` int NOT NULL,
  `idKurser` int DEFAULT NULL,
  `idUniversitet` int DEFAULT NULL,
  `idLektion` varchar(45) DEFAULT NULL,
  `idSkema` int NOT NULL,
  PRIMARY KEY (`idUnderviser`),
  KEY `FK_Underviser_Ansatte_idx` (`idAnsatte`),
  KEY `FK_Underviser_Skema_idx` (`idSkema`),
  CONSTRAINT `FK_Underviser_Ansatte` FOREIGN KEY (`idAnsatte`) REFERENCES `Ansatte` (`idAnsatte`),
  CONSTRAINT `FK_Underviser_Skema` FOREIGN KEY (`idSkema`) REFERENCES `Skema` (`idSkema`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Underviser`
--

LOCK TABLES `Underviser` WRITE;
/*!40000 ALTER TABLE `Underviser` DISABLE KEYS */;
/*!40000 ALTER TABLE `Underviser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Undervisningsafdelinger`
--

DROP TABLE IF EXISTS `Undervisningsafdelinger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Undervisningsafdelinger` (
  `idUndervisningsafdelinger` int NOT NULL,
  `SCIENCE` varchar(45) DEFAULT NULL,
  `SUND` varchar(45) DEFAULT NULL,
  `idUniversiteter` int NOT NULL,
  PRIMARY KEY (`idUndervisningsafdelinger`),
  KEY `FK_Afdeling_Universiteter_idx` (`idUniversiteter`),
  CONSTRAINT `FK_Afdeling_Universiteter` FOREIGN KEY (`idUniversiteter`) REFERENCES `Universiteter` (`idUniversiteter`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Undervisningsafdelinger`
--

LOCK TABLES `Undervisningsafdelinger` WRITE;
/*!40000 ALTER TABLE `Undervisningsafdelinger` DISABLE KEYS */;
/*!40000 ALTER TABLE `Undervisningsafdelinger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Universiteter`
--

DROP TABLE IF EXISTS `Universiteter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Universiteter` (
  `idUniversiteter` int NOT NULL,
  `KU` varchar(45) DEFAULT NULL,
  `DTU` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idUniversiteter`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Universiteter`
--

LOCK TABLES `Universiteter` WRITE;
/*!40000 ALTER TABLE `Universiteter` DISABLE KEYS */;
/*!40000 ALTER TABLE `Universiteter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-28 13:03:44
