import time


class Time:
    def __init__(self, countdown):
        self.time = time.time()
        self.countdown = countdown

    def getPassedTime(self):
        return time.time() - self.time
