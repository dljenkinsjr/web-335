#*============================================; 
#Title: Assignment 9.2; 
#Author: Professor Krasso ;
# Date: 8 December 2020; 
# Modified By: Douglas Jenkins; 
#Description: Querying and Creating Documents
#;===========================================*/

## creates the import information for python
from pymongo import MongoClient

import pymongo

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

##creates the user with information

user = {

    "first_name": "Jacob",
    "last_name": "Jasmine",
    "email": "jjacob@mail.com",
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

## allows you print out the user by using findone

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000008"}))