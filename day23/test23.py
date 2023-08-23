import random
import unittest
from HTMLTestRunner import HTMLTestRunner


class Calculator(unittest.TestCase):
    @classmethod
    def add(cls, a, b):
        return a+b

    @classmethod
    def subtract(cls, a, b):
        return a - b

    def test01(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        a+b == Calculator.add(a,b)
        print('\n1')

    def test02(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        a-b == Calculator.subtract(a,b)
        print('\n2')


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./unittest/', 'unit*.py')
    print(suite)
    with open('1.html', 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title="单元测试报告", description="第一次运行结果")
        runner.run(suite)
