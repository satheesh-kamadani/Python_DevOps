# Merge two sorted list

def merge_two_sorted_list(numbers1, numbers2):
    sorted_list = sorted(numbers1 + numbers2)
    return  sorted_list

my_list = [2, 3, 5, 1, 4]
my_list1 = [7, 9, 6, 10, 8]
sorted_list = merge_two_sorted_list(my_list, my_list1)
print(f"Merged two sorted list: {sorted_list}")