# Provide a countdown for X seconds, then print "Happy New Year!"
import time
def countdown(seconds):
    while (seconds > 0):
        print(f"Countdown: {seconds}")
        time.sleep(1)
        seconds -= 1
    print("Happy New Year!")
    return

countdown(5)