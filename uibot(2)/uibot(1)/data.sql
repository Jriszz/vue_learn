/*
SQLyog Ultimate v12.08 (64 bit)
MySQL - 5.7.25-log : Database - testcasedata
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`testcasedata` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `testcasedata`;

/*Table structure for table `base_orders` */

DROP TABLE IF EXISTS `base_orders`;

CREATE TABLE `base_orders` (
  `TestNo` int(4) NOT NULL AUTO_INCREMENT COMMENT '用例编号',
  `TestModule` varchar(250) NOT NULL COMMENT '测试模块',
  `OrderName` varchar(250) NOT NULL COMMENT '被测指令',
  `CaseName` varchar(500) NOT NULL COMMENT '测试用例名称',
  `CaseType` varchar(50) NOT NULL DEFAULT 'Normal' COMMENT '用例类型',
  `IsAutomation` char(2) NOT NULL DEFAULT 'Y' COMMENT '自动执行标识',
  `PreCondition` json DEFAULT NULL COMMENT '前置条件',
  `Designer` varchar(20) NOT NULL DEFAULT 'admin' COMMENT '设计人',
  `Comments` varchar(500) DEFAULT NULL COMMENT '备注',
  `BhCondition` json DEFAULT NULL COMMENT '后置条件',
  `IsCheckData` char(2) NOT NULL DEFAULT 'N' COMMENT '是否校验数据',
  `CheckData` json DEFAULT NULL COMMENT '被校验数据',
  `TestParmeter` json DEFAULT NULL COMMENT '测试数据',
  `ExpectVal` text NOT NULL COMMENT '预期结果',
  `ExpectDataVal` text COMMENT '预期数据结果',
  `CreateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `UpdateTime` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`TestNo`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

/*Data for the table `base_orders` */

insert  into `base_orders`(`TestNo`,`TestModule`,`OrderName`,`CaseName`,`CaseType`,`IsAutomation`,`PreCondition`,`Designer`,`Comments`,`BhCondition`,`IsCheckData`,`CheckData`,`TestParmeter`,`ExpectVal`,`ExpectDataVal`,`CreateTime`,`UpdateTime`) values (1,'基本命令','delay','AD','Normal','Y','null','admin','ADSA','null','N',NULL,'{\"delay_time\": \"ADA\"}','ADA',NULL,'2020-04-16 17:08:01',NULL),(2,'基本命令','delay','延时30秒','Normal','Y','null','admin','231','null','N',NULL,'{\"delay_time\": 30}','null',NULL,'2020-04-16 22:05:38',NULL),(3,'基本命令','delay','30秒','Normal','Y','null','admin','正向用例','null','N',NULL,'{\"delay_time\": 39}','10',NULL,'2020-04-17 19:29:11',NULL),(4,'基本命令','delay','342','Normal','Y','null','admin','2342','null','N',NULL,'{\"delay_time\": \"\"}','',NULL,'2020-04-17 19:30:17',NULL),(5,'基本命令','delay','535','Normal','Y','null','admin','34535','null','N',NULL,'{\"delay_time\": 3453}','3453',NULL,'2020-04-17 19:31:13',NULL),(6,'基本命令','delay','342','Normal','Y','null','admin','234','null','N',NULL,'{\"delay_time\": \"\"}','',NULL,'2020-04-17 19:33:25',NULL),(7,'基本命令','delay','342','Normal','Y','null','admin','2342','null','N',NULL,'{\"delay_time\": 2342}','2342',NULL,'2020-04-17 19:33:58',NULL),(8,'基本命令','delay','4535','Normal','Y','null','admin','3453','null','N',NULL,'{\"delay_time\": 23}','2342',NULL,'2020-04-17 19:37:07',NULL),(9,'基本命令','delay','3424','Normal','Y','null','admin','2342','null','N',NULL,'{\"delay_time\": 231}','1231',NULL,'2020-04-17 19:38:26',NULL),(10,'基本命令','delay','1231','Normal','Y','null','admin','1231','null','N',NULL,'{\"delay_time\": 2131}','1231',NULL,'2020-04-17 19:39:44',NULL),(11,'基本命令','delay','32','Normal','Y','null','admin','2342','null','N',NULL,'{\"delay_time\": 3123}','1231',NULL,'2020-04-17 19:42:28',NULL),(12,'基本命令','delay','342','Normal','Y','null','admin','2342','null','N',NULL,'{\"delay_time\": \"234の\"}','3242',NULL,'2020-04-17 19:43:10',NULL),(13,'基本命令','delay','2343','Normal','Y','null','admin','343','null','N',NULL,'{\"delay_time\": 34}','343',NULL,'2020-04-17 19:43:43',NULL),(14,'基本命令','delay','4535r','Normal','Y','null','admin','34535','null','N',NULL,'{\"convert_data\": 4545}','45454',NULL,'2020-04-17 19:44:07',NULL),(15,'基本命令','delay','3424','Normal','Y','null','admin','23424','null','N',NULL,'{\"delay_time\": 342}','3434',NULL,'2020-04-17 19:44:35',NULL),(16,'基本命令','delay','342','Normal','Y','null','admin','2342','null','N',NULL,'{\"delay_time\": 23}','232',NULL,'2020-04-17 20:02:55',NULL);

/*Table structure for table `exec_config` */

DROP TABLE IF EXISTS `exec_config`;

CREATE TABLE `exec_config` (
  `TestSequence` int(3) NOT NULL AUTO_INCREMENT,
  `TestModule` varchar(250) NOT NULL COMMENT '执行测试模块',
  `OrderName` varchar(250) NOT NULL COMMENT '被测指令',
  `TestNo` int(4) DEFAULT NULL COMMENT '用例编号',
  PRIMARY KEY (`TestSequence`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `exec_config` */

insert  into `exec_config`(`TestSequence`,`TestModule`,`OrderName`,`TestNo`) values (1,'基本命令','延时',0);

/*Table structure for table `modules_orders` */

DROP TABLE IF EXISTS `modules_orders`;

CREATE TABLE `modules_orders` (
  `ModuleNumber` int(6) NOT NULL AUTO_INCREMENT COMMENT '模块编号',
  `ModuleName` varchar(250) DEFAULT NULL COMMENT '模块名',
  `OrderName` varchar(250) DEFAULT NULL COMMENT '指令名',
  `OrderName_Chn` varchar(500) DEFAULT NULL,
  `ModuleName_Chn` varchar(250) DEFAULT NULL,
  `PreParameter` json DEFAULT NULL COMMENT '前置参数',
  `TestParameter` json DEFAULT NULL COMMENT '测试参数',
  `BhParameter` json DEFAULT NULL COMMENT '后置参数',
  `TableName` varchar(30) NOT NULL,
  PRIMARY KEY (`ModuleNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4;

/*Data for the table `modules_orders` */

insert  into `modules_orders`(`ModuleNumber`,`ModuleName`,`OrderName`,`OrderName_Chn`,`ModuleName_Chn`,`PreParameter`,`TestParameter`,`BhParameter`,`TableName`) values (18,'BaseOrders','delay','延时','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"delay_time\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"等待时间\"}]}',NULL,'base_orders'),(19,'BaseOrders','cbool','转为逻辑数据','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"convert_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待转换数据\"}]}',NULL,'base_orders'),(20,'BaseOrders','cnumber','转为小数数据','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"convert_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待转换数据\"}]}',NULL,'base_orders'),(21,'BaseOrders','cint','转为整数数据','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"convert_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待转换数据\"}]}',NULL,'base_orders'),(22,'BaseOrders','cstr','转为文字数据','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"covert_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待转换数据\"}]}',NULL,'base_orders'),(23,'BaseOrders','decimal','转为十进制数字','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"convert_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待转换数据\"}]}',NULL,'base_orders'),(24,'BaseOrders','clone','复制数据','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"copy_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待复制数据\"}]}',NULL,'base_orders'),(25,'BaseOrders','type','获取变量类型','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"judge_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待判断数据\"}]}',NULL,'base_orders'),(26,'BaseOrders','is_array','是否为数组','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"judge_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待判断数据\"}]}',NULL,'base_orders'),(27,'BaseOrders','is_array','是否为字典','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"judge_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待判断数据\"}]}',NULL,'base_orders'),(28,'BaseOrders','is_null','是否为空值','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"judge_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待判断数据\"}]}',NULL,'base_orders'),(29,'BaseOrders','is_numeric','是否为转换为数值','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"judge_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待判断数据\"}]}',NULL,'base_orders'),(30,'BaseOrders','hex','取十六进制','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"convert_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待转换数据\"}]}',NULL,'base_orders'),(31,'BaseOrders','oct','取八进制','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"convert_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待转换数据\"}]}',NULL,'base_orders'),(32,'BaseOrders','rnd','取随机数','基本命令',NULL,'{\"parameters\": []}',NULL,'base_orders'),(33,'BaseOrders','traceprint','输出调试信息','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"print_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"调试信息内容\"}]}',NULL,'base_orders'),(34,'BaseOrders','collect_garbage','垃圾回收','基本命令',NULL,'{\"parameters\": []}',NULL,'base_orders'),(35,'BaseOrders','unitest','单元测试块','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"unittest_data\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"待测试块\"}]}',NULL,'base_orders'),(36,'BaseOrders','function','子程序','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"function_name\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"子程序命令名\"}, {\"parameter_name\": \"function_prop\", \"parameter_type\": \"text\", \"parameter_name_chn\": \"命令属性\"}]}',NULL,'base_orders'),(37,'BaseOrders','Rem','Rem注释','基本命令',NULL,'{\"parameters\": [{\"parameter_name\": \"rem_data\", \"parameter_text\": \"text\", \"parameter_name_chn\": \"待注释内容\"}]}',NULL,'base_orders');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
