from times import compute_overlap_time, time_range
from pytest import raises
import pytest

# def test_given_input():
#     outer = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     inner = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     result = compute_overlap_time(outer, inner)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#     assert result == expected

# def test_nooverlap():
#     first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     second = time_range("2010-01-12 09:30:00", "2010-01-12 09:45:00")
#     result = compute_overlap_time(first, second)
#     expected = []
#     assert result == expected

# def test_multipleintervals():
#     first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3, 10)
#     second = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     result = compute_overlap_time(first, second)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:39:53'), ('2010-01-12 10:40:03', '2010-01-12 10:45:00')]
#     assert result == expected

# def test_border():
#     first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     second = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
#     result = compute_overlap_time(first, second)
#     expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00')]
#     assert result == expected

def test_backwardsrange():
    with raises(ValueError):
        range = time_range("2010-01-12 14:00:00", "2010-01-12 12:00:00")

test_cases = [
    #given input
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
     time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
     [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),

    #no overlap
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
     time_range("2010-01-12 09:30:00", "2010-01-12 09:45:00"),
     []),

    #multiple intervals each
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3, 10),
     time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
     [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:39:53'), ('2010-01-12 10:40:03', '2010-01-12 10:45:00')]),

    #border case
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
     time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00"),
     [('2010-01-12 12:00:00', '2010-01-12 12:00:00')])
]

@pytest.mark.parametrize("time_range1, time_range2, expected", test_cases)
def test_timeranges(time_range1, time_range2, expected):
    result = compute_overlap_time(time_range1, time_range2)
    assert result == expected