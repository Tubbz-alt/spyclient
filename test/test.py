import time
from spyclient import SpyClient

def init():
    # Create SpyClient instance
    c = SpyClient("127.0.0.1", 5555)

    # Print properties
    print("HOST IP:      {}".format(c.host))
    print("HOST PORT:    {}".format(c.port))
    print("CLIENT NAME:  {}\n".format(c.name))

    # Connect to server
    c.connect()
    if c.connected: print("CONNECTED to {}:{}\n".format(c.host, c.port))
    
    time.sleep(1)

    # Disconnect from server
    c.disconnect()
    if not c.connected: print("DISCONNECTED")

    exit(0)

try:
    init()
except KeyboardInterrupt:
    print("Exiting...")
    exit(1)
