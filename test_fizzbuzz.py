import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_FizBuzz(self):
        #Not a multiple of 3 or 5
        self.assertEqual(fizzbuzz.fizzbuzzNum(2), "2")
        self.assertEqual(fizzbuzz.fizzbuzzNum(11), "11")
        self.assertEqual(fizzbuzz.fizzbuzzNum(98), "98")

        #Multiples of 3 but not 5
        self.assertEqual(fizzbuzz.fizzbuzzNum(3), "Fizz")
        self.assertEqual(fizzbuzz.fizzbuzzNum(12), "Fizz")
        self.assertEqual(fizzbuzz.fizzbuzzNum(99), "Fizz")

        #Multiples of 5 but not 3
        self.assertEqual(fizzbuzz.fizzbuzzNum(5), "Buzz")
        self.assertEqual(fizzbuzz.fizzbuzzNum(15), "Buzz")
        self.assertEqual(fizzbuzz.fizzbuzzNum(100), "Buzz")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)