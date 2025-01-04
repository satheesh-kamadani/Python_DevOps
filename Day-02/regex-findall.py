import re

# Regular expression find text in the string

text = "Python is awesome"
pattern = input("Enter the text to be searched:")

search = re.search(pattern, text)
if search:
    print("Pattern found", search.group())
else:
    print("Pattern not found")

