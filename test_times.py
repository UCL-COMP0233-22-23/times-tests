# Test Times File

from times import compute_overlap_time
from times import time_range
import pytest

def test_subset_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2)
    result = compute_overlap_time(large, short)    
    expected = 15.0*60.0
    assert result == expected
    
def test_partial_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:40:00", 2)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2)

    result = compute_overlap_time(large, short)    
    expected = 10.0*60.0
    assert result == expected
    
def test_vanishing_overlap():
    large = time_range("2010-01-12 10:45:00", "2010-01-12 12:00:00", 2)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2)

    result = compute_overlap_time(large, short)    
    expected = 0.0
    assert result == expected

def test_zero_overlap():
    large = time_range("2010-01-12 12:00:00", "2010-01-12 12:00:00", 2)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2,)

    result = compute_overlap_time(large, short)    
    expected = 0.0
    assert result == expected
    
def test_input_values():
    with pytest.raises(ValueError):
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2)
        short = time_range("2010-01-12 10:50:00", "2010-01-12 10:45:00", 2)
        result = compute_overlap_time(large, short)

# Forgot to mention Answers UCL-COMP0233-22-23/RSE-Classwork#19
