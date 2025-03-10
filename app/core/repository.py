from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.core.date_time import Timestamp
from app.core.entities import Timeframe, Security, Candle, Object


@dataclass
class CandleRepositoryRequest:
    security: Security
    timeframe: Timeframe
    time_from: Timestamp
    n_candles: int


@dataclass
class CandlePeriod:
    time_from: Timestamp
    time_till: Timestamp


class IRepository(ABC):

    @abstractmethod
    async def create(self, items: list[Object]):
        pass

    @abstractmethod
    async def update(self, items: list[Object]):
        pass

    @abstractmethod
    async def delete(self, items: list[Object]):
        pass


class ISecurityRepository(IRepository):

    @abstractmethod
    async def all(self) -> list[Security]:
        pass


class ICandleRepository(IRepository):

    @abstractmethod
    async def get_periods(self, security: Security) -> list[CandlePeriod]:
        """
        Get non-overlaping time intervals present in DB.

        Use: no need to load data from these periods from Market Data Source.
        """
        pass

    @abstractmethod
    async def add_period(self, security: Security, period: CandlePeriod):
        """
        Register time interval as present in DB.

        To be used together with saving new candles to DB.
        """
        pass

    @abstractmethod
    async def get(self, request: CandleRepositoryRequest) -> list[Candle]:
        pass
