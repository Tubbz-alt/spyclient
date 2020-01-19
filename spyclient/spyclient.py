"""
spyclient.py
https://github.com/sam210723/spyclient

Airspy SpyServer client implementation for Python 3
"""

import ipaddress
from select import select
import socket
import struct
import threading
from . import enums, tuples

## Constants
PACKAGE_VER = "1.0"             # Python package version
PROTOCOL_VER = 0x20006A4        # Protocol implementation version
DEFAULT_HOST = "127.0.0.1"      # Default socket host
DEFAULT_PORT = 5555             # Default socket port
TIMEOUT = 2                     # Socket read timeout (sec)


class SpyClient:
    """
    Airspy SpyServer client implementation for Python 3.
    :param host: SpyServer host IP address (127.0.0.1)
    :param port: SpyServer TCP port (5555)
    """

    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT):
        # Properties
        self.host = host                # SpyServer IP address
        self.port = port                # SpyServer TCP port
        self.name = "SpyClient for Python v{}".format(PACKAGE_VER)

        # Flags
        self.connected = False          # Client connected to server
        self.rx_stop = False            # Stop socket receive thread


    #region Protocol Functions
    def say_hello(self):
        """
        Say hello to server
        """

        # Protocol version as unsigned little-endian integer
        ver = struct.pack('<I', PROTOCOL_VER)

        # Get bytes from client name
        client = self.name.encode('UTF-8')

        # Send version and client name to server
        body = ver + client        
        self.send_command(enums.CommandType.HELLO.value, body)
    
    def send_command(self, cmd, body):
        """
        Sends command packet to server
        :param cmd: Command type
        :param body: Command body bytes
        """

        # Assemble command header
        length = struct.pack('<I', len(body))
        header = cmd + length

        # Send command to server
        command = header + body
        self.send(command)
    #endregion


    #region Socket Functions
    def recv_loop(self):
        """
        Socket receive thread
        """

        while not self.rx_stop:
            # Block thread until socket is ready for reading
            rx, tx, err = select([ self.sck ], [], [], TIMEOUT)

            # Socket has data available
            if rx:
                # Get message header
                header = self.recv()

                # Ignore bool len exception
                if type(header) == bool:
                    continue

                # Message header is empty
                if header == b'':
                    self.disconnect()
                    raise PermissionError("SpyServer could not find/acquire a device")
    
    def connect(self):
        """
        Connect to SpyServer
        """

        # Validate IP address
        try:
            ipaddress.ip_address(self.host)
        except ValueError:
            raise

        # Validate port
        if not (1023 < self.port < 65536):
            raise ValueError("Host port \"{}\" is invalid".format(self.port))

        # Create and configure socket
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sck.settimeout(TIMEOUT)

        try:
            self.sck.connect((self.host, self.port))
        except socket.error:
            raise

        #TODO: Set flag after handling client sync and device info
        self.connected = True

        # Setup and start socket receive thread
        self.rx_thread = threading.Thread()
        self.rx_thread.name = "SpyClient Socket Receiver"
        self.rx_thread.run = self.recv_loop
        self.rx_thread.start()

        self.say_hello()

        return True

    def disconnect(self):
        """
        Disconnect from SpyServer
        """

        self.rx_stop = True
        self.sck.close()
        self.connected = False

    def send(self, data):
        """
        Send data to server
        """

        if not self.connected: return False
        self.sck.send(data)

    def recv(self, length=20):
        """
        Receive data from server
        """

        if not self.connected: return False
        
        try:
            return self.sck.recv(length)
        except:
            return None
    #endregion
