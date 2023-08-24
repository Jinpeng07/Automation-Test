import unittest
import ddt


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(1, 2, 3)
    def test01(self, v):
        print('test01')
        print(v)
        self.assertEqual(v,v)

    @ddt.data((1,1,3), [1,2,4])
    @ddt.unpack
    def test02(self, v1, v2, v3):
        print('test02')
        print(v1,v2,v3)
        self.assertEqual(v1,v2)


if __name__ == '__main__':
    unittest.main()
