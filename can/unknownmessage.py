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

    def __str__(self) -> str:
        field_strings = [f"UnknownMessage - Timestamp: {self.timestamp:>15.6f}"]
        field_strings.append(f"Data: {self.data}")
        return "\n".join(field_strings)
    
        