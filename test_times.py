from times import compute_overlap_time, time_range
import pytest


@pytest.mark.parametrize(

    "time_range_1,time_range_2, expected",
    [
        # normal
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range(
                "2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
            [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
             ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
        ),
        # no overlaps
        (
            time_range("2010-01-12 11:50:00", "2010-01-12 12:00:00"), time_range(
                "2010-01-12 10:30:00", "2010-01-12 10:45:00"),
            []
        ),
        # several intervals each
        (
            time_range("2010-01-12 10:40:00", "2010-01-12 12:00:00", 2,
                       60), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
            [("2010-01-12 10:40:00", "2010-01-12 10:45:00")]
        ),
        # same ending time
        (
            time_range("2010-01-12 10:40:00", "2010-01-12 10:45:00"), time_range(
                "2010-01-12 10:30:00", "2010-01-12 10:45:00"),
            [("2010-01-12 10:40:00", "2010-01-12 10:45:00")]
        )
    ]
)
def test_given_input(time_range_1, time_range_2, expected):
    assert compute_overlap_time(time_range_1, time_range_2) == expected


def test_start_time_bigger_than_end_time():
    with pytest.raises(ValueError):
        wrong = time_range("2010-01-12 10:45:00", "2010-01-12 10:40:00")
