import re

# Regular expression match the pattern in the string

text = "The big brown bag"
pattern = r"big"

search = re.match(pattern, text)
if search:
    print("Match found:", search.group())
else:
    print("Match not found")

