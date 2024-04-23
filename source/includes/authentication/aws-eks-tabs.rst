.. tabs::

   .. tab:: MongoClient
      :tabid: mongoclient

      .. code-block:: python

         import os
         from pymongo import MongoClient
         from pymongo.auth_oidc import OIDCCallback, OIDCCallbackContext, OIDCCallbackResult
         
         class MyCallback(OIDCCallback):
            def fetch(self, context: OIDCCallbackContext) -> OIDCCallbackResult:
                with open(os.environ["AWS_WEB_IDENTITY_TOKEN_FILE"]) as fid:
                    token = fid.read()
                return OIDCCallbackResult(access_token=token)
    
         props = {"OIDC_CALLBACK": MyCallback()}

         client = MongoClient(
            "mongodb://<hostname>:<port>",
            authMechanism="MONGODB-OIDC",
            authMechanismProperties=properties,
         )

   .. tab:: Connection String
      :tabid: connectionstring

      .. code-block:: python

         import os
         from pymongo import MongoClient
         from pymongo.auth_oidc import OIDCCallback, OIDCCallbackContext, OIDCCallbackResult
         
         class MyCallback(OIDCCallback):
            def fetch(self, context: OIDCCallbackContext) -> OIDCCallbackResult:
                with open(os.environ["AWS_WEB_IDENTITY_TOKEN_FILE"]) as fid:
                    token = fid.read()
                return OIDCCallbackResult(access_token=token)
    
         properties = {"OIDC_CALLBACK": MyCallback()}

         uri = ("mongodb://<hostname>:<port>/?"
                "&authMechanism=MONGODB-OIDC"
                "&authMechanismProperties=properties")
         client = MongoClient(uri)