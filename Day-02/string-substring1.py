# Search for a text in the string and report

text = "Python is a awesome programming language"
substring = input("Enter the text to be searched:")
if substring in text:
    print(substring, "found in the text")
else:
    print(substring, "not found in the text")
    