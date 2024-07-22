import time


class Time:
    myTime = time.time()

    def getPassedTimeFromStart(self):
        return time.time() - self.myTime

    def resetTime(self):
        self.myTime = time.time()

