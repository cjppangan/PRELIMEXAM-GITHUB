#PANGAN, CHRISTIAN JOSEPH P.
#PRELIM EXAM
import unittest

def temp(Fahrenheit):
    Fahrenheit = 32
    Celsius = ((Fahrenheit-32)*(5/9))   
    return Celsius

class MyTest(unittest.TestCase):

    def test(self):

        self.assertEqual(temp(32),0)
    def test2(self):

        self.assertEqual(temp(32),1)    

if __name__ == '__main__':

    unittest.main()
