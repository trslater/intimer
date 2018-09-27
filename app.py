import sys
import subprocess

from time import time, sleep
from datetime import datetime, timedelta
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
        for elapsed in range(timer["duration"]):
            start = time()

            remaining = timer["duration"] - elapsed

            sys.stdout.write(str(timedelta(seconds=remaining)) + "\r")
            sys.stdout.flush()

            sleep(1 - (time() - start))

        macos_notify(timer["done message"])

def macos_notify(message):
    # osascript -e 'display notification "Lorem ipsum dolor sit amet" with title "Title"'
    subprocess.run([
        "osascript",
        "-e",
        f"display notification \"{message}\" with title \"Eye Rest Timer\""
    ])

if __name__ == "__main__":
    main()