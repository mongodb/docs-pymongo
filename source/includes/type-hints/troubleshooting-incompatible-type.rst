Incompatible Type
~~~~~~~~~~~~~~~~~

If you use the generic form of the ``MongoClient`` class, you
might see the following mypy error:

.. code-block:: python

   error: Dict entry 0 has incompatible type "str": "int";
   expected "Mapping[str, Any]": "int"

The solution is to add the following type hint to your ``MongoClient`` object:

.. code-block:: python
  
   ``client: MongoClient[Dict[str, Any]]``