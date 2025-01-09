import sys

type = sys.argv[1]

if type == "t2.micro":
    print("This will charge you 2 dollars per day")
elif type == "t2.medium":
    print("This will charge you 4 dollars per day")
elif type == "t2.xlarge":
    print("This will charge you 8 dollars per day")
else:
    print("Please enter the valid instance name")
    