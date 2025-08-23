"""
Utility functions for the Cautious Broccoli project.

This module provides helper functions that demonstrate
clean, readable Python code without requiring external tools.
"""


def greet_user(name: str) -> str:
    """
    Generate a personalized greeting message.
    
    Args:
        name (str): The name of the user to greet
        
    Returns:
        str: A formatted greeting message
    """
    return f"Hello, {name}! Welcome to the Cautious Broccoli project."


def calculate_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Fibonacci number position cannot be negative")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b