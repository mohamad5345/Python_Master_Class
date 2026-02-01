inp = input("Sample input: ")

def isPalindrome(text):
    if text == text[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

isPalindrome(inp)