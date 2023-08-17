# import pymysql
#
# db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='admin123', db='test', charset='utf8')
# cur = db.cursor()
# cur.execute('select database()')
# data = cur.fetchall()
# print(data)
#
# cur.execute('drop database if exists mytest')
#
# cur.execute('use test')
# cur.execute('select database()')
# data = cur.fetchall()
# print(data)

class MyIterObj:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __next__(self):
        if self.start <= self.end:
            temp = self.start
            self.start += 1
            return temp
        else:
            raise StopIteration

    def __iter__(self):
        return self


myiter = MyIterObj(12, 20)
try:
    while True:
        print(next(myiter), end=' ')
except StopIteration as e:
    print(e.value)

l = iter([1, 2, 3])
print(next(l), end= ' ')
print()
res=(i for i in [1,2,3,4])

print(next(res))
print(next(res))
for i in res:
    print(i)
print('==================')
import sys


def fibonacci(n):  # 生成器函数 - 斐波那契，返回n个斐波那契数
    a, b, counter = 0, 1, 1
    while counter <= n:  # 生成n个
        yield a
        a, b = b, a + b  # 返回一个斐波那契数，更新a,b，然后循环计算后面一个
        counter += 1


f = fibonacci(10)  # f 是一个生成器对象，但它同时具有迭代器的所有功能，因为其自动实现了迭代器协议
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()