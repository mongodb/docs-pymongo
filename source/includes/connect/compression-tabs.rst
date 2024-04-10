.. tabs::

   .. tab:: MongoClient
      :tabid: mongoclient

      .. code-block:: python
         :emphasize-lines: 2

         client = pymongo.MongoClient("mongodb://<username>:<password>@<hostname>:<port>",
                                      compressors = "snappy,zstd,zlib")

   .. tab:: Connection String
      :tabid: connectionstring

      .. code-block:: python
         :emphasize-lines: 2

         uri = ("mongodb://<username>:<password>@<hostname>:<port>/?"
                "compressors=snappy,zstd,zlib")
         client = pymongo.MongoClient(uri)