
# Data Warehouse Reporting

# Scenario
You are a data engineer hired by an ecommerce company named SoftCart.com . The company retails download only items like E-Books, Movies, Songs etc. The company has international presence and customers from all over the world. You have designed the schema for the data warehouse in the previous assignment. Data engineering is a team game. Your senior data engineer reviewed your design. Your schema design was improvised to suit the production needs of the company. In this assignment you will generate reports out of the data in the data warehouse.

# Objectives
In this assignment you will:

 * Load data into Data Warehouse
 * Write aggregation queries
 * Create MQTs

# Prepare the your environment
Before you start the assignment:

1. Right Click on this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/CREATE_SCRIPT.sql) and save this SQL file in you local system.

2. Start PostgreSQL server

<pre lang="sh">
psql -U postgres -W -h localhost
# password : ${YOUR_PASSWORD}
</pre>

3. Create a new database Test1
<pre lang="sql">
CREATE DATABASE test1;
# password : ${YOUR_PASSWORD}
</pre>

Connect test1 database.

<pre lang="sh">
\c test1
</pre>

4. Create the following tables
 * DimDate
   <pre lang="sql">
   CREATE TABLE public."DimDate"
   (
       dateid integer NOT NULL,
       date date,
       "Year" smallint,
       "Quarter" smallint,
       "QuarterName" character(2) COLLATE pg_catalog."default",
       "Month" smallint,
       "Monthname" character(9) COLLATE pg_catalog."default",
       "Day" smallint,
       "Weekday" smallint,
       "WeekdayName" character(9) COLLATE pg_catalog."default",
       CONSTRAINT "DimDate_pkey" PRIMARY KEY (dateid)
   )
    
   TABLESPACE pg_default;
  
   ALTER TABLE public."DimDate"
   OWNER to postgres;
  </pre>
    
 * DimCategory
   <pre lang="sql">
   CREATE TABLE public."DimCategory"
   (
       categoryid integer NOT NULL,
       category text COLLATE pg_catalog."default",
       CONSTRAINT "DimCategory_pkey" PRIMARY KEY (categoryid)
   )
    
   TABLESPACE pg_default;
    
   ALTER TABLE public."DimCategory"
       OWNER to postgres;
   </pre>
 * DimCountry
   <pre lang="sql">
   CREATE TABLE public."DimCountry"
   (
       countryid integer NOT NULL,
       country text COLLATE pg_catalog."default",
       CONSTRAINT "DimCountry_pkey" PRIMARY KEY (countryid)
   )
    
   TABLESPACE pg_default;
    
   ALTER TABLE public."DimCountry"
       OWNER to postgres;
   </pre>
 * FactSales
   <pre lang="sql">
   CREATE TABLE public."FactSales"
   (
       orderid integer NOT NULL,
       dateid integer,
       countryid integer,
       categoryid integer,
       amount integer,
       CONSTRAINT "FactSales_pkey" PRIMARY KEY (orderid)
       CONSTRAINT category_fk FOREIGN KEY (categoryid)
           REFERENCES public."DimCategory" (categoryid) MATCH SIMPLE
           ON UPDATE NO ACTION
           ON DELETE NO ACTION,
       CONSTRAINT countryid_fk FOREIGN KEY (countryid)
           REFERENCES public."DimCountry" (countryid) MATCH SIMPLE
           ON UPDATE NO ACTION
           ON DELETE NO ACTION,
       CONSTRAINT dateid_fk FOREIGN KEY (dateid)
           REFERENCES public."DimDate" (dateid) MATCH SIMPLE
           ON UPDATE NO ACTION
           ON DELETE NO ACTION
   )
    
   TABLESPACE pg_default;
    
   ALTER TABLE public."FactSales"
       OWNER to postgres;
   </pre>

# Loading Data
In this exercise you will load the data into the tables. You will load the data provided by the company in csv format.

## Task 1 - Load data into the dimension table DimDate
 * Download the data from [this link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/data/DimDate.csv)
 * Load the downloaded data into DimDate table.

<pre lang="sql">
COPY "DimDate" FROM '{$CSV_FILES_PATH}/DimDate.csv' CSV HEADER;
</pre>

## Task 2 - Load data into the dimension table DimCategory
 * Download the data from [this link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCategory.csv)
 * Load the downloaded data into DimCategory table.
 <pre lang="sql">
 COPY "DimCategory" FROM '{$CSV_FILES_PATH}/DimCategory.csv' CSV HEADER;
 </pre>

## Task 3 - Load data into the dimension table DimCountry
 * Download the data from [this link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCountry.csv)
 * Load the downloaded data into DimCountry table.
 <pre lang="sql">
 COPY "DimCountry" FROM '{$CSV_FILES_PATH}/DimCountry.csv' CSV HEADER;
 </pre>
## Task 4 - Load data into the fact table FactSales
 * Download the data from [this link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/FactSales.csv)
 * Load this data into FactSales table.
 <pre lang="sql">
 COPY "FactSales" FROM '{$CSV_FILES_PATH}/FactSales.csv' CSV HEADER;
 </pre>
# Queries for data analytics
In this exercise you will query the data you have loaded in the previous exercise.

## Task 5 - Create a grouping sets query
Create a grouping sets query using the columns country, category, totalsales.
<pre lang="sql">
SELECT country, category, SUM(amount) AS totalsales
FROM "FactSales" s
INNER JOIN "DimCountry" ON "DimCountry".countryid = s.countryid
INNER JOIN "DimCategory" ON "DimCategory".categoryid = s.categoryid
GROUP BY GROUPING SETS((country,category),(country),(category));
</pre>

## Task 6 - Create a rollup query
Create a rollup query using the columns year, country, and totalsales.
<pre lang="sql">
SELECT "Year",country,SUM(amount)
FROM "FactSales" s
INNER JOIN "DimDate" d ON s.dateid = d.dateid
INNER JOIN "DimCountry" dc ON s.countryid = dc.countryid 
GROUP BY ROLLUP("Year",country);
</pre>

## Task 7 - Create a cube query
Create a cube query using the columns year, country, and average sales.
<pre lang="sql">
SELECT "Year", country, AVG(amount) AS averagesales
FROM "FactSales" s
INNER JOIN "DimCountry" dc ON dc.countryid = s.countryid
INNER JOIN "DimDate" dd ON dd.dateid = s.dateid
GROUP BY CUBE("Year",country);
</pre>

## Task 8 - Create an MQT
Create an MQT named total_sales_per_country that has the columns country and total_sales.
<pre lang="sql">
CREATE MATERIALIZED VIEW total_sales_per_country AS
SELECT country, SUM(amount) as total_sales
FROM "FactSales" s
INNER JOIN "DimCountry" d ON s.countryid = d.countryid
GROUP BY country
</pre>
