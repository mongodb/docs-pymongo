# start mongoclient
from pymongo import MongoClient

# define properties and MongoClient
properties = {"ENVIRONMENT": "gcp", "TOKEN_RESOURCE": "<audience>"}
client = MongoClient(
   "mongodb://<hostname>:<port>",
   username="<GCP identity client ID>",
   authMechanism="MONGODB-OIDC",
   authMechanismProperties=properties,
)
# end mongoclient

# start connection string
from pymongo import MongoClient

# define properties, URI, and MongoClient
properties = {"ENVIRONMENT": "gcp", "TOKEN_RESOURCE": "<audience>"}
uri = ("mongodb://<hostname>:<port>/?"
       "username=<GCP identity client ID>"
       "&authMechanism=MONGODB-OIDC"
       "&authMechanismProperties=properties")
client = MongoClient(uri)
# end connection string