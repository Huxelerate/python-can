from typing import Optional
from . import typechecking

class EthernetFrameExt:  # pylint: disable=too-many-instance-attributes; OK for a dataclass
    """
   
    """

    def __init__(  # pylint: disable=too-many-locals, too-many-arguments
        self,
        timestamp: float = 0.0,
        is_error_frame: bool = False,
        struct_length: int = 0,
        flags: int = 0,
        channel: Optional[typechecking.Channel] = None,
        hardware_channel: Optional[typechecking.Channel] = None,
        duration: int = None,
        checksum: int = None,
        #Direction flag: 0=Rx, 1=Tx, 2=TxRq
        direction: int = None,
        # Number of valid frameData bytes
        length: int = 0,
        # Handle which refer the corresponding EthernetFrameForwarded event
        handle: int = 0,
        # Frame data
        # TODO: check here typechecking.CanData
        data: Optional[typechecking.CanData] = None,
        rawdata: Optional[typechecking.CanData] = None

    ):
        """
        
        """
        self.timestamp = timestamp
        self.is_error_frame = is_error_frame
        self.struct_length = struct_length
        self.flags = flags
        self.channel = channel
        self.hardware_channel = hardware_channel
        self.duration = duration
        self.checksum = checksum
        self.direction= direction
        self.length = length
        self.handle = handle

        if data is None:
            self.data = bytearray()
        elif isinstance(data, bytearray):
            self.data = data
        else:
            try:
                self.data = bytearray(data)
            except TypeError as error:
                err = f"Couldn't create message from {data} ({type(data)})"
                raise TypeError(err) from error
            
        if rawdata is None:
            self.rawdata = bytearray()
        elif isinstance(rawdata, bytearray):
            self.rawdata = rawdata
        else:
            try:
                self.rawdata = bytearray(rawdata)
            except TypeError as error:
                err = f"Couldn't create message from {rawdata} ({type(rawdata)})"
                raise TypeError(err) from error

    def __str__(self) -> str:
        field_strings = [f"ETHFEXT - Timestamp: {self.timestamp:>15.6f}"]
        # if self.is_extended_id:
        #     arbitration_id_string = f"{self.arbitration_id:08x}"
        # else:
        #     arbitration_id_string = f"{self.arbitration_id:03x}"
        # field_strings.append(f"ID: {arbitration_id_string:>8}")

        # flag_string = " ".join(
        #     [
        #         "X" if self.is_extended_id else "S",
        #         "Rx" if self.is_rx else "Tx",
        #         "E" if self.is_error_frame else " ",
        #         "R" if self.is_remote_frame else " ",
        #         "F" if self.is_fd else " ",
        #         "BS" if self.bitrate_switch else "  ",
        #         "EI" if self.error_state_indicator else "  ",
        #     ]
        # )
        flag_string = f"flags: {self.flags}"

        field_strings.append(flag_string)

        data_strings = ""
        if self.data is not None:
            data_strings = self.data[: len(self.data)].hex(" ")
        if data_strings:  # if not empty
            field_strings.append(data_strings.ljust(24, " "))
        else:
            field_strings.append(" " * 24)

        if (self.data is not None) and (self.data.isalnum()):
            field_strings.append(f"'{self.data.decode('utf-8', 'replace')}'")

        if self.channel is not None:
            try:
                field_strings.append(f"Channel: {self.channel}")
            except UnicodeEncodeError:
                pass
        if self.hardware_channel is not None:
            try:
                field_strings.append(f"Hardware Channel: {self.hardware_channel}")
            except UnicodeEncodeError:
                pass


        return "    ".join(field_strings).strip()
