# Remove duplicates from a list

def remove_duplicates(numbers):
    return list(set(numbers))

my_list = [1, 1, 1, 1, 2, 2, 2, 10, 5, 5,]
unique_list = remove_duplicates(my_list)
print(f"List with duplicates removed: {unique_list}")