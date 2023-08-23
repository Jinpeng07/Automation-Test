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
        print('\n22-11')

    def test02(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        a-b == Calculator.subtract(a,b)
        print('\n22-22')
