/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 10.4.28-MariaDB : Database - jdlivraria
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`jdlivraria` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `jdlivraria`;

/*Table structure for table `livros` */

DROP TABLE IF EXISTS `livros`;

CREATE TABLE `livros` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `autor` varchar(100) NOT NULL,
  `editora` varchar(50) NOT NULL,
  `preco` decimal(10,2) NOT NULL,
  `descricao` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `livros` */

insert  into `livros`(`codigo`,`titulo`,`autor`,`editora`,`preco`,`descricao`) values 
(1,'Código Limpo','Robert C. Martin','Alta Books',59.90,NULL),
(2,'O Hobbit','J.R.R. Tolkien','HarperCollins',39.90,'Livro sobre anoes'),
(3,'Python Fluente','Luciano Ramalho','Novatec',79.90,''),
(4,'A Menina que Roubava Livros','Markus Zusak','Intrínseca',29.90,'Bom dia'),
(5,'A Origem das Espécies','Charles Darwin','L&PM Editores',45.00,NULL),
(6,'Eu me caguei','Openraimer','saraiva',20.00,'Caguei bolinha preta'),
(7,'Código Limpo','Robert C. Martin','Alta Books',59.90,'Livro sobre boas práticas de programação com exemplos em Python.'),
(8,'O Hobbit','J.R.R. Tolkien','HarperCollins',39.90,'Uma história de aventuras em um mundo de fantasia.'),
(9,'Python Fluente','Luciano Ramalho','Novatec',79.90,'Guia avançado para a linguagem Python.'),
(10,'A Menina que Roubava Livros','Markus Zusak','Intrínseca',29.90,'A história de uma jovem alemã durante a Segunda Guerra Mundial.'),
(11,'A Origem das Espécies','Charles Darwin','L&PM Editores',45.00,'Obra sobre a teoria da evolução.'),
(12,'O Pequeno Príncipe','Antoine de Saint-Exupéry','Agir',19.90,'Um livro que encanta leitores de todas as idades.'),
(13,'O Senhor dos Anéis','J.R.R. Tolkien','Martins Fontes',120.00,'Trilogia épica de fantasia.'),
(14,'O Código Da Vinci','Dan Brown','Arqueiro',29.90,'Mistério e conspiração na busca pelo Santo Graal.'),
(15,'1984','George Orwell','Companhia das Letras',39.90,'Distopia sobre um regime totalitário.'),
(16,'O Alquimista','Paulo Coelho','Rocco',24.90,'Jornada de autoconhecimento.'),
(17,'Dom Casmurro','Machado de Assis','Martin Claret',14.90,'Clássico da literatura brasileira.'),
(18,'Harry Potter e a Pedra Filosofal','J.K. Rowling','Rocco',39.90,'Primeiro livro da série de fantasia.'),
(19,'Crime e Castigo','Fiódor Dostoiévski','Nova Fronteira',49.90,'Estudo psicológico de um assassinato.'),
(20,'A Metamorfose','Franz Kafka','Companhia das Letras',19.90,'Novela sobre a transformação de um homem em inseto.'),
(21,'Anna Karenina','Liev Tolstói','Nova Fronteira',59.90,'História de amor e tragédia na Rússia do século XIX.'),
(22,'O Pequeno Livro das Sementes','Ruth Kassinger','Sextante',39.90,'Exploração do mundo das sementes.'),
(23,'A Guerra dos Tronos','George R.R. Martin','LeYa',80.00,'Início da série de fantasia \'As Crônicas de Gelo e Fogo\'.'),
(24,'Eu Sou Malala','Malala Yousafzai','Companhia das Letras',29.90,'Autobiografia da ativista paquistanesa.'),
(25,'Sapiens - Uma Breve História da Humanidade','Yuval Noah Harari','L&PM Editores',59.90,'Visão da história humana.'),
(26,'A Coragem de Ser Imperfeito','Brené Brown','Sextante',34.90,'Livro sobre vulnerabilidade e imperfeição.'),
(30,'O poder da mente','Olavo Adriel','IFRN - EDTS',14.00,'Um livro sobre empoderamente pessoal');

/*Table structure for table `usuarios` */

DROP TABLE IF EXISTS `usuarios`;

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(50) NOT NULL,
  `senha` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `usuarios` */

insert  into `usuarios`(`id`,`usuario`,`senha`) values 
(1,'olavo','senha123'),
(2,'leo','657b298b04e033810343842f993c9817'),
(3,'pedro','202cb962ac59075b964b07152d234b70'),
(4,'joao','202cb962ac59075b964b07152d234b70'),
(5,'giovane','202cb962ac59075b964b07152d234b70');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
