import unittest
import lib

class LibTest(unittest.TestCase):

	def test_even(self):
		self.assertEqual(lib.even(2), True)
		self.assertEqual(lib.even(1), False)
		self.assertEqual(lib.even(-1), False)
		self.assertEqual(lib.even(-2), True)
		self.assertEqual(lib.even(0), True)
		
	
	def test_factorial(self):
		self.assertEqual(lib.factorial(0), 1)
		self.assertEqual(lib.factorial(4), 24)
		self.assertEqual(lib.factorial(-10), 1)
	
	def test_palindrome(self):
		self.assertEqual(lib.palindrome('ss'), True)
		self.assertEqual(lib.palindrome('sq'), False)
		self.assertEqual(lib.palindrome('sS'), False)
		self.assertEqual(lib.palindrome('qss'), False)
		self.assertEqual(lib.palindrome('qsq'), True)
		
	#def test_prime(self):
	
	#def test_sin(self):
	
	#def test_sqrt(self):

unittest.main(verbosity=2)
