import unittest

from main import conocerPalindromo

class Test(unittest.TestCase):
    def test_conocer_edad(self):
        self.assertEqual(True,conocerPalindromo("amor a roma"))

if __name__== '__main__':
    unittest.main()