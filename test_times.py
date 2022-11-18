from times import compute_overlap_time,time_range


def test_given_input():

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00",2, 60) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert compute_overlap_time(large, short) == expected
    
#两个时间没有重合
def test_given_input_do_not_overlap():
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 9:30:00", "2010-01-12 9:45:00",2, 60) 
    expected=[]    
    assert compute_overlap_time(large, short) == expected  
    
#两个时间都有多段   
def test_given_input_both_contain_several_interval():
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",2,2400)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00",2, 60) 
    expected=[('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:40:00')]   
    assert compute_overlap_time(large, short) == expected  
    
#只有一秒重合
def test_given_input_end_when_the_other_starts():
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00",2, 60) 
    expected=[('2010-01-12 10:30:00', '2010-01-12 10:30:00')]
    assert compute_overlap_time(large, short) == expected 