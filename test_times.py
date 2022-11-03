from times import time_range
from times import compute_overlap_time

def test_time_given_input():

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    #print(compute_overlap_time(large, short))
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

    #two time ranges do not overlap
    large2 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short2 = time_range("2010-01-12 13:30:00", "2010-01-12 13:45:00", 2, 60)
    #print(compute_overlap_time(large, short))
    result2 = compute_overlap_time(large, short)
    expected2 = []
    assert result2 == expected2

    #two time ranges that both contain several intervals each
    large3 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short3 = time_range("2010-01-12 11:30:00", "2010-01-12 12:45:00", 2, 60)
    #print(compute_overlap_time(large, short))
    result3 = compute_overlap_time(large, short)
    expected3 = [("2010-01-12 11:30:00", "2010-01-12 11:44:00"),("2010-01-12 11:45:00", "2010-01-12 12:00:00")]
    assert result3 == expected3

    #two time ranges that end exactly at the same time when the other starts
    large4 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short4 = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00", 2, 60)
    #print(compute_overlap_time(large, short))
    result4 = compute_overlap_time(large, short)
    expected4 = []
    assert result4 == expected4