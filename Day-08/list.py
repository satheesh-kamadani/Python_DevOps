# List

my_list = [10, 2, 15, "Banana", "Apple", "Orange"]
print(my_list)

print(my_list[1])

list_length = len(my_list)
print(list_length)

my_list.append(4)
print(my_list)

my_list.remove("Apple")
print(my_list)

new_list = my_list[2:5]
print(new_list)

new_list = my_list + [5, 6]
print(new_list)

my_list.remove("Banana")
my_list.remove("Orange")

my_list.sort()
print(my_list)

is_present = 10 in my_list
print(is_present)


