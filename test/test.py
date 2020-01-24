import os
from socket import gethostbyname
from spyclient import SpyClient
import sys
import time

def init():
    # Get IP of test SpyServer
    host = "vksdr.com"
    ip = gethostbyname(host)
    #ip = "127.0.0.1"

    # Create SpyClient instance
    c = SpyClient(ip, 5555)

    # Check for Travis CI environment
    try:
        os.environ['TRAVIS']
        print("Detected Travis CI environment")
        
        ver = sys.version.split(" ")[0]
        job = os.environ['TRAVIS_JOB_NUMBER']
        c.name = f"Travis CI #{job} (Python {ver})"
    except KeyError:
        pass

    # Print properties
    print("HOST:         {}".format(host))
    print("HOST IP:      {}".format(c.host))
    print("HOST PORT:    {}".format(c.port))
    print("CLIENT NAME:  {}\n".format(c.name))

    # Connect to server
    c.connect()
    if c.connected: print(f"CONNECTED to {c.host}:{c.port}\n")
    
    time.sleep(2)
    print(f"Server Version:     {c.server_ver.to_string()}\n")
    c.print_device_info()

    # Disconnect from server
    time.sleep(0.5)
    c.disconnect()
    if not c.connected: print("\nDISCONNECTED")

    exit(0)

try:
    init()
except KeyboardInterrupt:
    print("Exiting...")
    exit(1)
