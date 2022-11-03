from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_non_overlapping_time():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2012-01-12 10:00:00", "2012-01-12 12:00:00")
    expected = None
    assert compute_overlap_time(range1, range2) == expected

# def test_several_intervals_time():
#     range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2)
#     range2 = time_range("2012-01-12 10:00:00", "2012-01-12 12:00:00", 3)

def test_backward_time_range():
    time_range("2012-01-12 10:00:00", "2010-01-12 12:00:00")
