"""
RateLimiter asked at Fast
"""
from collections import defaultdict
import time


class RateLimiter(object):
    def __init__(self, maxAllowed):
        self.maxAllowed = maxAllowed
        self.rateMap = defaultdict(list)

    def _isThrottled(self, key, count):
        timeElapasedSinceLastSecond = self.currentMillitime()
        secondInterval = self.currentSecond() % 2
        
        reqInPrevInterval = self.rateMap[key][(secondInterval + 1) % 2]
        requestsInSlidingInterval = ((1000 - timeElapasedSinceLastSecond) / 1000) * reqInPrevInterval
        
        reqInCurInterval = self.rateMap[key][secondInterval]

        throttled = requestsInSlidingInterval + reqInCurInterval >= self.maxAllowed

        if not throttled:
            self.rateMap[key][secondInterval] += count

        return throttled
    
    def limit(self, key, count=1):
        if key not in self.rateMap:
            self.rateMap[key] = [0, 0]
        
        return self._isThrottled(key, count)

    def currentMillitime(self):
        return round(time.time() * 1000) % 1000
    
    def currentSecond(self):
        t = time.ctime().split(' ')
        clock = t[3]
        second = clock.split(':')[2]
        return int(second)
    
    def cleanup(self):
        pass
