#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrage(unittest.TestCase):
	def test_basic(self):
		testcase = "Musk, Elon"
		expected = "Elon Musk"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_empty (self):
		testcase = ""
		expected = ""
		self.assertEqual(rearrange_name(testcase), expected)

	def test_double_name(self):
		testcase = "Musk, Elon R."
		expected = "Elon R. Musk"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_one_name(self):
		testcase = "Tesla"
		expected = "Tesla"
		self.assertEqual(rearrange_name(testcase), expected)

unittest.main() 


