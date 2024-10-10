def apply_map_filter(numbers):
    """
    Apply map to square each number and filter to keep only even squares.
    
    Args:
        numbers (list): A list of integers.
        
    Returns:
        list: A list of even squares of the input numbers.
    """
    # Using map with a lambda function to square each number
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    
    # Using filter with a lambda function to filter even numbers
    even_squares = list(filter(lambda x: x % 2 == 0, squared_numbers))
    
    return even_squares


if __name__ == "__main__":
    # Sample input
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Output: even squares of the input numbers
    result = apply_map_filter(numbers)
    print(f"Even squares: {result}")
