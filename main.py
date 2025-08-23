"""
Cautious Broccoli - A simple Python demonstration script.

This script demonstrates basic Python functionality without requiring
external code analysis tools or subscriptions.
"""

from utils import greet_user, calculate_fibonacci


def main():
    """Main function demonstrating basic functionality."""
    print("Welcome to Cautious Broccoli!")
    
    # Demonstrate greeting functionality
    name = "Developer"
    greeting = greet_user(name)
    print(greeting)
    
    # Demonstrate calculation functionality
    print("\nFibonacci sequence (first 10 numbers):")
    for i in range(10):
        fib_num = calculate_fibonacci(i)
        print(f"F({i}) = {fib_num}")
    
    print("\nDemo completed successfully!")


if __name__ == "__main__":
    main()