from pymongo import MongoClient

try:

    # start example code here

    # end example code here

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
