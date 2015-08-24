CREATE DATABASE  IF NOT EXISTS `exchange_database` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `exchange_database`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win32 (x86)
--
-- Host: localhost    Database: exchange_database
-- ------------------------------------------------------
-- Server version	5.6.20

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
-- Table structure for table `unitkeywords`
--

DROP TABLE IF EXISTS `unitkeywords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unitkeywords` (
  `unit_key` int(11) NOT NULL AUTO_INCREMENT,
  `unit_code` varchar(20) NOT NULL,
  `unit_desc` varchar(5000) NOT NULL,
  PRIMARY KEY (`unit_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unitkeywords`
--

LOCK TABLES `unitkeywords` WRITE;
/*!40000 ALTER TABLE `unitkeywords` DISABLE KEYS */;
/*!40000 ALTER TABLE `unitkeywords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unitlist`
--

DROP TABLE IF EXISTS `unitlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unitlist` (
  `unit_key` int(11) NOT NULL AUTO_INCREMENT,
  `unit_code` varchar(20) NOT NULL,
  `unit_name` varchar(300) NOT NULL,
  `unit_desc` varchar(5000) NOT NULL,
  `unit_text` varchar(300) DEFAULT NULL,
  `ISBN` int(11) DEFAULT NULL,
  `FreeTags` varchar(5000) DEFAULT NULL,
  `Positive` varchar(5000) DEFAULT NULL,
  `sch_id` int(11) NOT NULL,
  `unit_link` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`unit_key`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unitlist`
--

LOCK TABLES `unitlist` WRITE;
/*!40000 ALTER TABLE `unitlist` DISABLE KEYS */;
INSERT INTO `unitlist` VALUES (1,'CITS1402','Relational Database Management Systems [UG]','This unit deals with data modelling through the theory and practice of database design, implementation and use. Several database models are addressed, with a strong focus on the relational model and its theoretical grounding in sets and relational algebra. The process of problem decomposition into entity-relations, the design of appropriate relational schemas, and their refinement through normalisation underlies this unit. Critical issues surrounding the design of query languages and their implementation are addressed, and information retrieval is practised using a specific query language. Students learn database connectivity by building systems in one of several programming languages that support a connectivity Application Programming Interface (API).',NULL,NULL,NULL,NULL,1,'http://www.unitoutlines.ecm.uwa.edu.au/Units/CITS1402/SEM-2/2015'),(2,'CITS2002','Programming and Systems [UG]','Understanding the relationship between a programming language and the contemporary operating systems on which it executes is central to developing many skills in Computer Science. This unit introduces the standard C programming language, on which many other programming languages and systems are based, through a study of core operating system services including input and output, memory management and file systems. The C language is introduced through discussions on basic topics like data types, variables, expressions, control structures, scoping rules, functions and parameter passing. More advanced topics like C\'s run-time environment, system calls, dynamic memory allocation, pointers and recursion are presented in the context of operating system services related to process execution, memory management and file systems. The importance of process scheduling, memory management and interprocess communication in modern operating systems is discussed in the context of operating system support for multiprogramming. Laboratory and tutorial work place a strong focus on the practical application of fundamental programming concepts, with examples designed to compare and contrast many key features of contemporary operating systems.',NULL,NULL,NULL,NULL,1,'http://www.unitoutlines.ecm.uwa.edu.au/Units/CITS2002/SEM-2/2015'),(3,'CITS4403','Computational Modelling','This unit explores current research topics in computational modelling. Students develop skills to identify problems, formulate solutions and conduct further research in open questions in this domain.',NULL,NULL,NULL,NULL,1,'http://www.unitoutlines.ecm.uwa.edu.au/Units/CITS4403/SEM-1/2015'),(4,'CITS1001','Object-oriented Programming and Software Engineering [UG]','This unit introduces the language structures and techniques needed to write well-structured programs in the object-oriented paradigm using the Java programming language. In particular, the process of developing appropriate classes, objects and methods to solve simple computational problems underlies the entire unit. Core computer programming topics such as the use of variables, primitive and reference data types, expressions, control structures involving selection and repetition, method decomposition and parameter passing are all covered in this context. Algorithmic techniques such as iteration, sorting, searching along with programming practices such as error handling, testing, debugging and documentation are introduced. The unit also covers advanced topics such as association, inheritance and interface. A strong focus is placed on the practical application of these concepts and techniques to produce working programs in computer laboratories. The rationale for using the object-oriented paradigm, and in particular the language Java, is covered in detail. No prior knowledge of computing or programming is assumed.','Barnes, D. J. and Kolling, M. Objects First with Java, 5th edn: Prentice Hall/Pearson Education 2012',NULL,NULL,NULL,1,'http://www.unitoutlines.ecm.uwa.edu.au/Units/CITS1001/SEM-1/2015'),(5,'CITS2200','Data Structures and Algorithms [UG]','At the core of most computer applications is the storage and retrieval of information. The way that the stored data is structured has a strong impact on what can be retrieved, how quickly it can be retrieved and how much space it occupies. The use of generic structures, or abstract data types (ADTs), to encapsulate the data also facilitates software engineering principles of independent modification, extension and re-use. This unit studies the specification, implementation and time-and-space performance of a range of commonly used ADTs and corresponding algorithms in an object-oriented setting.','Weiss, M. A. Data Structures and Problem Solving Using Java, 4th edn: Addison-Wesley 2010',NULL,NULL,NULL,1,'http://www.unitoutlines.ecm.uwa.edu.au/Units/CITS2200/SEM-1/2015'),(6,'CITS3200','Professional Computing [UG]','This unit teaches communication skills, an appreciation of the ethical and social implications of computing projects, and skills in project management and quality assurance. A number of lectures are given to introduce the principles of project management and the fundamental ethical and social principles involved in large-scale computing projects. The bulk of the unit is then taken up with a large group project, involving about six students per group. The project gives the students opportunities to practise various project management techniques and communication skills introduced in the lectures in a technical context.',NULL,NULL,NULL,NULL,1,'http://www.unitoutlines.ecm.uwa.edu.au/Units/CITS3200/SEM-2/2015'),(7,'CS1020','Data Structures and Algorithms I','This module is the second part of a three-part series on introductory programming and problem solving by computing. It continues the introduction that begins in CS1010, and emphasises objectoriented programming with application to simple data structures. Topics include object-oriented problem modeling with objects, classes and methods, object-oriented problem formulation and solving, data structure implementation strageties, abstraction and encapsulation of data structures, object-oriented programming constructs, APIs and class libraries, exception handling, lists, linked lists, stacks, queues, hash tables and their algorithmic design, sorting and searching methods, recursive algorithms, and Big-O notation. This module is appropriate for SoC and FoS students.',NULL,NULL,NULL,NULL,2,NULL),(8,'CS2102','Database Systems','The aim of this module is to introduce the fundamental concepts and techniques necessary for the understanding and practice of design and implementation of database applications and of the management of data with relational database management systems. The module covers practical and theoretical aspects of design with entity-relationship model, theory of functional dependencies and normalisation by decomposition in second, third and Boyce-Codd normal forms. The module covers practical and theoretical aspects of programming with SQL data definition and manipulation sublanguages, relational tuple calculus, relational domain calculus and relational algebra.',NULL,NULL,NULL,NULL,2,NULL),(9,'CS1010','Programming Methodology','This module introduces the fundamental concepts of problem solving by computing and programming using an imperative programming language. It is the first and foremost introductory course to computing. It is also the first part of a three-part series on introductory programming and problem solving by computing, which also includes CS1020 and CS2010. Topics covered include problem solving by computing, writing pseudo-codes, basic problem formulation and problem solving, program development, coding, testing and debugging, fundamental programming constructs (variables, types, expressions, assignments, functions, control structures, etc.), fundamental data structures: arrays, strings and structures, simple file processing, and basic recursion. This module is appropriate for SoC students.',NULL,NULL,NULL,NULL,2,NULL),(10,'CS3226','Web Programming and Applications','This module introduces students to software development on the Web platforms. Students will be exposed to important computer science concepts, including networking, databases, computer security, user interface design, programming languages, and software engineering. These concepts will be tied together through hands-on practice in building a Web-based application using the current Web development technology. At the end of the module, students are expected to be able to design and develop a Web application, to appreciate the underlying technology needed to build a Web application, and to develop a fundamental understanding of related computer science concepts.',NULL,NULL,NULL,NULL,2,NULL),(11,'IT1005','Introduction to Programming with Matlab','With the widespread use of computers and computational tools in industrial practice and research, it is important for students in the chemical engineering programme to gain a firm understanding and appreciation of the fundamentals of programming, algorithmic problem solving, coding and debugging. The final goal is to be able to apply these skills to solving realistic chemical engineering problems. MATLAB, a high-level computing language will be employed due to its capability to solve domain-specific computing problems more conveniently than with traditional programming languages. MATLAB also provides the platform to span a wide variety of application areas.',NULL,NULL,NULL,NULL,2,NULL),(12,'CS5239','Computer System Performance Analysis','The objective of this module is to provide students a working knowledge of computer performance evaluation and capacity planning. They will be able to identify performance bottlenecks, to predict when performance limits of a system will be exceeded, and to characterise present and future workload to perform capacity planning activities. Topics include: performance analysis overview; measurement techniques and tools including workload characterisation, instrumentation, benchmarking, analytical modelling techniques including operational analysis, stochastic queuing network analysis; performance of client-server architectures; capacity planning; case studies.',NULL,NULL,NULL,NULL,2,NULL),(13,'MA0003','Preliminary Mathematics I','The module covers the basic manipulative skills in mathematics which are required by students studying a scientific discipline. The module begins with a review of arithmetic skills, before illustrating how algebraic expressions can be manipulated and rearranged. This includes exploration of fractions, powers, brackets, factors etc. The concept of a function is introduced by investigating graphical techniques and then re-enforced by applying many of the algebraic methods introduced at the start of the module. The properties and graphs of a range of functions are analysed including polynomials, exponentials and trigonometric functions, with a range of examples explored.','Foundation Mathematics (3rd Ed), Booth, D. J., Pearson, 1998',NULL,NULL,NULL,3,'http://handbooks.data.cf.ac.uk/module/MA0003/15A.html'),(14,'MA0291','Accountancy','To give an appreciation of the nature and significance of Accounting in the private sector of the economy by an examination of the contribution it can make to the internal administration and external financing of a firm.  This module also highlights the pivotal role of accounting as a service activity within a broad business context.','Accounting & Finance for Non-Specialists, Atrill, P., & McLaney, E., Financial Times/Prentice Hall',NULL,NULL,NULL,3,'http://handbooks.data.cf.ac.uk/module/MA0291/15A.html'),(15,'MA3006','Introduction to Coding Theory and Data Compression','This double module introduces the fundamentals of coding theory and data compression. The first part is devoted to coding theory and will mainly focus on error-correcting codes, their properties and applications. No document or computer files can be guaranteed free from error.  Error-correcting codes are used to spot mistakes and suggest the most likely correction. If the rate of errors is such that several mistakes are likely in a single ‘word’ (e.g. radio transmissions), then the codes used are more combinatoric.  If errors are so rare that having two mistakes in the same ‘word’ is very unlikely (e.g. brand new computer disc), then the codes used are more algebraic. Many error-correcting codes correspond to geometrical patterns. The second part of the module deals with the broad field of data compression. We will first study lossless compression schemes, including the fundamental algorithms of Shannon, Huffman, Lempel-Ziv and arithmetic coding. Finally, the module will give the basic principles of lossy compression, such as quantization and transform coding. For instance, we will see the role wavelets (“the mathematical microscope”) play in data compression.','Introduction to Data Compression, Sayood, K., Morgan Kaufmann, 2000',NULL,NULL,NULL,3,'http://handbooks.data.cf.ac.uk/module/MA3006/15A.html'),(16,'MA3501','Elements of Mathematical Statistics','Is the arithmetic average the best way of estimating the mean of a probability distribution? Is Student\'s t-test the best way of testing null hypotheses about the mean? The answers to these questions are assumed to be yes in elementary statistics, this module shows that there is a firm mathematical basis for this assumption. The first part of the module is a study of methods of estimation of parameters of probability distributions.Brief comparisons are made of maximum likelihood estimation, the method of moments approach and Bayesian inference. The properties that are desirable in estimators are identified, and by using a series of results it is shown that under fairly general conditions maximum likelihood estimators have optimal properties. It is even possible, for some statistical estimation problems, to identify estimators that are unbiased (correct on average, in the long run) and have a smaller theoretical variance than any other unbiased estimator. The second part of the module covers the testing of hypotheses in statistics. It is shown how optimal statistical tests can be devised and a link is made with maximum likelihood. The module presents a coherent view of estimation and hypothesis testing in a firm theoretical framework.','Probability and Statistics, DeGroot, M. H., Addison-Wesley',NULL,NULL,NULL,3,'http://handbooks.data.cf.ac.uk/module/MA3501/15A.html'),(17,'MA4008','Computational Fluid Dynamics','This module provides an introduction to basic numerical methods used to simulate the flow of Newtonian fluids. Different formulations of the governing equations will be introduced and their relative merits discussed. The module will cover the discretization of the governing equations using the finite volume and finite element methods. The treatment of the convection term will be described and the effect this has on the overall stability of the schemes in the case of convection-dominated flows. The solution of the resulting systems of equations will be described using coupled and decoupled approaches. Most fluid flow problems cannot be solved by analytical means. In these cases one needs to resort to numerical techniques. In this module two distinct numerical methods will be described for discretizing the governing equations: the finite volume and finite element methods. The finite volume method is based on the integration of the governing equations over a control volume and the discretization of fluxes across the edges using finite difference approximations. The finite element method is based on the weak formulation of the problem, the partition of the flow domain into finite elements and the development of local polynomial-based approximations to the solution on each element. Important features of both methods will be discussed.','Computational Fluid Dynamics – The Finite Volume Method,  Versteeg, H. K.& Malalasekera, W., Pearson, 2007',NULL,NULL,NULL,3,'http://handbooks.data.cf.ac.uk/module/MA4008/15A.html');
/*!40000 ALTER TABLE `unitlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `universitylist`
--

DROP TABLE IF EXISTS `universitylist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `universitylist` (
  `sch_id` int(11) NOT NULL AUTO_INCREMENT,
  `sch_name` varchar(80) NOT NULL,
  `country` varchar(25) NOT NULL,
  `state` varchar(25) NOT NULL,
  `region` varchar(25) NOT NULL,
  PRIMARY KEY (`sch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `universitylist`
--

LOCK TABLES `universitylist` WRITE;
/*!40000 ALTER TABLE `universitylist` DISABLE KEYS */;
INSERT INTO `universitylist` VALUES (1,'University of Western Australia','Australia','Western Australia','Nedlands'),(2,'National University of Singapore','Singapore','Singapore','Singapore'),(3,'Cardiff University','United Kingdom','Cardiff','Europe');
/*!40000 ALTER TABLE `universitylist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-21  0:09:32
