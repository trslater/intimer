from time import time, sleep
from itertools import cycle

timers = cycle([
    {
        "duration":     5,
        "done message": "Time to rest your eyes!"
    },
    {
        "duration":     10,
        "done message": "Back to work..."
    },
])

def main():
    for timer in timers:
        for remaining in range(timer["duration"]):
            start = time()

            go(timer, remaining)

            sleep(1 - (time() - start))

        print(timer["done message"])

def go(timer, remaining):
    print(timer["duration"] - remaining)

if __name__ == "__main__":
    main()