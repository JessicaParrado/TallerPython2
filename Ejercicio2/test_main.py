import unittest

from main import conocerMultiplos

class Test(unittest.TestCase):
    def test_conocer_multiplos(self):
        list =[]
        list.append(3)
        list.append(6)
        list.append(9)
        list.append(12)
        list.append(15)
        list.append(18)
        list.append(21)
        self.assertEqual(list,conocerMultiplos(2,21,3))

if __name__== '__main__':
    unittest.main()