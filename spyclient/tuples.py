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

    def to_string(self):
        """
        Returns server version as string
        """        
        return f"v{self.major}.{self.minor}.{self.patch}"

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

    def print(self):
        """
        Prints device information
        """

        # Loop through fields in DeviceInfo tuple
        for j in self._fields:
            key = j.replace("_", " ").title()
            key = key.replace("Iq", "IQ")
            key = key.replace("Adc", "ADC") + ":"

            val = getattr(self, j)

            # Value formatting
            if j == "device_type":        val = val.name
            elif j == "max_sample_rate":  val = str(val/1000000) + " Msps"
            elif j == "max_bandwidth":    val = str(val/1000000) + " Msps"
            elif j == "min_frequency":    val = str(val/1000000) + " MHz"
            elif j == "max_frequency":    val = str(val/1000000) + " MHz"
            elif j == "adc_resolution":   val = f"{val} bits"
            elif j == "forced_iq_format": val = bool(val)

            print(f"{key.ljust(20)}{val}")

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
