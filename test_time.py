import times

def test_given_input():
    large = times.time_range("2021-01-12 10:00:00", "2021-01-12 12:00:00")
    short = times.time_range("2021-01-12 10:30:00", "2021-01-12 10:45:00")
    actual = times.compute_overlap_time(large, short)
    expected = [('2021-01-12 10:30:00', '2021-01-12 10:45:00')]
    assert actual == expected
    