import sys
import os

# Adjust the path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import apply_map_filter  # Import your function from app.py

def test_apply_map_filter():
    # Test cases to validate the functionality of apply_map_filter
    assert apply_map_filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 16, 36, 64, 100]
    assert apply_map_filter([1, 3, 5]) == []         # No even squares
    assert apply_map_filter([0, 2, 4]) == [0, 4, 16]  # Include the even squares after squaring


if __name__ == "__main__":
    test_apply_map_filter()
    print("All tests passed!")
