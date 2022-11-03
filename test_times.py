from times import time_range, compute_overlap_time

def test_given_input():
    #standard case
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    result = compute_overlap_time(large, short)
    expected = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    assert result == expected

def test_given_input():
    #two time ranges no overlap
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:01:00")
    short = time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_given_input():
    #two time ranges that contains several intervals each
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:31:00", 2, 60)
    short = time_range("2010-01-12 10:15:00", "2010-01-12 10:46:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = time_range[(("2010-01-12 10:15:00", "2010-01-12 10:31:00"), ("2010-01-12 10:31:00", "2010-01-12 10:46:00"))]

def test_given_input():
    #one ends and one starts at the same time
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:31:00")
    short = time_range("2010-01-12 10:31:00", "2010-01-12 10:46:00")
    result = compute_overlap_time(large, short)
    expected = ["2010-01-12 10:31:00", "2010-01-12 10:31:00"]
    assert result == expected

