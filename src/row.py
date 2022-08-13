from numpy._typing import NDArray

from src.common_datatypes import Time


class Row:
    layer: int
    start: Time
    end: Time
    style: Time
    name: str
    margin: NDArray[float]
    effect: str
    text: str
