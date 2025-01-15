# Find common elements in two lists

def find_common_elements(numbers1, numbers2):
    return list(set(numbers1) & set(numbers2))


my_list = [1, 2, 3, 5, 6, 9, 10]
my_list1 = [1, 2, 3, 5, 8, 7]
common_elements = find_common_elements(my_list, my_list1)
print(f"Common elements in both the list are: {common_elements}")

