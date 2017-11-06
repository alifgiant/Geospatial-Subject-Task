-- MySQL dump 10.16  Distrib 10.1.13-MariaDB, for Win32 (AMD64)
--
-- Host: localhost    Database: ta_db
-- ------------------------------------------------------
-- Server version	10.1.13-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `region`
--

DROP TABLE IF EXISTS `region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `region` (
  `nameRegion` varchar(10) NOT NULL,
  `titikX` double(10,5) NOT NULL,
  `titikY` double(10,5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region`
--

LOCK TABLES `region` WRITE;
/*!40000 ALTER TABLE `region` DISABLE KEYS */;
INSERT INTO `region` VALUES ('R0',1.00000,877.51034),('R0',119.12406,917.42813),('R0',71.22854,1000.00000),('R0',1.00000,1000.00000),('R1',119.12406,917.42813),('R1',165.47962,933.09311),('R1',109.38077,1000.00000),('R1',71.22854,1000.00000),('R2',165.47962,933.09311),('R2',363.46939,1000.00000),('R2',178.93575,1000.00000),('R3',1.00000,115.26389),('R3',47.52255,346.58435),('R3',1.00000,295.05566),('R4',47.52255,346.58435),('R4',71.59786,466.29215),('R4',1.00000,419.63090),('R4',1.00000,307.92346),('R5',71.59786,466.29215),('R5',78.09108,498.57788),('R5',1.00000,484.57220),('R5',1.00000,419.63090),('R6',78.09108,498.57788),('R6',90.21429,558.85714),('R6',77.20374,572.81790),('R6',1.00000,528.29296),('R6',1.00000,484.57220),('R7',90.21429,558.85714),('R7',93.72094,576.29300),('R7',77.20374,572.81790),('R8',93.72094,576.29300),('R8',95.12837,583.29104),('R8',83.45467,576.47024),('R9',95.12837,583.29104),('R9',151.20561,862.11954),('R9',119.12406,917.42813),('R9',1.00000,877.51034),('R9',1.00000,654.58708),('R9',73.64211,576.63964),('R10',151.20561,862.11954),('R10',165.47962,933.09311),('R10',119.12406,917.42813),('R11',77.20374,572.81790),('R11',83.45467,576.47024),('R11',73.64211,576.63964),('R12',95.12837,583.29104),('R12',257.80549,678.34134),('R12',151.20561,862.11954),('R13',257.80549,678.34134),('R13',339.20253,725.90066),('R13',165.47962,933.09311),('R13',151.20561,862.11954),('R14',339.20253,725.90066),('R14',446.68890,788.70366),('R14',383.30000,1000.00000),('R14',363.46939,1000.00000),('R14',165.47962,933.09311),('R15',446.68890,788.70366),('R15',555.92981,852.53182),('R15',661.95620,1000.00000),('R15',637.45729,1000.00000),('R16',555.92981,852.53182),('R16',808.31933,1000.00000),('R16',661.95620,1000.00000),('R17',47.52255,346.58435),('R17',165.87424,477.67146),('R17',136.50125,509.18967),('R17',71.59786,466.29215),('R18',165.87424,477.67146),('R18',205.67704,521.75732),('R18',136.50125,509.18967),('R19',205.67704,521.75732),('R19',252.44049,573.55282),('R19',234.35429,573.86507),('R19',136.50125,509.18967),('R20',252.44049,573.55282),('R20',279.90242,603.96984),('R20',234.35429,573.86507),('R21',279.90242,603.96984),('R21',292.71366,618.15965),('R21',93.72094,576.29300),('R21',234.35429,573.86507),('R22',292.71366,618.15965),('R22',325.66548,654.65731),('R22',279.78222,640.45345),('R23',325.66548,654.65731),('R23',363.65604,696.73591),('R23',339.20253,725.90066),('R23',257.80549,678.34134),('R23',279.78222,640.45345),('R24',363.65604,696.73591),('R24',446.68890,788.70366),('R24',339.20253,725.90066),('R25',1.00000,556.78517),('R25',27.54972,562.37104),('R25',73.64211,576.63964),('R25',1.00000,577.89376),('R26',27.54972,562.37104),('R26',77.20374,572.81790),('R26',73.64211,576.63964),('R27',292.71366,618.15965),('R27',305.41432,620.83178),('R27',383.83812,672.66554),('R27',325.66548,654.65731),('R28',305.41432,620.83178),('R28',401.98821,641.15025),('R28',406.86469,645.20266),('R28',383.83812,672.66554),('R29',401.98821,641.15025),('R29',404.30093,641.63682),('R29',406.86469,645.20266),('R30',404.30093,641.63682),('R30',409.02173,642.63005),('R30',406.86469,645.20266),('R31',409.02173,642.63005),('R31',485.67293,658.75691),('R31',473.20123,700.32925),('R31',406.86469,645.20266),('R32',485.67293,658.75691),('R32',1000.00000,766.96768),('R32',1000.00000,863.40783),('R32',473.20123,700.32925),('R33',363.65604,696.73591),('R33',383.83812,672.66554),('R33',465.33990,726.53367),('R33',446.68890,788.70366),('R34',409.02173,642.63005),('R34',470.09091,569.79524),('R34',510.17663,577.07790),('R34',485.67293,658.75691),('R35',470.09091,569.79524),('R35',535.91214,491.29286),('R35',512.58150,569.06167),('R36',535.91214,491.29286),('R36',947.00385,1.00000),('R36',1000.00000,1.00000),('R36',1000.00000,560.64675),('R36',512.58150,569.06167),('R37',279.90242,603.96984),('R37',295.11300,614.02319),('R37',292.71366,618.15965),('R38',295.11300,614.02319),('R38',305.41432,620.83178),('R38',292.71366,618.15965),('R39',465.33990,726.53367),('R39',657.83326,853.76104),('R39',833.80981,1000.00000),('R39',808.31933,1000.00000),('R39',555.92981,852.53182),('R40',657.83326,853.76104),('R40',879.09091,1000.00000),('R40',833.80981,1000.00000),('R41',1.00000,80.70051),('R41',233.91828,404.65791),('R41',183.06667,459.22340),('R41',47.52255,346.58435),('R41',1.00000,115.26389),('R42',233.91828,404.65791),('R42',335.00298,545.25287),('R42',273.04483,533.99650),('R42',183.06667,459.22340),('R43',335.00298,545.25287),('R43',354.08830,571.79794),('R43',319.25680,572.39929),('R44',354.08830,571.79794),('R44',404.30093,641.63682),('R44',401.98821,641.15025),('R44',319.25680,572.39929),('R45',406.86469,645.20266),('R45',438.85505,689.69687),('R45',383.83812,672.66554),('R46',438.85505,689.69687),('R46',465.33990,726.53367),('R46',383.83812,672.66554),('R47',78.09108,498.57788),('R47',136.50125,509.18967),('R47',90.21429,558.85714),('R48',205.67704,521.75732),('R48',273.04483,533.99650),('R48',319.25680,572.39929),('R48',252.44049,573.55282),('R49',335.00298,545.25287),('R49',470.09091,569.79524),('R49',354.08830,571.79794),('R50',510.17663,577.07790),('R50',1000.00000,666.06755),('R50',1000.00000,766.96768),('R50',485.67293,658.75691),('R51',1.00000,554.15217),('R51',27.54972,562.37104),('R51',1.00000,556.78517),('R52',95.12837,583.29104),('R52',279.78222,640.45345),('R52',257.80549,678.34134),('R53',438.85505,689.69687),('R53',473.20123,700.32925),('R53',465.33990,726.53367),('R54',473.20123,700.32925),('R54',657.83326,853.76104),('R54',465.33990,726.53367),('R55',510.17663,577.07790),('R55',512.58150,569.06167),('R55',1000.00000,560.64675),('R55',1000.00000,666.06755),('R56',535.91214,491.29286),('R56',683.00000,1.00000),('R56',947.00385,1.00000),('R57',165.87424,477.67146),('R57',183.06667,459.22340),('R57',273.04483,533.99650),('R57',205.67704,521.75732),('R58',233.91828,404.65791),('R58',610.10209,1.00000),('R58',650.69490,1.00000),('R58',335.00298,545.25287),('R59',295.11300,614.02319),('R59',319.25680,572.39929),('R59',401.98821,641.15025),('R59',305.41432,620.83178),('R60',1000.00000,863.40783),('R60',1000.00000,1000.00000),('R60',879.09091,1000.00000),('R60',657.83326,853.76104),('R60',473.20123,700.32925),('R61',1.00000,80.70051),('R61',1.00000,1.00000),('R61',610.10209,1.00000),('R61',233.91828,404.65791),('R62',1.00000,307.92346),('R62',1.00000,295.05566),('R62',47.52255,346.58435),('R63',1.00000,554.15217),('R63',1.00000,528.29296),('R63',77.20374,572.81790),('R63',27.54972,562.37104),('R64',1.00000,654.58708),('R64',1.00000,577.89376),('R64',73.64211,576.63964),('R65',178.93575,1000.00000),('R65',109.38077,1000.00000),('R65',165.47962,933.09311),('R66',637.45729,1000.00000),('R66',383.30000,1000.00000),('R66',446.68890,788.70366),('R67',650.69490,1.00000),('R67',683.00000,1.00000),('R67',535.91214,491.29286),('R67',470.09091,569.79524),('R67',335.00298,545.25287),('R68',78.09108,498.57788),('R68',71.59786,466.29215),('R68',136.50125,509.18967),('R69',93.72094,576.29300),('R69',90.21429,558.85714),('R69',136.50125,509.18967),('R69',234.35429,573.86507),('R70',95.12837,583.29104),('R70',93.72094,576.29300),('R70',292.71366,618.15965),('R70',279.78222,640.45345),('R71',83.45467,576.47024),('R71',77.20374,572.81790),('R71',93.72094,576.29300),('R72',83.45467,576.47024),('R72',95.12837,583.29104),('R72',73.64211,576.63964),('R73',555.92981,852.53182),('R73',446.68890,788.70366),('R73',465.33990,726.53367),('R74',165.87424,477.67146),('R74',47.52255,346.58435),('R74',183.06667,459.22340),('R75',279.90242,603.96984),('R75',252.44049,573.55282),('R75',319.25680,572.39929),('R75',295.11300,614.02319),('R76',363.65604,696.73591),('R76',325.66548,654.65731),('R76',383.83812,672.66554),('R77',409.02173,642.63005),('R77',404.30093,641.63682),('R77',354.08830,571.79794),('R77',470.09091,569.79524),('R78',438.85505,689.69687),('R78',406.86469,645.20266),('R78',473.20123,700.32925),('R79',273.04483,533.99650),('R79',335.00298,545.25287),('R79',319.25680,572.39929),('R80',510.17663,577.07790),('R80',470.09091,569.79524),('R80',512.58150,569.06167);
/*!40000 ALTER TABLE `region` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-07 12:21:29
