from pymongo import MongoClient

try:

    # start connection code here

    # end connection code here

    client.admin.command("ping")
    print("Connected successfully")

    # other application code

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
