import unittest


class Maker(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.name = '\nnameeeeeeeeee'

    def testname(self):
        print(self.name)


if __name__ == '__main__':
    unittest.main()