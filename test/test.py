import time
from spyclient import SpyClient

def init():
    # Create SpyClient instance
    c = SpyClient("127.0.0.1", 5555)

    # Print properties
    print(f"HOST IP:      {c.host}")
    print(f"HOST PORT:    {c.port}")
    print(f"CLIENT NAME:  {c.name}\n")

    # Connect to server
    c.connect()
    if c.connected: print(f"CONNECTED to {c.host}:{c.port}\n")
    
    time.sleep(1)

    # Disconnect from server
    c.disconnect()
    if not c.connected: print("DISCONNECTED")

try:
    init()
except KeyboardInterrupt:
    print("Exiting...")
    exit()
