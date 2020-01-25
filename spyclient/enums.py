import struct
from enum import Enum


class CommandType(Enum):
    """
    Command types
    """

    HELLO = struct.pack('<I', 0)   # Say hello to server
    GET   = struct.pack('<I', 1)   # Get setting from server
    SET   = struct.pack('<I', 2)   # Set setting on server
    PING  = struct.pack('<I', 3)   # Check server is alive

class MessageType(Enum):
    """
    Message types
    """

    DEVICE_INFO  = 0
    CLIENT_SYNC  = 1
    PONG         = 2
    READ_SETTING = 3
    UINT8_IQ     = 100
    INT16_IQ     = 101
    INT24_IQ     = 102
    FLOAT_IQ     = 103
    UINT8_AF     = 200
    INT16_AF     = 201
    INT24_AF     = 202
    FLOAT_AF     = 203
    DINT4_FFT    = 300
    UINT8_FFT    = 301

class DeviceType(Enum):
    """
    Device types
    """

    INVALID    = 0
    AIRSPY_ONE = 1
    AIRSPY_HF  = 2
    RTLSDR     = 3

class SettingType(Enum):
    STREAMING_MODE     = struct.pack('<I', 0)
    STREAMING_ENABLED  = struct.pack('<I', 1)
    GAIN               = struct.pack('<I', 2)
    IQ_FORMAT          = struct.pack('<I', 100)
    IQ_FREQUENCY       = struct.pack('<I', 101)
    IQ_DECIMATION      = struct.pack('<I', 102)
    IQ_DIGITAL_GAIN    = struct.pack('<I', 103)
    FFT_FORMAT         = struct.pack('<I', 200)
    FFT_FREQUENCY      = struct.pack('<I', 201)
    FFT_DECIMATION     = struct.pack('<I', 202)
    FFT_DB_OFFSET      = struct.pack('<I', 203)
    FFT_DB_RANGE       = struct.pack('<I', 204)
    FFT_DISPLAY_PIXELS = struct.pack('<I', 205)
class StreamType(Enum):
    """
    Stream types supported by SpyServer.
    """

    IQ_ONLY  = 1                    #: Only receive an IQ stream from server
    AF_ONLY  = 2                    #: Only receive an audio stream from server
    FFT_ONLY = 4                    #: Only receive an FFT data from server
    FFT_IQ   = 5                    #: Receive both FFT data and an IQ stream from server
    FFT_AF   = 6                    #: Receive both FFT data and an audio stream from server

class StreamType(Enum):
    """
    Stream types supported by SpyServer.
    """

    STATUS = 0                      #: 
    IQ = 1                          #: IQ stream
    AF = 2                          #: Audio stream
    FFT = 4                         #: FFT data

class StreamFormat(Enum):
    """
    IQ, AF and FFT stream types supported by SpyServer.
    """

    INVALID = 0                     #: Invalid stream type
    UINT8 = 1                       #: Unsigned 8-bit integer
    INT16 = 2                       #: Signed 16-bit integer
    INT24 = 3                       #: Signed 24-bit integer
    FLOAT = 4                       #: 32-bit float
    DINT4 = 5                       #: 4-bit integer
