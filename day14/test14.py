import time
import multiprocessing


def light(event):
    print('此时是红灯')
    time.sleep(3)
    print('绿灯了')
    event.set()
    print(event.is_set())


def car(event, name):
    print(f'car{name}在等红灯')
    event.clear()
    event.wait()
    print(f'car{name}可以走了')


if __name__ == '__main__':
    event = multiprocessing.Event()
    l = multiprocessing.Process(target=light,args=(event,))
    l.start()
    car1 = multiprocessing.Process(target=car, args=(event,1,))
    car2 = multiprocessing.Process(target=car, args=(event,2,))
    car1.start()
    car2.start()
