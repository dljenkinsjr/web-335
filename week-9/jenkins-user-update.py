#*============================================; 
#Title: Assignment 9.3; 
#Author: Professor Krasso ;
# Date: 8 December 2020; 
# Modified By: Douglas Jenkins; 
# Description: Updating and Deleting Documents
#;===========================================*/

## creates the import information for python
from pymongo import MongoClient

import pymongo

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

## updates the user with information

db.users.update_one(

    {"employee_id": "0000008"},
    {
        "$set": {

            "email": "doujenkins@my365.bellevue.edu"
        }
    }
)

## outputs the updated results
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))