# A ride sharing system manages ride requests from riders and availability from drivers. Riders request rides, and drivers become available over time. The system should match riders and drivers in the order they arrive.
#
# Implement the RideSharingSystem class:
#
#     RideSharingSystem() Initializes the system.
#     void addRider(int riderId) Adds a new rider with the given riderId.
#     void addDriver(int driverId) Adds a new driver with the given driverId.
#     int[] matchDriverWithRider() Matches the earliest available driver with the earliest waiting rider and removes both of them from the system. Returns an integer array of size 2 where result = [driverId, riderId] if a match is made. If no match is available, returns [-1, -1].
#     void cancelRider(int riderId) Cancels the ride request of the rider with the given riderId if the rider exists and has not yet been matched.

# Solution 
# Two ways - lazy queue or Linked HashMap, basically the idea is use a queue for driver, for riders use queue/linkedhashmap
# Linkedhashmap is better because you can always guarantee O(1) for all operations where as lazy queue is Amortized O(1)
# TC: O(1)
# SC: O(N) where N is the number of nodes

from typing import List
from collections import deque
class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
class LinkedHashMap:
    def __init__(self):
        self.head,self.tail = ListNode(-1),ListNode(-1) 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
    def insert(self,val):
        node = ListNode(val)
        self.cache[val] = node
        prev,nxt = self.tail.prev,self.tail
        prev.next = node
        nxt.prev = node
        node.next,node.prev = nxt,prev
    def delete(self,node):
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev
    def remove(self,val):
        # print(self.cache)
        node = self.cache[val]
        self.delete(node)
        del self.cache[val]
        # print(self.cache)
    def pop(self):
        if self.head.next == self.tail:
            return None
        val = self.head.next.val
        self.remove(val)
        return val

         
class RideSharingSystem:

    def __init__(self):
        self.riders = LinkedHashMap()
        self.drivers = deque()

    def addRider(self, riderId: int) -> None:
        self.riders.insert(riderId)


    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if not self.drivers:
            return [-1,-1]
        riderId = self.riders.pop()
        if riderId == None:
            return [-1,-1]
        driverId = self.drivers.popleft()
        return [driverId,riderId]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riders.cache:
            self.riders.remove(riderId)

class LazyQueue:

    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.cancel = set()
    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        if riderId in self.cancel:
            self.cancel.remove(riderId)
    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if not self.drivers:
            return [-1,-1]
        # print(self.riders)
        # print(self.cancel)
        while self.riders and self.riders[0] in self.cancel:
            r = self.riders.popleft()
            self.cancel.remove(r)
        if not self.riders:
            return [-1,-1]
        riderId = self.riders.popleft()
        driverId = self.drivers.popleft()
        return [driverId,riderId]

    def cancelRider(self, riderId: int) -> None:
        self.cancel.add(riderId)

