from typing import NamedTuple


class MessageHeader(NamedTuple):
    """
    Message header struct
    """

    protocol:     int
    message_type: int
    stream_type:  int
    sequence:     int
    size:         int

class ProtocolVersion(NamedTuple):
    """
    Server protocol version struct
    """

    major: int
    minor: int
    patch: int

class DeviceInfo(NamedTuple):
    """
    Device information struct
    """

    device_type:       int
    serial:            int
    max_sample_rate:   int
    max_bandwidth:     int
    decimation_stages: int
    gain_stages:       int
    max_gain:          int
    min_frequency:     int
    max_frequency:     int
    adc_resolution:    int
    min_iq_decimation: int
    forced_iq_format:  int

class ClientSync(NamedTuple):
    """
    Client sync struct
    """

    can_control: int
    gain:        int
    device_cf:   int
    iq_cf:       int
    fft_cf:      int
    min_iq_cf:   int
    max_iq_cf:   int
    min_fft_cf:  int
    max_fft_cf:  int
