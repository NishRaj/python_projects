vowels = ['a','e','o','u','i']
word = input("Please input a word: ")
found = []
for letter in word:
    if letter.casefold() in vowels:
        if letter not in found:
            found.append(letter)
found.extend([4,5,6])
found.insert(100,'hi')
try:
    found.remove('f')
except ValueError:
    pass
print(found)