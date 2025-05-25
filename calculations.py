from models import ReadingProgress, ReadingStats, ReadingInfo, ReadingProgress, FinishPrediction
from datetime import datetime, timedelta

def calculate_reading_stats(reading_info: ReadingInfo) -> ReadingStats:
    
    days_passed: int = reading_info.date_range.days_passed()
    months_passed: float = days_passed / 30.44

    days_per_month: float = reading_info.reading_days / months_passed
    pages_per_day_total: float = reading_info.pages_read / days_passed
    pages_per_reading_day: float = reading_info.pages_read / reading_info.reading_days
    
    reading_progress_stats: FinishPrediction = calculate_finish_prediction(
        ReadingProgress(
            reading_info.date_range,
            pages_per_day_total,
            reading_info.total_pages,
            reading_info.pages_read
        )
    )
    
    pages_remaining: int = reading_progress_stats.pages_remaining
    days_to_finish: float = reading_progress_stats.days_to_finish
    estimated_finish_date: datetime = reading_progress_stats.estimated_finish_date
    
    return ReadingStats(
        days_per_month,
        pages_per_day_total,
        pages_per_reading_day,
        pages_remaining,
        days_to_finish,
        estimated_finish_date
    )



def calculate_finish_prediction(finish_prediction: ReadingProgress) -> FinishPrediction:
    
    days_passed: int = finish_prediction.date_range.days_passed()
    pages_per_day_total: float = finish_prediction.pages_read / days_passed
    
    pages_remaining: int = finish_prediction.total_pages - finish_prediction.pages_read
    days_to_finish: float = pages_remaining / pages_per_day_total
    estimated_finish_date: datetime = finish_prediction.date_range.end + timedelta(days=days_to_finish)
    
    return FinishPrediction(
        pages_remaining,
        days_to_finish,
        estimated_finish_date
    )