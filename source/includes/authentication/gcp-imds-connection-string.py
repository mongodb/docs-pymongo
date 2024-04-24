from pymongo import MongoClient

# define URI and MongoClient
uri = ("mongodb://<hostname>:<port>/?"
       "username=<GCP identity client ID>"
       "&authMechanism=MONGODB-OIDC"
       "&authMechanismProperties=environment:gcp,token_resource:<audience>")
client = MongoClient(uri)