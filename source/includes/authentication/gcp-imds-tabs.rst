.. tabs::

   .. tab:: MongoClient
      :tabid: mongoclient

      .. code-block:: python

         from pymongo import MongoClient
         
         properties = {"ENVIRONMENT": "gcp", "TOKEN_RESOURCE": "<audience>"}

         client = MongoClient(
            "mongodb://<hostname>:<port>",
            username="<GCP identity client ID>",
            authMechanism="MONGODB-OIDC",
            authMechanismProperties=properties,
         )

   .. tab:: Connection String
      :tabid: connectionstring

      .. code-block:: python

         from pymongo import MongoClient

         properties = {"ENVIRONMENT": "gcp", "TOKEN_RESOURCE": "<audience>"}
         
         uri = ("mongodb://<hostname>:<port>/?"
                "username="<GCP identity client ID>"
                "&authMechanism=MONGODB-OIDC"
                "&authMechanismProperties=properties")
         client = MongoClient(uri)