# Large and small elements in list

def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest

my_list = [3, 8, 1, 7, 16, 100, 102, 319]
largest, smallest = find_largest_and_smallest(my_list)
print(f"Largest: {largest}, Smallest: {smallest}")


    

my_list = [3, 8, 1, 7, 16, 100, 102, 319]

