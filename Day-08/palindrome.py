# Check whether the list is a palindrome or not

def is_palindrome(numbers):
    return numbers == numbers[::-1]

my_list = [1, 2, 3, 2, 1, 5]
if is_palindrome(my_list):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")