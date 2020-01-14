# SpyServer Client for Python

[![GitHub license](https://img.shields.io/github/license/sam210723/spyclient.svg)](https://github.com/sam210723/spyclient/master/LICENSE)

**SpyClient** is a Python-based client for [Airspy SpyServer](https://airspy.com).


## Getting Started
To connect to SpyServer at the default address of ``127.0.0.1:5555``, create a new instance of ``SpyClient()`` and call ``.connect()``.

```
client = SpyClient()
client.connect()
```

Server address, server port, and client name can be be set using the constructor.

```
host = "127.0.0.1"
port = 5555
name = "SpyClient for Python"

client = SpyClient(host, port, name)
client.connect()
```

Client properties can also be set after initialisation.

```
client = SpyClient()

client.host = "127.0.0.1"
client.port = 5555
client.name = "SpyClient for Python"

client.connect()
```
