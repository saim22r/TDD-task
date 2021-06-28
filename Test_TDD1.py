# TDD Task

import unittest
import pytest

from Test_TDD2 import TestCalcs

class TestDivisible(unittest.TestCase):

    nums = TestCalcs()

    def test_divisible(self):
        self.assertEqual(self.nums.divisible(5, 5), 0)

    def test_positive(self):
        self.assertEqual(self.nums.positive(5), True)

