from spyclient import SpyClient

def init():
    c = SpyClient("127.0.0.1", 5555)


try:
    init()
except KeyboardInterrupt:
    print("Exiting...")
    exit()
