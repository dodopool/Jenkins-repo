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
	def test_case_1(self):
		test_1 = 0
		result = fibonacci(test_1)
		self.assertEqual(result, 0)
	def test_case_2(self):
		test_2 = 1
		result = fibonacci(test_2)
		self.assertEqual(result, 1)
		
if __name__ == '__main__':
	unittest.main()
