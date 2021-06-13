from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        Solution.tar = target
        Solution.mini = -1
        stations.sort()
        return Solution.recurse(0, startFuel, 0, stations)

    def recurse(dist: int, fuel: int, stops: int, stations: List[List[int]]) -> int:
        # print()
        # print(dist)
        # print(fuel)
        # print(stops)
        # print(stations)
        # print()
        if fuel + dist >= Solution.tar:
            Solution.mini = stops
            return stops

        if len(stations) == 0 or (stops == Solution.mini):
            return -1

        i = 0
        while i < len(stations) and stations[i][0] >= dist and stations[i][0] <= fuel + dist:
            Solution.recurse(stations[i][0], fuel + stations[i][1] - (stations[i][0] - dist), stops + 1, stations[i + 1:])
            # print('yo')
            # print(stations[i + 1:])
            # print(stations[i][0])
            # print(fuel + stations[i][1] - (stations[i][0] - dist))
            # print(stops + 1)
            # print(stations[i][0])
            # recurse()
            # print()
            i += 1

        return Solution.mini

s = Solution()
print(s.minRefuelStops(1, 1, [])) #0
print(s.minRefuelStops(10, 1, [])) #-1
print(s.minRefuelStops(100, 1, [[10,100]])) #-1
print(s.minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]])) #2
print(s.minRefuelStops(100, 10, [[1,60],[2,30],[3,30],[6,40]])) #2

