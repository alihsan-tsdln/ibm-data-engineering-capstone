# Querying data in NoSQL databases

# Scenario
You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MongoDB as a NoSQL database. You will be using MongoDB to store the e-commerce catalog data.

# Objectives
In this assignment you will:
 * import data into a MongoDB database.
 * query data in a MongoDB database.
 * export data from MongoDB.

# Tools / Software
 * MongoDB Server
 * MongoDB Command Line Backup Tools

# Exercise 1 - Check your environment
Before you proceed with the assignment :
 * Check if you have the ‘mongoimport’ and ‘mongoexport’ installed on your environment, otherwise install them.
   <pre lang=sh>
   mongoimport --version
   mongoexport --version
   </pre>
   If they are not exist.
   <pre lang=sh>
   #FOR UBUNTU
   sudo apt-get update
   sudo apt-get install -y mongodb-org
   sudo apt-get install -y mongodb-clients
   </pre>
   
 * Download the catalog.json file from https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json.
   And download json file
   <pre lang="sh">
   curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json
   </pre>

# Exercise 2 - Working with MongoDB

## Task 1 - Import ‘catalog.json’ into mongodb server into a database named ‘catalog’ and a collection named ‘electronics’
<pre lang="sh">
mongoimport -d catalog -c electronics --file {$YOUR_JSON_FILE_PATH/catalog.json} -u {$YOUR_USERNAME} -p {$YOUR_PASSWORD} --authenticationDatabase admin
</pre>

## Task 2 - List out all the databases
<pre lang="sh">
mongosh -u {$YOUR_USERNAME} -p --authenticationDatabase admin
# enter password: {$YOUR_PASSWORD}
</pre>
<pre lang="mongo">
show databases
</pre>
  
## Task 3 - List out all the collections in the database catalog.
<pre lang="mongo">
use catalog
show collections
</pre>

## Task 4 - Create an index on the field “type”
<pre lang="mongo">
db.electronics.createIndex({"type" : 1})
db.electronics.getIndexes()
</pre>

## Task 5 - Write a query to find the count of laptops
<pre lang="mongo">
db.electronics.countDocuments({"type" : "laptop"})
</pre>

## Task 6 - Write a query to find the number of smart phones with screen size of 6 inches.
<pre lang="mongo">
db.electronics.countDocuments({"type" : "smart phone", "screen size" : 6})
</pre>

## Task 7. Write a query to find out the average screen size of smart phones.
<pre lang="mongo">
db.electronics.aggregate([{$match : {"type" : "smart phone"}}, {$group : {_id : null, avg_val : {$avg : "$screen size"}}}, {$project : {_id : 0, avg_val:1}}])
</pre>

## Task 8 - Export the fields _id, “type”, “model”, from the ‘electronics’ collection into a file named electronics.csv
<pre lang="sh">
mongoexport -d catalog -c electronics  -o electronics.csv --csv -f _id,type,model -u {$YOUR_USERNAME} -p {$YOUR_PASSWORD} --authenticationDatabase admin
</pre>
