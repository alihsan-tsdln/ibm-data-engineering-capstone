# OLTP Database
## About This SN Labs Cloud IDE
This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and MySQL running in a Docker container.

# Important Notice about this lab environment
Please be aware that sessions for this lab environment are not persisted. Every time you connect to this lab, a new environment is created for you. Any data you may have saved in the earlier session would get lost. Plan to complete these labs in a single session, to avoid losing your data.
## Scenario
You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MySQL as an OLTP database. You will be using MySQL to store the OLTP data.
## Objectives
In this assignment you will:
* design the schema for OLTP database.
* load data into OLTP database.
* automate admin tasks.
## Tools / Software
* MySQL 8.0.22
* phpMyAdmin 5.0.4

# Exercise 1 - Check the lab environment
Before you proceed with the assignment :
* Start MySQL server.

# Exercise 2 - Design the OLTP Database
## Task 1 - Create a database.
Create a database named sales.
```
CREATE DATABASE sales
```
## Task 2 - Design a table named sales_data.
Design a table named sales_data based on the sample data given.
```
CREATE TABLE `sales_data` (
 `product_id` int NOT NULL,
 `customer_id` int NOT NULL,
 `price` int NOT NULL,
 `quantity` mediumint NOT NULL,
 `timestamp` date NOT NULL,
 PRIMARY KEY (`product_id`,`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```
