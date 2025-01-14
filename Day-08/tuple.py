# Tuple

my_tuple = (1, 3, "apple", "banana")
print(my_tuple)

my_element = my_tuple[1]
print(my_element)

tuple_length = len(my_tuple)
print(tuple_length)

coordinates = (3,4)
x, y = coordinates
print(x, y)

new_tuple = my_tuple + (5, "grapes")
print(new_tuple)

is_present = "banana" in my_tuple
print(is_present)

def get_coordinates():
    return (3, 4)
x, y = get_coordinates()
print(x, y)