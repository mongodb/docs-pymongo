from pymongo import MongoClient

# define URI and MongoClient
uri = ("mongodb://<hostname>:<port>/?"
       "username=<Azure identity client ID>"
       "&authMechanism=MONGODB-OIDC"
       "&authMechanismProperties=environment:azure,token_resource:<audience>")
client = MongoClient(uri)