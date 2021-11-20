#!/usr/bin/python3
# Test cases for adding two numbers

import unittest

from Program import fibonacci

"""
	Test case for testing if the 
	Fibonacci sequence is correctly
	calculated or not
"""
class TestFibo(unittest.TestCase):
	def test_case_3(self):
		test_3 = 5
		result = fibonacci(test_3)
		self.assertEqual(result, 5)
	def test_case_4(self):
		test_4 = 9
		result = fibonacci(test_4)
		self.assertEqual(result, 34)
		
if __name__ == '__main__':
	unittest.main()
