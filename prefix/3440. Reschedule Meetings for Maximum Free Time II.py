# You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.
#
# These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].
#
# You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.
#
# Return the maximum amount of free time possible after rearranging the meetings.
#
# Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.
#
# Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.


# Solution
# I knew the idea was to try and find if a certain segment can fit in any gaps, but I did not know how to write the gaps part, but now i know it is basiaclly using a (N + 1) 1D array
# to store the left and right of every index, then it is just a suffix and prefix type of question

# TC: O(N)
# SC: O(N)

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        N = len(startTime)
        events = list(zip(startTime,endTime))
        gaps = [0] * (N + 1)
        gaps[0] = startTime[0]
        for i in range(N - 1):
            end = events[i][1]
            n_start = events[i + 1][0]
            gaps[i + 1] = n_start - end
        gaps[N] = eventTime - endTime[-1] 
        # print(gaps)
        prefix = [gaps[0]]
        suffix = [gaps[-1]]
        for i in range(1,N + 1):
            prefix.append(max(prefix[-1],gaps[i]))
        for i in range(N - 1,-1,-1):
            suffix.append(max(suffix[-1],gaps[i]))
        # print(prefix)
        suffix = suffix[::-1]
        res = 0
        for i in range(N):
            start,end = events[i][0],events[i][1]
            left = gaps[i]
            right = gaps[i + 1]
            duration = end - start
            res = max(res,left + right)
            if i - 1 >= 0:
                if prefix[i - 1] >= duration:
                    res = max(res,left + right + duration)
            if i + 2 <= N:
                if suffix[i + 2] >= duration:
                    res = max(res,left + right + duration)
        return res
