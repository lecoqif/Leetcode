from collections import defaultdict
from typing import Tuple

class UndergroundSystem:

    def __init__(self):
        # Tuple --> Checkin station, check in time
        self.travels = defaultdict(lambda:("", 0))
        
        # Tuple --> total time, number of journeys
        self.travelTimes = defaultdict(lambda:(0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travels[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.travels[id]
        self.travels.pop(id)
        totalTime, journeyCount = self.travelTimes[startStation + '-' + stationName]
        totalTime += t - startTime
        journeyCount += 1
        self.travelTimes[startStation + '-' + stationName] = (totalTime, journeyCount)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, journeyCount = self.travelTimes[startStation + '-' + endStation]
        return totalTime / journeyCount


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)