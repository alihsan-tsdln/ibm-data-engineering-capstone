# OLTP Database

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

# Exercise 1 - Check your environment
Before you proceed with the assignment :
* Start MySQL server.
 <pre lang=sh>
   mysql -h ${YOUR_HOSTNAME} -P {YOUR_MYSQL_PORT} -u ${YOUR_USERNAME} -p
 # enter password: ${YOUR_PASSWORD}
 </pre>

# Exercise 2 - Design the OLTP Database
## Task 1 - Create a database.
Create a database named sales.
<pre lang="sql">
CREATE DATABASE sales;
</pre>
## Task 2 - Design a table named sales_data.
Design a table named sales_data based on the sample data given.
![image](https://github.com/alihsan-tsdln/ibm-data-engineering-capstone/assets/91479565/68875cba-74dc-4b3f-be7c-2e8a8458b29e)
Create the sales_data table in sales database.

<pre lang="sql">
CREATE TABLE `sales_data` (
 `product_id` int NOT NULL,
 `customer_id` int NOT NULL,
 `price` int NOT NULL,
 `quantity` mediumint NOT NULL,
 `timestamp` date NOT NULL,
 PRIMARY KEY (`product_id`,`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
</pre>

# Exercise 3 - Load the Data
## Task 3 - Import the data in the file oltpdata.csv
Download the file oltpdata.csv from https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/oltpdata.csv

Import the data from oltpdata.csv into sales_data table using phpMyAdmin.

<pre lang="sql">
LOAD DATA INFILE "{$DOWNLOADED_CSV_FILE_PATH}.csv"
INTO TABLE sales.sales_data
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n';
</pre>

## Task 4 - List the tables in the database sales
<pre lang="sql">
USE sales;
SHOW TABLES;
</pre>

## Task 5. Write a query to find out the count of records in the tables sales_data.
<pre lang="sql">
SELECT COUNT(*) FROM sales_data;
</pre>

## Task 6 - Create an index
Create an index named ts on the timestamp field.
<pre lang="sql">
CREATE INDEX time_idx ON sales_data(timestamp);
</pre>

## Task 7 - List indexes
List indexes on the table sales_data.
<pre lang="sql">
SHOW INDEX IN sales_data;
</pre>

## Task 8 - Write a bash script to export data.
Write a bash script named datadump.sh that exports all the rows in the sales_data table to a file named sales_data.sql
<pre lang="sh">
echo "Export process started!"
$DB_NAME = "sales"
$DB_USER = "{$YOUR_MYSQL_DBADMIN_USERNAME}"
$DB_PASSWORD = "{$YOUR_MYSQL_DBADMIN_PASSWORD}"
$OUTPUT_PATH = "\data\"
$OUTPUT_FILE = "sales_data.sql"

$MYSQL_CMD = "mysql -u $DB_USER -p $DB_PASSWORD -e"

$MYSQL_CMD "SELECT * FROM sales_data" > {$OUTPUT_PATH + $OUTPUT_FILE}

echo "Data exported to {$OUTPUT_PATH + $OUTPUT_FILE}"
</pre>
