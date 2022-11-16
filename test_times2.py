from times import time_range
from times import compute_overlap_time
import pytest

large1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
short1 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
large3 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
short3 = time_range("2010-01-12 11:30:00", "2010-01-12 12:45:00", 2, 60)

large2 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
short2 = time_range("2010-01-12 13:30:00", "2010-01-12 13:45:00", 2, 60)

@pytest.mark.parametrize("test_input,expected",[(compute_overlap_time(large1,short1),[('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),(compute_overlap_time(large3, short3),[("2010-01-12 11:30:00", "2010-01-12 12:00:00")])])
def test_compute_overlap_time(test_input, expected):
    assert test_input == expected