from pymongo import MongoClient

# define properties and MongoClient
properties = {"ENVIRONMENT": "gcp", "TOKEN_RESOURCE": "<audience>"}
client = MongoClient(
   "mongodb://<hostname>:<port>",
   authMechanism="MONGODB-OIDC",
   authMechanismProperties=properties
)