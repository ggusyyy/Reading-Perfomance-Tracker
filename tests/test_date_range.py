from datetime import datetime
import unittest

from models import DateRange


class TestDateRange(unittest.TestCase):

    def test_it_works(self) -> None:
        date_range = DateRange(
            datetime(2025, 1, 1),
            datetime(2025, 1, 31)
        )
        days_passed = date_range.days_passed()
        self.assertEqual(days_passed, 30)
    
    def test_it_fails_if_start_is_after_end(self) -> None:
        with self.assertRaises(ValueError):
            DateRange(
                datetime(2025, 1, 1),
                datetime(2024, 1, 1)
            )


if __name__ == '__main__':
    unittest.main()
