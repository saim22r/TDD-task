# TDD Task
- Create a test to check is the number divisible/remainder 0 if True pass the test if False fail
- Create a class and method to write code to pass the test
- Create a test case to calculate % and code to pass the test
- Create a test to check if the given values are positive 
- Create a method in the class to pass the test

### First Steps
- 1. Create a test file called `TDD_task.py` 
- 2. Create a file called `Test_TDD.py`
- 3. Write `pip install pytest` into the terminal and import pytest and unittest
    
## Code
### TDD_task
```
import unittest
import pytest

from Test_TDD import TestCalcs

class TestDivisible(unittest.TestCase):

    nums = TestCalcs()

    def test_divisible(self):
        self.assertEqual(self.nums.divisible(6, 6), 1)

    def test_positive(self):
        self.assertEqual(self.nums.positive(6), True)
```
### Test_TDD
```
class TestCalcs:

    def divisible(self, num1, num2):
        return num1 % num2

    def positive(self, num):
        return num > 0
```
- Finally in the terminal type `python -m pytest` and run. Check if all tests have passed