# Age group

age = int(input("Enter the age: "))

if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior")
else:
    print("Invalid age")
