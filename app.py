from time import time, sleep
from itertools import cycle

timers = cycle([
    {
        "duration":     1200,
        "done message": "Time to rest your eyes!"
    },
    {
        "duration":     20,
        "done message": "Back to work..."
    },
])

def main():
    for timer in timers:
        for remaining in range(timer["duration"]):
            start = time()

            print(remaining)

            sleep(1 - (time() - start))

def get_next_timer():
    for timer in timers:
        yield timer

if __name__ == "__main__":
    main()