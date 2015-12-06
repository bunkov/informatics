import unittest
import lib
import math

class LibTest(unittest.TestCase):

	def test_even_EvenPositive(self):
		self.assertEqual(lib.even(2), True)
		self.assertEqual(lib.even(1982302), True)
	def test_even_NotEvenPositive(self):
		self.assertEqual(lib.even(1), False)
		self.assertEqual(lib.even(3), False)
		self.assertEqual(lib.even(323812101), False)
	def test_even_Zero(self):
		self.assertEqual(lib.even(0), True)
	def test_even_EvenNegative(self):
		self.assertEqual(lib.even(-2), True)
		self.assertEqual(lib.even(-1982302), True)
	def test_even_NotEvenNegative(self):
		self.assertEqual(lib.even(-1), False)
		self.assertEqual(lib.even(-323812101), False)
	
	def test_factorial_Positive(self):
		self.assertEqual(lib.factorial(4), 24)
		self.assertEqual(lib.factorial(1), 1)
		self.assertEqual(lib.factorial(10), 3628800)
	def test_factorial_Negative(self):
		self.assertEqual(lib.factorial(-10), 1)
	def test_factorial_Zero(self):
		self.assertEqual(lib.factorial(0), 1)
	
	def test_palindrome_True(self):
		self.assertEqual(lib.palindrome('ss'), True)
		self.assertEqual(lib.palindrome('qsq'), True)
	def test_palindrome_False(self):
		self.assertEqual(lib.palindrome('sq'), False)
		self.assertEqual(lib.palindrome('qss'), False)
	def test_palindrome_Register(self):
		self.assertEqual(lib.palindrome('sS'), False)
		self.assertEqual(lib.palindrome('sQqQS'), False)
	
	def test_prime_PrimePositive(self):
		self.assertEqual(lib.prime(2), True)
		self.assertEqual(lib.prime(3), True)
		self.assertEqual(lib.prime(3571), True)
	def test_prime_NotPrimePositive(self):
		self.assertEqual(lib.prime(4), False)
		self.assertEqual(lib.prime(6), False)
		self.assertEqual(lib.prime(1982302), False)
	def test_prime_Zero(self):
		self.assertEqual(lib.prime(0), False)
	def test_prime_One(self):
		self.assertEqual(lib.prime(1), False)
	def test_prime_Negative(self):
		self.assertEqual(lib.prime(-3), False)
	
	def test_sin(self):
		self.assertEqual(lib.sin(0), 0)
		self.assertEqual(lib.sin(math.pi/2), 1)
		self.assertEqual(lib.sin(math.pi), 0)
		self.assertEqual(lib.sin(3*math.pi/2), -1)
		self.assertEqual(lib.sin(2*math.pi), 1)
		self.assertEqual(lib.sin(-math.pi/2), -1)
		self.assertEqual(lib.sin(-math.pi), 0)
		self.assertEqual(lib.sin(-3*math.pi/2), 1)
		self.assertEqual(lib.sin(-2*math.pi), 0)

	def test_sqrt_Positive(self):
		self.assertEqual(lib.sqrt(9), 3)
		self.assertEqual(lib.sqrt(1), 1)
		self.assertEqual(lib.sqrt(0), 0)
	def test_sqrt_Negative(self):
		self.assertEqual(lib.sqrt(-1), 0)

unittest.main(verbosity=2)