#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrage(unittest.TestCase):
	def test_basic(self):
		testcase = "Musk, Elon"
		expected = "Elon Musk"
		self.assertEqual(rearrange_name(testcase), expected)

unittest.main() 


