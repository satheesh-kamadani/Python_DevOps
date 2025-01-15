# Element occcurance in a list

def count_occurance(numbers, element):
    return numbers.count(element)

my_list = [1, 1, 2, 2, 4, 5, 6, 8, 8, 9, 5]
number = int(input("Enter the element: "))
count = count_occurance(my_list, number)
print(f"The occurance of the element {number}: {count}")