import threading
import time


def loop1_10():
    for i in range(1, 11):
        time.sleep(5)
        print(i)


def loop1_11():
    for i in range(1, 11):
        print('This is in wait' + str(i))


for i in range(1, 100):
    threading.Thread(target=loop1_10).start()
    threading.Thread(target=loop1_11).start()
    print(threading.active_count())
