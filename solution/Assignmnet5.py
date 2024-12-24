def is_palindrome_4(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    stack = list(s)  # Convert string to stack (list)
    reversed_str = ''.join([stack.pop() for _ in range(len(stack))])  # Reverse the string using stack
    return s == reversed_str

# Test
input_string = "A man a plan a canal Panama"
print(f"Is palindrome? {is_palindrome_4(input_string)}")
