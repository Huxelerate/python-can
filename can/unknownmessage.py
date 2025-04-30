from typing import Optional
from . import typechecking

class UnknownMessage:
    """
    Class to handle all unsupported messages.
    """

    def __init__(
            self,
            objectType: int = 0,
            timestamp: float = 0.0,
            data: Optional[typechecking.CanData] = None
        ):
        self.objectType = objectType
        self.timestamp = timestamp
        self.data = data

        # if data is None:
        #     self.data = bytearray()
        # elif isinstance(data, bytearray):
        #     self.data = data
        # else:
        #     try:
        #         self.data = bytearray(data)
        #     except TypeError as error:
        #         err = f"Couldn't create message from {data} ({type(data)})"
        #         raise TypeError(err) from error
    def __str__(self) -> str:
        field_strings = [f"UnknownMessage - Timestamp: {self.timestamp:>15.6f}"]
        field_strings.append(f"Data: {self.data}")
        return "\n".join(field_strings)
    
        