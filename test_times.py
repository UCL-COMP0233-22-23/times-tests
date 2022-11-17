from .times import compute_overlap_time,time_range

def test_given_input():
    if __name__ == "__main__":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00",3, 120)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:33:40'), ('2010-01-12 10:35:40', '2010-01-12 10:39:20'), ('2010-01-12 10:41:20', '2010-01-12 10:45:00')]
    assert result == expected