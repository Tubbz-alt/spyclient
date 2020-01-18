# SpyServer Client

[![Build Status](https://travis-ci.org/sam210723/spyclient.svg?branch=master)](https://travis-ci.org/sam210723/spyclient)
[![GitHub license](https://img.shields.io/github/license/sam210723/spyclient.svg)](https://github.com/sam210723/spyclient/master/LICENSE)

**SpyClient** is a client implementation of the [Airspy SpyServer](https://airspy.com) protocol for Python 3. **SpyServer** is purpose-built server software for accessing Software Defined Radio hardware over a network.


## Getting Started
**SpyClient** will be published to PyPI upon ``v1.0`` release.

The current development version of **SpyClient** can be installed by cloning this repository then running ``make install``. To test changes without having to reinstall the package use ``make develop`` instead. Check the [``Makefile``](Makefile) for more options.

### Connecting
The default host address used by **SpyClient** is ``127.0.0.1:5555``. To connect to a server at this address, create a new instance of ``SpyClient()`` and call ``.connect()``.

```python
client = SpyClient()
client.connect()
```

A different host address can be specified using arguments of the ``SpyClient()`` constructor.

```python
host = "127.0.0.1"
port = 5555

client = SpyClient(host, port)
client.connect()
```

The host address can also be set after initialisation using the ``.host`` and ``.port`` properties.

```python
client = SpyClient()
client.host = "127.0.0.1"
client.port = 5555

client.connect()
```
