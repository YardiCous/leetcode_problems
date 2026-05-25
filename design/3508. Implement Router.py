# Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:
#
#     source: A unique identifier for the machine that generated the packet.
#     destination: A unique identifier for the target machine.
#     timestamp: The time at which the packet arrived at the router.
#
# Implement the Router class:
#
# Router(int memoryLimit): Initializes the Router object with a fixed memory limit.
#
#     memoryLimit is the maximum number of packets the router can store at any given time.
#     If adding a new packet would exceed this limit, the oldest packet must be removed to free up space.
#
# bool addPacket(int source, int destination, int timestamp): Adds a packet with the given attributes to the router.
#
#     A packet is considered a duplicate if another packet with the same source, destination, and timestamp already exists in the router.
#     Return true if the packet is successfully added (i.e., it is not a duplicate); otherwise return false.
#
# int[] forwardPacket(): Forwards the next packet in FIFO (First In First Out) order.
#
#     Remove the packet from storage.
#     Return the packet as an array [source, destination, timestamp].
#     If there are no packets to forward, return an empty array.
#
# int getCount(int destination, int startTime, int endTime):
#
#     Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range [startTime, endTime].
#
# Note that queries for addPacket will be made in non-decreasing order of timestamp.

# Solution
# Poor description make me WA but overall normal design question
# addPacket O(1)
# forwardPacket O(1)
# getCount (log N)

from collections import deque,defaultdict
from typing import List
import bisect
class Router:

    def __init__(self, memoryLimit: int):
        self.memory = memoryLimit
        self.destination = defaultdict(deque)
        self.all_packets = deque()
        self.packets = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) in self.packets:
            return False
        self.packets.add((source,destination,timestamp))
        self.all_packets.append((source,destination,timestamp))
        self.destination[destination].append(timestamp)
        if len(self.all_packets) > self.memory:
            src,dest,time = self.all_packets.popleft()
            self.packets.remove((src,dest,time))
            self.destination[dest].popleft()
        return True

    def forwardPacket(self) -> List[int]:
        if self.all_packets:
            source,dest,time = self.all_packets.popleft()
            self.packets.remove((source,dest,time))
            self.destination[dest].popleft()
            return [source,dest,time]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        current_destination = self.destination[destination]
        left_index = bisect.bisect_left(current_destination,startTime)
        right_index = bisect.bisect_right(current_destination,endTime)
        return right_index - left_index


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
