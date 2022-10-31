from times import time_range, compute_overlap_time

def test_given_input():
    result = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 4, 60) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:33:00'), ('2010-01-12 10:34:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:41:00'), ('2010-01-12 10:42:00', '2010-01-12 10:45:00')]
    assert result == expected

if __name__ == "__main__":
    test_given_input()
