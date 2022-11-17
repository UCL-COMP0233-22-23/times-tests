import datetime

#时间格式，例如2000-01-06 12:34:56
def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):#开始和结束的这个时间区间里有多少段间隔，每个间隔多少秒，每段时间应该相等
    #strptime把一个时间字符串解析为时间元组
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")#年月日时分秒
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]
#strftime返回可读字符串表示当地的时间

#计算重叠时间
def compute_overlap_time(range1, range2):#range1/2都是一段时间
    overlap_time = []
    for start1, end1 in range1:#start1 和end1为每段时间的开始时间和结束时间
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((low, high))
    return overlap_time

if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00") 
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00",2, 60)
    print(compute_overlap_time(large, short))
    
    