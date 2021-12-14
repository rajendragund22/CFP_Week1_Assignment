import time


class StopWatch:

    def stop_watch(self):
        int(input("Enter 1 to Start:"))
        startTime = time.time()
        int(input("Enter 0 to Stop Time:"))
        endTime = time.time()
        timeElapsed = endTime - startTime
        print("Time elapsed from Start to Stop is: ", timeElapsed, " Sec")

obj=StopWatch()
obj.stop_watch()