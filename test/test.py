from spyclient import SpyClient

def init():
    # Create SpyClient instance
    c = SpyClient("127.0.0.1", 5555)

    # Print properties
    print(f"HOST IP:      {c.host}")
    print(f"HOST PORT:    {c.port}")
    print(f"CLIENT NAME:  {c.name}")


try:
    init()
except KeyboardInterrupt:
    print("Exiting...")
    exit()
