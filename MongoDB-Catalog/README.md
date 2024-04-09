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

# Exercise 1 - Check the lab environment
Before you proceed with the assignment :
 * Check if you have the ‘mongoimport’ and ‘mongoexport’ installed on the lab, otherwise install them.
 * Download the catalog.json file from https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json.

```
mongoimport --version
mongoexport --version
```
If they are not exist.
```
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo apt-get install -y mongodb-clients
```

And download json file
```
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json
```

# Exercise 2 - Working with MongoDB

## Task 1 - Import ‘catalog.json’ into mongodb server into a database named ‘catalog’ and a collection named ‘electronics’
```
mongoimport -d catalog -c electronics --file {$YOUR_JSON_FILE_PATH/catalog.json} -u {$YOUR_USERNAME} -p {$YOUR_PASSWORD} --authenticationDatabase admin
```

## Task 2 - List out all the databases
```
mongosh -u {$YOUR_USERNAME} -p {$YOUR_PASSWORD} --authenticationDatabase admin
> show databases
```

## Task 3 - List out all the collections in the database catalog.
```
> use catalog
> show collections
```

## Task 4 - Create an index on the field “type”
```
catalog> db.electronics.createIndex({"type" : 1})
catalog> db.electronics.getIndexes()
```

## Task 5 - Write a query to find the count of laptops
```
catalog> db.electronics.countDocuments({"type" : "laptop"})
```

## Task 6 - Write a query to find the number of smart phones with screen size of 6 inches.
```
catalog> db.electronics.countDocuments({"type" : "smart phone", "screen size" : 6})
```

## Task 7. Write a query to find out the average screen size of smart phones.
```
catalog> db.electronics.aggregate([{$match : {"type" : "smart phone"}}, {$group : {_id : null, avg_val : {$avg : "$screen size"}}}, {$project : {_id : 0, avg_val:1}}])
```

## Task 8 - Export the fields _id, “type”, “model”, from the ‘electronics’ collection into a file named electronics.csv
```
mongoexport -d catalog -c electronics  -o electronics.csv --csv -f _id,type,model -u {$YOUR_USERNAME} -p {$YOUR_PASSWORD} --authenticationDatabase admin
```
