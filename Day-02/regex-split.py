import re

# Regular expression split words in the string

text = "apple, banana, orange, grape, kiwi"
pattern = r","

split_text = re.split(pattern, text)
print("split results:", split_text)