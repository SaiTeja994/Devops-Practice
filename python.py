#python code for palindrome
def is_palindrome(s):
    return s == s[::-1]
#test the function
print(is_palindrome("radar")) #True
print(is_palindrome("python")) #False
