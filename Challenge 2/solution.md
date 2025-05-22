# Solution to the challenge 2

## messy_script.py

```python
def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        int: The sum of the numbers in the list.
    """
    return sum(numbers)  # Using Python's built-in sum function for better performance and readability


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Sum:", calculate_sum(numbers))
```

## test_messy_script.py

```python
import unittest
from messy_script import calculate_sum

class TestCalculateSum(unittest.TestCase):
    def test_calculate_sum_with_positive_numbers(self):
        self.assertEqual(calculate_sum([1, 2, 3, 4, 5]), 15)

    def test_calculate_sum_with_negative_numbers(self):
        self.assertEqual(calculate_sum([-1, -2, -3, -4, -5]), -15)

    def test_calculate_sum_with_mixed_numbers(self):
        self.assertEqual(calculate_sum([-1, 2, -3, 4, -5]), -3)

    def test_calculate_sum_with_empty_list(self):
        self.assertEqual(calculate_sum([]), 0)

    def test_calculate_sum_with_single_element(self):
        self.assertEqual(calculate_sum([42]), 42)

if __name__ == "__main__":
    unittest.main()
```

## Run command for power shell

```powershell
python -m unittest test_messy_script.py
```