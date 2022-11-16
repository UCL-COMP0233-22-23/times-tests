from times import time_range
from times import compute_overlap_time
from pytest import raises
def test_time_given_input():

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

    #two time ranges do not overlap
    large2 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short2 = time_range("2010-01-12 13:30:00", "2010-01-12 13:45:00", 2, 60)
    with raises(ValueError) as e_info2:
        compute_overlap_time(large2, short2)
    expected2 = "no overlap between two time range"
    assert e_info2.value.args[0] == expected2

    #two time ranges that both contain several intervals each
    large3 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short3 = time_range("2010-01-12 11:30:00", "2010-01-12 12:45:00", 2, 60)
    result3 = compute_overlap_time(large3, short3)
    expected3 = [("2010-01-12 11:30:00", "2010-01-12 12:00:00")]
    assert result3 == expected3

    #two time ranges that end exactly at the same time when the other starts
    large4 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short4 = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00", 2, 60)
    with raises(ValueError) as e_info4:
        compute_overlap_time(large4, short4)
    expected4 = "no overlap between two time range"
    assert e_info4.value.args[0] == expected4

    large5 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short5 = time_range("2010-01-12 09:00:00", "2010-01-12 09:45:00", 2, 60)
    with raises(ValueError) as e_info5:
        compute_overlap_time(large5, short5)
    expected5 = "no overlap between two time range"
    assert e_info5.value.args[0] == expected5
