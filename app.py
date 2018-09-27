from time import time, sleep
from itertools import cycle
import subprocess

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

        macos_notify(timer["done message"])

def go(timer, remaining):
    print(timer["duration"] - remaining)

def macos_notify(message):
    # osascript -e 'display notification "Lorem ipsum dolor sit amet" with title "Title"'
    subprocess.run([
        "osascript",
        "-e",
        f"display notification \"{message}\" with title \"Eye Rest Timer\""
    ])

if __name__ == "__main__":
    main()