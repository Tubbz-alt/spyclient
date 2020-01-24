SpyClient Documentation
=====================================

SpyClient is a client implementation of the `Airspy SpyServer <https://airspy.com>`_ protocol for Python 3.
SpyServer is purpose-built server software for accessing Software Defined Radio hardware over a network.


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   spyclient
   tuples
   enums


Getting Started
=====================================

To use **SpyClient** in your Python code, import the SpyClient class from the spyclient module:

.. code-block:: python

    from spyclient import SpyClient


Next, create a new instance of the ``SpyClient()`` class:

.. code-block:: python

    client = SpyClient()


By default SpyClient will try connect to a SpyServer running on the same host (``127.0.0.1:5555``).
If this is not the case, the server host and port can be specified when creating a ``SpyClient()`` instance:

.. code-block:: python

    client = SpyClient("127.0.0.1", 5555)


Alternatively, the server host and port can be specified after ``SpyClient()`` is initialised:

.. code-block:: python

    client = SpyClient()
    client.host = "127.0.0.1"
    client.port = 5555
