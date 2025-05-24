from models import ReadingStats
from datetime import datetime, timedelta

def calculate_stats(start_date: datetime, end_date: datetime, pages_read: int,
                    reading_days: int, total_pages: int) -> ReadingStats:
    
    days_passed: int = (end_date - start_date).days
    months_passed: float = days_passed / 30.44

    days_per_month: float = reading_days / months_passed
    pages_per_day_total: float = pages_read / days_passed
    pages_per_reading_day: float = pages_read / reading_days

    pages_remaining: int = total_pages - pages_read
    days_to_finish: float = pages_remaining / pages_per_day_total
    estimated_finish_date: datetime = end_date + timedelta(days=days_to_finish)

    return ReadingStats(
        days_per_month,
        pages_per_day_total,
        pages_per_reading_day,
        pages_remaining,
        days_to_finish,
        estimated_finish_date
    )
