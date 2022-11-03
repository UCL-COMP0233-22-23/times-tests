from times import time_range, compute_overlap_time
from pytest import raises

"""create a test each in test_times.py for:

 - two time ranges that do not overlap
 - two time ranges that both contain several intervals each
 - two time ranges that end exactly at the same time when the other starts
"""
def test_given_input():
    result = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 4, 60) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:33:00'), ('2010-01-12 10:34:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:41:00'), ('2010-01-12 10:42:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_several_intervals():
    intervals_1 = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 2, 60) 
    intervals_2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 2, 60) 
    print(compute_overlap_time(intervals_1, intervals_2))
    assert compute_overlap_time(intervals_1, intervals_2) == [('2010-01-12 11:00:30', '2010-01-12 11:29:30')]

def test_perfect_overlap():
    intervals_1 = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 1, 0) 
    intervals_2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 1, 0) 
    assert compute_overlap_time(intervals_1, intervals_2) == [('2010-01-12 10:30:00', '2010-01-12 11:30:00')]

def test_invalid_inputs():
    with raises(ValueError):
        time_range("2010-01-12 10:30:00", "2010-01-12 09:30:00", 1, 0)

if __name__ == "__main__":
    test_given_input()
    #test_several_intervals()
    test_invalid_inputs()

