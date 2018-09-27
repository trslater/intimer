import time

while True:
    start = time.time()
    print('.')
    time.sleep(1 - (time.time() - start))