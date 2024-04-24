Server Reports Wire Version X, PyMongo Requires Y
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you attempt to connect to a MongoDB Server v3.4 or earlier,
{+driver-short+} throws the following error:

.. code-block:: 

   pymongo.errors.ConfigurationError: Server at localhost:27017 reports wire version 5, but this version of PyMongo requires at least 6 (MongoDB 3.6).

This occurs when the driver version is too new for the server it's connecting to.
To resolve this issue, upgrade your database to a v3.6 or later, or downgrade to
PyMongo v3.x, which supports MongoDB Server v2.6 or later.

AutoReconnect
~~~~~~~~~~~~~

An ``AutoReconnect`` exception indicates that a
:manual:`failover <reference/glossary/#std-term-failover>` has occurred. This means that
{+driver-short+} has lost its connection to the original primary member
of the replica set, and its last operation might have failed.

When this error occurs, {+driver-short+} automatically tries to find the new primary member
for subsequent operations. To handle the error, your application must take one of the
following actions:

- Retry the operation that might have failed
- Continue running, with the understanding that the operation might have failed

.. important::
    
   {+driver-short+} raises an ``AutoReconnect`` error on all operations until the
   replica set elects a new primary member.