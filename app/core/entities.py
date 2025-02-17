from dataclasses import dataclass
from enum import Enum

from app.core.date_time import Timestamp


class Timeframe(Enum):

    M1 = "M1"
    M10 = "M10"
    H1 = "H1"


@dataclass
class Object:
    pass


@dataclass
class Security(Object):

    ticker: str
    board: str


@dataclass
class Candle(Object):

    security: Security
    timeframe: Timeframe
    timestamp: Timestamp
    open: float
    high: float
    low: float
    close: float
