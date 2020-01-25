from typing import NamedTuple


class MessageHeader(NamedTuple):
    """
    Message header struct
    """

    protocol:     int           #: Server protocol version (see `ProtocolVersion <tuples.html#spyclient.tuples.ProtocolVersion>`_)
    message_type: int           #: Server protocol version (see `MessageType <enums.html#spyclient.enums.MessageType>`_)
    stream_type:  int           #: Server protocol version (see `StreamType <enums.html#spyclient.enums.StreamType>`_)
    sequence:     int           #: Message continuity counter
    size:         int           #: Message length

class ProtocolVersion(NamedTuple):
    """
    Server protocol version struct
    """

    major: int                  #: Major version number
    minor: int                  #: Minor version number
    patch: int                  #: Patch number

    def to_string(self):
        """
        Returns server version as string in the format ``"v[MAJOR].[MINOR].[PATCH]"``
        """        
        return f"v{self.major}.{self.minor}.{self.patch}"

class DeviceInfo(NamedTuple):
    """
    Device information struct
    """

    device_type:       int      #: Type of SDR attached to SpyServer (see `DeviceType <enums.html#spyclient.enums.DeviceType>`_)
    serial:            int      #: Serial number of SDR
    max_sample_rate:   int      #: Maximum sample rate of device (Sps)
    max_bandwidth:     int      #: Maximum bandwidth of device (Hz)
    decimation_stages: int      #: 
    gain_stages:       int      #: 
    max_gain:          int      #: Maximum gain value
    min_frequency:     int      #: Minimum frequency (Hz)
    max_frequency:     int      #: Maximum frequency (Hz)
    adc_resolution:    int      #: Analog-to-digital converter bit-depth (bits)
    min_iq_decimation: int      #: Minimum IQ decimation factor
    forced_iq_format:  bool     #: Is server forcing 8-bit IQ only stream

    def print(self):
        """
        Prints device information to stdout
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
        print()

class ClientSync(NamedTuple):
    """
    Client sync struct
    """

    can_control: bool           #: Does client have control of server settings
    gain:        int            #: Current device gain value (see `DeviceInfo.max_gain <tuples.html#spyclient.tuples.DeviceInfo.max_gain>`_)
    device_cf:   int            #: Current device center frequency (Hz)
    iq_cf:       int            #: Current IQ center frequency (Hz)
    fft_cf:      int            #: Current FFT center frequency (Hz)
    min_iq_cf:   int            #: Minimum IQ center frequency (Hz)
    max_iq_cf:   int            #: Maximum IQ center frequency (Hz)
    min_fft_cf:  int            #: Minimum FFT center frequency (Hz)
    max_fft_cf:  int            #: Maximum FFT center frequency (Hz)

    def print(self):
        """
        Prints client sync information to stdout
        """

        # Loop through fields in ClientSync tuple
        for j in self._fields:
            key = j.replace("_", " ").title()
            key = key.replace("Iq", "IQ")
            key = key.replace("Fft", "FFT")
            key = key.replace("Cf", "CF") + ":"

            val = getattr(self, j)

            # Readable device type
            if j == "can_control": val = True if val else False
            if j != "gain" and j != "can_control": val = str(val/1000000) + " MHz"

            print("{}{}".format(key.ljust(20), val))
        print()
