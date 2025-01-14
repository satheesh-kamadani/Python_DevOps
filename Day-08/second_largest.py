# Find the second largest form the list

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

my_list = [1, 10, 25, 76, 89, 100]
second_largest = find_second_largest(my_list)
print(f"Second largest number from the list is: {second_largest}")