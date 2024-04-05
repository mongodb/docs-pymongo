# start starter app
from pymongo import MongoClient

try:
    database = client.get_database("<your database>")
    movies = database.get_collection("<your collection>")

    # start your code here
    uri = "<your connection string>"
    client = MongoClient(uri)

    # end your code here

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
# end starter app
