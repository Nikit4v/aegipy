from enum import Enum

from pydantic import validator, ValidationError, Field

from .common_datatypes import BaseModel
import numpy as np
from numpy.typing import ArrayLike, DTypeLike, NDArray


class BorderStyle(Enum):
    Normal = 1
    Opaque = 3


class Style(BaseModel):
    name: str
    fontname: str
    fontsize: float
    primary_color: NDArray[float | int]
    secondary_colour: NDArray[float | int]
    outline_colour: NDArray[float | int]
    background_colour: NDArray[float | int]
    italic: bool
    bold: bool
    underline: bool
    strike_out: bool
    scale: NDArray[float]
    spacing: float
    angle: float
    border_style: BorderStyle
    outline: float
    shadow: float
    alignment: int
    margin: NDArray[float]
    encoding: int  # It is probably make sense, but in fact... nobody can explain meaning of this field

    @property
    def ibus(self) -> (bool, bool, bool, bool):
        """
        Function to get italic, bold, underline and strikeout in one time.

        :return: Tuple with 4 bools: italic, bold, underline and strikeout (in this order)
        """
        return self.italic, self.bold, self.underline, self.strike_out

    @validator("scale", pre=True)
    def validate_ndarray(cls, v):
        match v:
            case (x, y):
                return np.array([x, y])
            case np.ndarray():
                if len(v.shape) == 1 and v.shape[0] > 1:
                    v: np.ndarray
                    return v[:2].copy()
                else:
                    raise ValueError("Invalid ndarray shape")
            case list():
                if len(v) < 2:
                    raise ValueError("Invalid list shape")
                return np.ndarray(v[:2])

    @validator("primary_color", "secondary_colour", "outline_colour", "background_colour", pre=True)
    def validate_color(cls, v):
        match v:
            case (r, g, b):
                if isinstance(r, float) and isinstance(g, float) and isinstance(b, float):
                    return np.array([r, g, b, 0.])
                if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
                    return np.array([r, g, b, 0])
                raise ValueError("Invalid color format")
            case (r, g, b, a):
                if type(r) == type(g) == type(b) == type(a):
                    return np.array([r, g, b, a])
                raise ValueError("Invalid color format")
            case np.ndarray():
                if len(v.shape) == 1 and v.shape[0] > 3:
                    v: np.ndarray
                    return v[:4].copy()
                else:
                    raise ValueError("Invalid ndarray shape")
            case list():
                if len(v) < 4:
                    raise ValueError("Invalid list shape")
                return np.ndarray(v[:4])
