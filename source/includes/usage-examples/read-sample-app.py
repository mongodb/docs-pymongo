from pymongo import MongoClient

uri = "<connection string URI>"
client = MongoClient(uri)

try:
    database = client["<database name>"]
    collection = database["<collection name>"]

    # start example code below

    # end example code here

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
