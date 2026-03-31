"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n= len(intervals)
        for i in range(n):
            int1= intervals[i]
            for j in range(i+1,n):
                int2= intervals[j]
                if min(int1.end,int2.end) > max(int1.start,int2.start):
                    return False
        return True

