# You are given a 0-indexed integer array buses of length n, where buses[i] represents the departure time of the ith bus. You are also given a 0-indexed integer array passengers of length m, where passengers[j] represents the arrival time of the jth passenger. All bus departure times are unique. All passenger arrival times are unique.
#
# You are given an integer capacity, which represents the maximum number of passengers that can get on each bus.
#
# When a passenger arrives, they will wait in line for the next available bus. You can get on a bus that departs at x minutes if you arrive at y minutes where y <= x, and the bus is not full. Passengers with the earliest arrival times get on the bus first.
#
# More formally when a bus arrives, either:
#
#     If capacity or fewer passengers are waiting for a bus, they will all get on the bus, or
#     The capacity passengers with the earliest arrival times will get on the bus.
#
# Return the latest time you may arrive at the bus station to catch a bus. You cannot arrive at the same time as another passenger.
#
# Note: The arrays buses and passengers are not necessarily sorted.

# Solution
# The idea in a greedy way we want to board the last bus, well there two cases, one is there is space to take the last bus, and other case is last bus is filled, 
# then we need to find the largest time to board the last bus that is not taken but also has to be before the previous passengers

# TC: O(N log N)
# SC: O(N)

from typing import List
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        M = len(passengers)
        t = capacity
        i = 0
        for time in buses:
            cap = capacity
            while i < M and passengers[i] <= time and cap > 0:
                i += 1
                cap -= 1
            t = cap
        res = buses[-1] if t > 0 else passengers[i - 1]
        p = set(passengers)
        while res in p:
            res -=1
        return res
