# # class Maker:
# #     ins = None
# #     pass
# #
# #
# # maker = object.__new__(Maker)
# # Maker.ins
#
# class Maker:
#     @classmethod
#     def test(cls):
#         print('I am class method')
#
#
# m = Maker()
# m.test()
# Maker.test()
import os
from multiprocessing import Process


def mytask(n, m):
    num = 1
    for i in range(1000000):
        num = i
    print(f'child process is {os.getpid()}')

class Maker(Process):
    def __init__(self, d):
        super().__init__()
        self.d = d

    def run(self):
        num = 1
        for i in range(100000000):
            num = i
        print(f'child process is {os.getpid()}')

if __name__ == '__main__':
    print("父进程PID为%s " % os.getpid())
    # 创建子进程,使用类
    p1 = Maker(3)
    p1.start()
    p1.join()  # 阻塞主进程,让子进程完成任务或子进程被终止
