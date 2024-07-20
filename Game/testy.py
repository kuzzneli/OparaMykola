from TimeModule import Time
import time

count = 30
t = Time(count)
timePassed = []
while count > 0:
    passed = int(t.getPassedTime())
    if not passed in timePassed:
        print(count - passed)
        timePassed.append(passed)
