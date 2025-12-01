#for our mongoDB connection and setup

import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# load .env
load_dotenv()

#get the Mongo URI from environment variables
uri = os.getenv("MONGO_URI")
if not uri:
    raise ValueError("No MONGO_URI found. Please set it in your .env file")

#connect to MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))

#set the project database
db = client['EcommerceProject']
