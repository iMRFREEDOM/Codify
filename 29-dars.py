import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

COUNT = 200_000_000
SLEEP = 10

def io_bound(sec):
    pid = os.getpid()
    print(f"{pid} * {current_process().name} * {current_thread().name} --> Kutish boshlandi...")
    time.sleep(sec)
    print(f"{pid} * {current_process().name} * {current_thread().name} --> Kutish yakunlandi...")


def cpu_bound(n):
    pid = os.getpid()
    print(f"{pid} * {current_process().name} * {current_thread().name} --> Hisoblash boshlandi...")
    while n > 0:
        n -= 1
    print(f"{pid} * {current_process().name} * {current_thread().name} --> Hisoblash yakunlandi...")


if __name__ == "__main__":
    start = time.time()
    #1-holat: Single threed - io_bound             20.001880645751953
    io_bound(SLEEP)
    io_bound(SLEEP)
    
    # 2-holat: multithreeding io_bound              10.002065420150757
    t1 = Thread(target=io_bound, args=(SLEEP,))
    t2 = Thread(target=io_bound, args=(SLEEP,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 3-holat singlethreed cpu_bound                 18.030054807662964
    cpu_bound(COUNT)
    cpu_bound(COUNT)
    

    #4-holat: multithreed cpu_bound                  18.006675481796265
    t1 = Thread(target=cpu_bound, args=(COUNT,))
    t2 = Thread(target=cpu_bound, args=(COUNT,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    #5-holat: multiprocessing cpu_bound
    p1 = Process(target=cpu_bound, args=(COUNT,))     # 9.081756114959717
    p2 = Process(target=cpu_bound, args=(COUNT,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    #6-holat: multiprocessing io_bound
    p1 = Process(target=io_bound, args=(SLEEP,))       # 10.161593914031982
    p2 = Process(target=io_bound, args=(SLEEP,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()
    print("Ketgan vaqt(s)", end - start)


# Xulosa:
# 1. io_bound - multithreeeding
# 2. cpu_bound - multiprocessing
# 3.multithreeding - eoiiooriri