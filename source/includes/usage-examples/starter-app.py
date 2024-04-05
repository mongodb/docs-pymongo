# start starter app
from pymongo import MongoClient

try:
    # start authentication code here

    # end authentication code here

    database = client.get_database("<your database>")
    collection = database.get_collection("<your collection>")

    # ...

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
# end starter app
