from times import compute_overlap_time
from times import time_range

def test_given_input():
    if __name__ == "__main__":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")

        short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
        print(compute_overlap_time(large, short))
    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected
#function pass the test


def test_no_overlap():
    if __name__ == "__main__":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")

        short = time_range("2011-01-12 10:30:00", "2011-01-12 10:45:00")
        print(compute_overlap_time(large, short))
    result = compute_overlap_time(large, short) 
    expected = []
    assert result == expected
test_no_overlap()
#error reported. function cannot handle time with no overlap
#after edit, it pass the test