from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class ReadingStats:
    days_per_month: float
    pages_per_day_total: float
    pages_per_reading_day: float
    pages_remaining: int
    days_to_finish: float
    estimated_finish_date: datetime

    
@dataclass(frozen=True)
class FinishPrediction:
    pages_remaining: int
    days_to_finish: float
    estimated_finish_date: datetime
    
@dataclass(frozen=True)
class DateRange:
    start: datetime
    end: datetime
    
    def __post_init__(self) -> None:
        if self.start.timestamp() > self.end.timestamp():
            raise ValueError(
                f"La fecha inicial ({self.start}) es mayor a la fecha de hoy ({self.end})."
                )
    
    def days_passed(self) -> int:
        return (self.end - self.start).days

@dataclass(frozen=True)
class ReadingInfo:
    date_range: DateRange
    pages_read: int
    reading_days: int
    total_pages: int

@dataclass(frozen=True)
class ReadingProgress:
    date_range: DateRange
    pages_per_day_total: float
    total_pages: int
    pages_read: int