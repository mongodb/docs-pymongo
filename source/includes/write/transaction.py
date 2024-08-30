# start-transaction
# Establish a connection to the MongoDB server
client = MongoClient("<connection string>")

# Define the database and collection
restaurants_db = client["sample_restaurants"]
restaurants_collection = restaurants_db["restaurants"]

# Function to perform the transaction
def insert_documents(session):
    restaurants_collection_with_session = restaurants_collection.with_options(
        write_concern=WriteConcern("majority"),
        read_concern=ReadConcern("local")
    )
    
    # Insert documents within the transaction
    restaurants_collection_with_session.insert_one(
        {"name": "PyMongo Pizza", "cuisine": "Pizza"}, session=session
    )
    restaurants_collection_with_session.insert_one(
        {"name": "PyMongo Burger", "cuisine": "Burger"}, session=session
    )

# Start a client session
with client.start_session() as session:
    try:
        # Use the with_transaction method to start a transaction, execute the callback, and commit (or abort on error).
        session.with_transaction(insert_documents)
        print("Transaction succeeded")
    except (ConnectionFailure, OperationFailure) as e:
        print(f"Transaction failed: {e}")

# Close the client connection
client.close()
# end-transaction