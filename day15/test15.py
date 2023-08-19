import threading
import time
import queue

#创建队列队象
q=queue.Queue(maxsize=500)

def mytest():
    for i in range(500):
        q.put("书本-"+str(i))
        print("put书本-"+str(i))
        time.sleep(5)


def mytest02():
    while True:
        msg=q.get(block=True, timeout=3)
        print('get' + msg)
        time.sleep(1)


t1=threading.Thread(target=mytest)
t2=threading.Thread(target=mytest02)

t1.start()
t2.start()
t1.join()
t2.join()