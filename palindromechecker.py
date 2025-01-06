# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is the same when reversed
    return s == s[::-1]

# Input from the user
string = input("Enter a string to check if it's a palindrome: ")

# Check and display the result
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
