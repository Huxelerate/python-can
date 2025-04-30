from enum import Enum
from typing import Optional
from . import typechecking

class DirectionFlag(Enum):
    """The state in which ethernetFrame dir can be"""

    Rx = 0
    Tx = 1
    TxRq = 2

class EthernetFrame:
    """

    """

    def __init__( 
        self,
        timestamp: float = 0.0,
        source_address: Optional[bytearray] = None,
        channel: Optional[typechecking.Channel] = None,
        destination_address: Optional[bytearray] = None,
        direction: DirectionFlag = None,
        
        # EtherType indicates the protocol for ethernet payload data 
        type: Optional[bytearray] = None,

        # TPID when VLAN tag valid, zero when no
        # VLAN. See Ethernet standard specification.
        tpid: Optional[int] = 0,

        # TCI when VLAND tag valid, zero when no
        # VLAN. See Ethernet standard specification.
        tci: Optional[int] = 0,

        payloadLength: int = 0,
        # TODO: check here typechecking.CanData
        data: Optional[typechecking.CanData] = None,

        rawdata: Optional[typechecking.CanData] = None

    ): 
        self.timestamp = timestamp
        self.source_address = source_address
        self.channel = channel
        self.destination_address = destination_address
        self.direction = direction
        self.type = type
        self.tpid = tpid
        self.tci = tci
        self.payloadLength = payloadLength

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
        field_strings = [f"ETHF - Timestamp: {self.timestamp:>15.6f}"]
        field_strings.append(f"Source Address: {self.source_address}")
        field_strings.append(f"Destination Address: {self.destination_address}")
        field_strings.append(f"Direction: {self.direction}")
        field_strings.append(f"EtherType: {self.type}")
        field_strings.append(f"TPID: {self.tpid}")
        field_strings.append(f"TCI: {self.tci}")
        field_strings.append(f"Payload Length: {self.payloadLength}")
        field_strings.append(f"Data: {self.data}")
        field_strings.append(f"Raw Data: {self.rawdata}")
       
        return "\n".join(field_strings)