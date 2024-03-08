Python 3
~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :class: compatibility-large

   * - {+driver-short+} Version
     - Python 3.12
     - Python 3.11
     - Python 3.10 [#ssl-4.0-issue]_
     - Python 3.9
     - Python 3.8
     - Python 3.7
     - Python 3.6
     - Python 3.5
     - Python 3.4
     - PyPy3

   * - 4.6
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     -
     -
     -
     -

   * - 4.5
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     -
     -
     -
     -

   * - 4.4
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     -
     -
     -
     -

   * - 4.3
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     -
     -
     -
     -

   * - 4.2
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     -
     -
     -
     -

   * - 4.1 [#three-six-compat]_
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     -
     -
     -

   * - 4.0
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     -
     -
     -

   * - 3.13
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓

   * - 3.12
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓

   * - 3.11
     -
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓

   * - 3.10
     -
     -
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓

   * - 3.9
     -
     -
     -
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓

   * - 3.8
     -
     -
     -
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓

   * - 3.7
     -
     -
     -
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓

   * - 3.6
     -
     -
     -
     -
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓

.. [#ssl-4.0-issue] Versions of Python 3.10 and later are not compatible with
   TLS/SSL for versions of MongoDB 4.0 and earlier. For more information, see the
   :ref:`TLS guide <pymongo-python-3.10-tls>`.
.. [#three-six-compat] Pymongo 4.1 requires Python 3.6.2 or later.

.. note::

   PyPy3 is a Python 3.2-compatible alternative interpreter.

Python 2
~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :class: compatibility-large

   * - PyMongo Driver Version
     - | Python 2.7,
       | PyPy
     - Python 2.6

   * - 4.0 [#python-2-compat]_
     -
     -

   * - 3.12
     - ✓
     -

   * - 3.11
     - ✓
     -

   * - 3.10
     - ✓
     -

   * - 3.9
     - ✓
     -

   * - 3.8
     - ✓
     -

   * - 3.7
     - ✓
     - ✓


   * - 3.6
     - ✓
     - ✓

.. [#python-2-compat] Versions of PyMongo 4.0 and later are not compatible
   with Python 2

.. note::

   Jython 2.5 is a Python 2.5-compatible alternative interpreter.
   
   PyPy is a Python 2.7-compatible alternative interpreter.