# Rotating the list by k steps

def rotate_list(lst, k):
    k = k % len(lst)  # In case k is greater than the length of the list
    return lst[-k:] + lst[:-k]

# Example usage
my_list = [1, 2, 3, 4, 5]
k = 2
rotated_list = rotate_list(my_list, k)
print(f"List after rotating by {k} steps: {rotated_list}")