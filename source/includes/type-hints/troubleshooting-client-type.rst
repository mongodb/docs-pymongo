Client Type Annotations
~~~~~~~~~~~~~~~~~~~~~~~

If you don't add a type annotation for your ``MongoClient`` object,
you might see the following mypy error:

.. code-block:: python

   from pymongo import MongoClient
   client = MongoClient()  # error: Need type annotation for "client"

The solution is to annotate the ``MongoClient`` object as
``client: MongoClient`` or ``client: MongoClient[Dict[str, Any]]``.