import time
import unittest


class TestClass1(unittest.TestCase):
    def test01(self):
        time.sleep(1)
        print('test01...')

    def test02(self):
        print('test02...')

    def test03(self):
        print('test03...')

    def test04(self):
        print('test04...')

    def test05(self):
        print('test05...')


class TestClass2(unittest.TestCase):
    def test01(self):
        time.sleep(1)
        print('test01...222')

    def test02(self):
        print('test02...222')

    def test03(self):
        print('test03...222')

    def test04(self):
        print('test04...222')

    def test05(self):
        print('test05...222')
