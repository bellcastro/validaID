import unittest

from validaID import validaID

class TestMethod(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(validaID("abc12"), True, "Precisa ser True")

    def test_case2(self):
        self.assertEqual(validaID("cont*1"), False, "Precisa ser False")

    def test_case3(self):
        self.assertEqual(validaID("1soma"), False, "Precisa ser False")
    
    def test_case4(self):
        self.assertEqual(validaID("a123456"), False, "Precisa ser False")

if __name__ == '__main__':
    unittest.main()