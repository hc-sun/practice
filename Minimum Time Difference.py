class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        times = sorted([int(time[:2])*60 + int(time[-2:]) for time in timePoints]) #change time format to minutes
        low = sys.maxsize
        for i in range(len(times)-1): #compare adjacent times
            low = min(low, times[i+1]-times[i])
            if low == 0:
                return 0
        low = min(low, times[0] - times[-1] + 1440) #consider circle 60*24=1440
        return low
        
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.