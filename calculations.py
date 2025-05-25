from models import ReadingStats, ReadingInfo
from datetime import datetime, timedelta

def calculate_reading_stats(reading_info: ReadingInfo) -> ReadingStats:
    
    days_passed: int = reading_info.date_range.days_passed()
    months_passed: float = days_passed / 30.44

    days_per_month: float = reading_info.reading_days / months_passed
    pages_per_day_total: float = reading_info.pages_read / days_passed
    pages_per_reading_day: float = reading_info.pages_read / reading_info.reading_days

    pages_remaining: int = reading_info.total_pages - reading_info.pages_read
    days_to_finish: float = pages_remaining / pages_per_day_total
    estimated_finish_date: datetime = reading_info.date_range.end + timedelta(days=days_to_finish)

    return ReadingStats(
        days_per_month,
        pages_per_day_total,
        pages_per_reading_day,
        pages_remaining,
        days_to_finish,
        estimated_finish_date
    )
