import time

############################################################################


'''Logic for the Stop-Watch'''


def stop_watch():
    int(input("Enter 1 to Start:"))
    startTime = time.time()
    int(input("Enter 0 to Stop Time:"))
    endTime = time.time()
    timeElapsed = endTime - startTime
    print("Time elapsed from Start to Stop is: ", timeElapsed, " Sec")

#############################################################################