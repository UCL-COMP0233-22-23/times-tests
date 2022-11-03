import datetime
import time
from pytest import raises


def correctly_ordered_inputs(range0):
    if range0[0][0] > range0[-1][1]:
        raise ValueError("\n The input contains a time range which goes backwards in time as index is increased. \n Please ensure inputs are time-ordered.")

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):  
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]



def compute_overlap_time(range1, range2):
    
    # Checking inputs
    correctly_ordered_inputs(range1)
    correctly_ordered_inputs(range2)
    
    latest_start = max(min([start for start, end in range1]), 
                       min([start for start, end in range2]))
    earliest_end = min(max([end for start, end in range1]), 
                       max([end for start, end in range2]))
    ls_sec = time.mktime(time.strptime(latest_start, "%Y-%m-%d %H:%M:%S"))
    ee_sec = time.mktime(time.strptime(earliest_end, "%Y-%m-%d %H:%M:%S"))
    if ls_sec < ee_sec:
        return ee_sec - ls_sec
    else:
        return 0
    

if __name__ == "__main__":
    large = time_range("2010-01-12 10:35:00", "2010-01-12 10:31:00", 2)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:50:00", 2)
    print()
    print(compute_overlap_time(large, short), 'seconds of overlap')