from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.core.date_time import Timestamp
from app.core.entities import Security, Timeframe
from app.core.market_data_adapter import IMarketDataAdapter
from app.core.repository import ICandleRepository


@dataclass
class MarketDataLoaderRequest:
    security: Security
    timeframe: Timeframe
    time_from: Timestamp
    time_till: Timestamp


class IMarketDataLoader(ABC):

    @abstractmethod
    def __init__(
        self,
        market_data_adapter: IMarketDataAdapter,
        candle_repository: ICandleRepository,
    ):
        pass

    @abstractmethod
    def load_candles(self, request: MarketDataLoaderRequest):
        pass
