charSet = set()

while True:
    char = input('Enter a character: ')
    if char in charSet or len(char) > 1:
        break
    charSet.update(char)
print('Number of unique characters entered: ',len(charSet))