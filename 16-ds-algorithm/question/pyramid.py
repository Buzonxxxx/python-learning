def print_pattern(s, n):
    """
    Given a string 's' and an integer 'n', this function prints a new string pattern.
    The pattern starts with the first character of 's', continues with the next characters
    in sequence up to the nth character, then reverses (excluding the nth character) to create
    a symmetrical pattern. The length of the pattern is 2 * n - 1.
    
    Example usage:
    If s = 'abcdefglkjhgfd', and n = 2, the function prints 'aba'.
    If n = 3, it prints 'abcba'.
    If n = 4, it prints 'abcdcba'.
    
    Parameters:
    s (str): The input string to create the pattern from.
    n (int): The number of characters to include in the pattern before reversing.
    
    Returns:
    None: This function does not return a value; it prints the pattern directly.
    """
    # Check if n is equal to 1
    if n == 1:
        print(s[0])  # Print the first character of the string
    else:
        pattern = s[:n]  # Initialize the pattern with the first n characters of the string
        # Append the characters in reverse order (excluding the nth character)
        for i in range(n-2, -1, -1):
            pattern += s[i]
        print(pattern)  # Print the pattern

# Example function calls:
print_pattern('abcdefglkjhgfd', 2)  # Expected output: 'aba'
print_pattern('abcdefglkjhgfd', 3)  # Expected output: 'abcba'
print_pattern('abcdefglkjhgfd', 4)  # Expected output: 'abcdcba'

