"""
spyclient.py
https://github.com/sam210723/spyclient

Airspy SpyServer client implementation for Python 3
"""

from . import enums, tuples


## Constants
PACKAGE_VER = "1.0"             # Python package version
PROTOCOL_VER = 0x2000638        # Protocol implementation version
DEF_HOST = "127.0.0.1"          # Default socket host
DEF_PORT = 5555                 # Default socket port
TIMEOUT = 2                     # Socket read timeout (sec)


class SpyClient:
    """
    Airspy SpyServer client implementation for Python 3.
    :param host: SpyServer host IP address (127.0.0.1)
    :param port: SpyServer TCP port (5555)
    """

    def __init__(self, host=DEF_HOST, port=DEF_PORT):
        return
