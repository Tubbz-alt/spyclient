"""
spyclient.py
https://github.com/sam210723/spyclient

Airspy SpyServer client implementation for Python 3
"""

from . import enums, tuples


## Constants
PACKAGE_VER = "1.0"             # Python package version
PROTOCOL_VER = 0x2000638        # Protocol implementation version
DEFAULT_HOST = "127.0.0.1"      # Default socket host
DEFAULT_PORT = 5555             # Default socket port
TIMEOUT = 2                     # Socket read timeout (sec)
DEFAULT_NAME = f"SpyClient for Python v{PACKAGE_VER}"


class SpyClient:
    """
    Airspy SpyServer client implementation for Python 3.
    :param host: SpyServer host IP address (127.0.0.1)
    :param port: SpyServer TCP port (5555)
    """

    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT, name=DEFAULT_NAME):
        self.host = host                # SpyServer host IP address
        self.port = port                # SpyServer TCP port
        self.addr = (host, port)        # SpyServer address tuple
        self.name = name                # SpyClient name
