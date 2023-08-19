# s = 'abc'
# for i in s:
#     print(i, end=' ')
# print()
# iter_s = iter(s)
# try:
#     while True:
#         print(next(iter_s), end=' ')
# except StopIteration as e:
#     print()
#
#
# def gen(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1
#
#
# g = gen(10)
# for i in g:
#     print(i, end= ' ')
# def dec_mytest(func):
#     def ret(s):
#         itera = func(s)
#         for i in itera:
#             print(i, end=' ')
#     return ret
#
# @dec_mytest
# def mytest(n):
#     return iter(n)
# #
# #
# # mytest('aaa')
# import time
#
#
# def collect_time(func):
#     def total_time():
#         begin = time.time()
#         func()
#         end = time.time()
#         return end - begin
#     return total_time
#
#
# @collect_time
# def itertest():
#     time.sleep(2)
#
#
# print(itertest())

def f1():
    n = 999

    def f2():
        print(n)

    return f2


if __name__ == '__main__':
    #result = f1()
    f1()()




