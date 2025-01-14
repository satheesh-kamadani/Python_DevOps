# Reverse the list

def reverse_list(numbers):
    numbers.reverse()
    return numbers

my_list = [1, 2, 3, 4, 5]
new_list = reverse_list(my_list)
print(f"Reversed list: {new_list}")