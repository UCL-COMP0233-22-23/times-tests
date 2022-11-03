from times import time_range,compute_overlap_time

def test_given_input(): 
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
    
    result = []
    result = compute_overlap_time(large, short)
    expected  = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected
    

    
    #two time ranges that do not overlap
    large = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    print(compute_overlap_time(large, short))
    
    result1 = []
    result1 = compute_overlap_time(large, short)
    expected1  = []
    assert result1 == expected1
    

    
    #two time ranges that both contain several intervals each
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
    
    result2 = []
    result2 = compute_overlap_time(large, short)
    expected2  = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:40:00')]
    assert result2 == expected2
    

    
    #two time ranges that end exactly at the same time when the other starts
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
    
    result3 = []
    result3 = compute_overlap_time(large, short)
    expected3  = []
    assert result3 == expected3
    