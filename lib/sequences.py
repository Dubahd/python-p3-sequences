#!/usr/bin/env python3

def print_fibonacci(length):
    """
    Print a list of the Fibonacci sequence up to the specified length.
    
    Args:
        length (int): The number of Fibonacci numbers to generate
    
    Returns:
        None: The function prints the list directly
    """
    # Handle edge cases
    if length == 0:
        print([])
        return
    
    if length == 1:
        print([0])
        return
    
    # Initialize the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    
    # Generate Fibonacci numbers until we reach the desired length
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    # Print the sequence
    print(fibonacci_sequence)