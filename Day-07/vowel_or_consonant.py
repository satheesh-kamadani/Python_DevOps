# Vowel or consonant

char = input("Enter the letter: ").lower()

if char in "aeiou":
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")