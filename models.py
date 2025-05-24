from dataclasses import dataclass
from datetime import datetime

@dataclass
class ReadingStats:
    days_per_month: float
    pages_per_day_total: float
    pages_per_reading_day: float
    pages_remaining: int
    days_to_finish: float
    estimated_finish_date: datetime