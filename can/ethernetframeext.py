from typing import Optional

from .ethernetframe import DirectionFlag
from . import typechecking

class EthernetFrameExt:  # pylint: disable=too-many-instance-attributes; OK for a dataclass

    def __init__(  # pylint: disable=too-many-locals, too-many-arguments
        self,
        timestamp: float = 0.0,
        struct_length: int = 0,
        flags: int = 0,
        channel: Optional[typechecking.Channel] = None,
        hardware_channel: Optional[int] = None,
        duration: Optional[int] = None,
        checksum: Optional[int] = None,
        direction: Optional[DirectionFlag] = None,

        # EtherType indicates the protocol for ethernet payload data 
        ether_type: Optional[bytearray] = None,

        # Number of valid frameData bytes
        length: int = 0,
        # Handle which refer the corresponding EthernetFrameForwarded event
        handle: int = 0,
        # Frame data
        data: Optional[typechecking.CanData] = None
    ):
        self.timestamp = timestamp
        self.struct_length = struct_length
        self.flags = flags
        self.channel = channel
        self.hardware_channel = hardware_channel
        self.duration = duration
        self.checksum = checksum
        self.direction= direction
        self.type = ether_type
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

    def __str__(self) -> str:
        field_strings = [f"ETHFEXT - Timestamp: {self.timestamp:>15.6f}"]
        flag_string = f"flags: {self.flags}"
        field_strings.append(flag_string)


        data_strings = "Data: "
        if self.data is not None:
            data_strings += self.data[: len(self.data)].hex(" ")
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
        if self.direction is not None:
            try:
                field_strings.append(f"Direction: {self.direction}")
            except UnicodeEncodeError:
                pass
        if self.length is not None:
            try:
                field_strings.append(f"Length: {self.length}")
            except UnicodeEncodeError:
                pass
        if self.handle is not None:
            try:
                field_strings.append(f"Handle: {self.handle}")
            except UnicodeEncodeError:
                pass
        if self.checksum is not None:
            try:
                field_strings.append(f"Checksum: {self.checksum}")
            except UnicodeEncodeError:
                pass
        if self.duration is not None:
            try:
                field_strings.append(f"Duration: {self.duration}")
            except UnicodeEncodeError:
                pass
        if self.struct_length is not None:
            try:
                field_strings.append(f"Struct Length: {self.struct_length}")
            except UnicodeEncodeError:
                pass
        


        return "\n".join(field_strings).strip()
