import struct
from enum import Enum


class CommandType(Enum):
    """
    Command types supported by SpyServer.
    """

    HELLO = struct.pack('<I', 0)    #: Send client name to server and begin connection setup
    GET   = struct.pack('<I', 1)    #: Get setting value from server
    SET   = struct.pack('<I', 2)    #: Set setting value on server
    PING  = struct.pack('<I', 3)    #: Check server is alive by requesting a ping response

class MessageType(Enum):
    """
    Message types sent by SpyServer.
    """

    DEVICE_INFO  = 0                #: Properties of the SDR attached to SpyServer (see `DeviceInfo <tuples.html#spyclient.tuples.DeviceInfo>`_)
    CLIENT_SYNC  = 1                #: Current state of SpyServer used to synchronise the client instance with the server (see `ClientSync <tuples.html#spyclient.tuples.ClientSync>`_)
    PONG         = 2                #: Reponse to a PING command (see `CommandType.PING <enums.html#spyclient.enums.CommandType.PING>`_)
    READ_SETTING = 3                #: Reponse to a GET command (see `CommandType.GET <enums.html#spyclient.enums.CommandType.GET>`_)
    UINT8_IQ     = 100              #: Unsigned 8-bit integer IQ sample
    INT16_IQ     = 101              #: Signed 16-bit integer IQ sample
    INT24_IQ     = 102              #: Signed 24-bit integer IQ sample
    FLOAT_IQ     = 103              #: 32-bit float IQ sample
    UINT8_AF     = 200              #: Unsigned 8-bit integer audio sample
    INT16_AF     = 201              #: Signed 16-bit integer audio sample
    INT24_AF     = 202              #: Signed 24-bit integer audio sample
    FLOAT_AF     = 203              #: 32-bit float audio sample
    DINT4_FFT    = 300              #: 4-bit integer FFT data
    UINT8_FFT    = 301              #: 8-bit integer FFT data

class DeviceType(Enum):
    """
    Device types supported by SpyServer.
    """

    INVALID    = 0                  #: Invalid or missing device
    AIRSPY_ONE = 1                  #: Airspy Mini or R2
    AIRSPY_HF  = 2                  #: Airspy HF+ Dual Port or HF+ Discovery
    RTLSDR     = 3                  #: RTL-SDR R820T/T2

class SettingType(Enum):
    """
    Setting types supported by SpyServer.
    """

    STREAMING_MODE     = struct.pack('<I', 0)           #: Select stream type (see `StreamType <enums.html#spyclient.enums.StreamType>`_ enum)
    STREAMING_ENABLED  = struct.pack('<I', 1)           #: Start and stop streaming of IQ/FFT/AF data
    GAIN               = struct.pack('<I', 2)           #: Device gain (see `DeviceInfo.max_gain <tuples.html#spyclient.tuples.DeviceInfo.max_gain>`_)
    IQ_FORMAT          = struct.pack('<I', 100)         #: IQ stream format (see `StreamFormat <enums.html#spyclient.enums.StreamFormat>`_)
    IQ_FREQUENCY       = struct.pack('<I', 101)         #: IQ center frequency
    IQ_DECIMATION      = struct.pack('<I', 102)         #: IQ decimation factor
    IQ_DIGITAL_GAIN    = struct.pack('<I', 103)         #: IQ offset
    FFT_FORMAT         = struct.pack('<I', 200)         #: FFT data type (`DINT4 <enums.html#spyclient.enums.MessageType.DINT4_FFT>`_ or `UINT8 <enums.html#spyclient.enums.MessageType.UINT8_FFT>`_)
    FFT_FREQUENCY      = struct.pack('<I', 201)         #: FFT center frequency
    FFT_DECIMATION     = struct.pack('<I', 202)         #: FFT decimation factor
    FFT_DB_OFFSET      = struct.pack('<I', 203)         #: FFT offset (dB)
    FFT_DB_RANGE       = struct.pack('<I', 204)         #: FFT range (dB)
    FFT_DISPLAY_PIXELS = struct.pack('<I', 205)         #: FFT bins

class StreamMode(Enum):
    """
    Streaming modes supported by SpyServer.
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
