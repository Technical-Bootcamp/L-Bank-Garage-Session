# Solution to the challenge 2

## Use GitHub Copilot Agent Mode

<details>
<summary>Click for Solution #1</summary>

    Improve readability and structure of the script

</details>

<details>
<summary>Click for Solution #2</summary>

    Optimize the performance
    
</details>

<details>
<summary>Click for Solution #3.0</summary>

    Switch to the Agent Mode
    
</details>

<details>
<summary>Click for Solution #3</summary>

    Generate unit tests for the script
    
</details>

<details>
<summary>Click for Solution #4</summary>

    Test all edge cases and incorrect input parameters
    
</details>

<details>
<summary>Click for Solution #5</summary>

    Run the test
    
</details>

## Results

<details>
<summary>Possible resulting files</summary>

## messy_script.py

```python
from typing import List

def calculate_sum(numbers: List[int]) -> int:
    # The calculate_sum function is already optimized using Python's built-in sum function.
    return sum(numbers)

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

    def test_calculate_sum_with_large_numbers(self):
        self.assertEqual(calculate_sum([10**6, 10**6, 10**6]), 3 * 10**6)

    def test_calculate_sum_with_single_element(self):
        self.assertEqual(calculate_sum([42]), 42)

    def test_calculate_sum_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            calculate_sum([1, 2, 'three', 4])

    def test_calculate_sum_with_none(self):
        with self.assertRaises(TypeError):
            calculate_sum(None)

    def test_calculate_sum_with_nested_list(self):
        with self.assertRaises(TypeError):
            calculate_sum([1, [2, 3], 4])

if __name__ == "__main__":
    unittest.main()
```

## Run command for power shell

```powershell
python -m unittest discover -p "test_*.py" 
```

</details>
