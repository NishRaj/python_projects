s = 'hello'
z = '@#'
print(s[-1])
print(s[0])
print(len(s))
print(s.count('l'))
print(s.find('l'))
print(s.upper())
print(s.capitalize())
print(z.isalnum())
print(float('3.14'))
contains = 'z' in s
print(contains)

digit_str = '19a'
if digit_str.isdigit():
    print(int(digit_str))
else :
    print(digit_str , ' is not a digit.')

# Split
nish = 'Hello my name is Nishank'
print(nish.split(" "))

# Replace
replace_str = 'Hi, you , are , a , moron!'
print(replace_str.replace(',','#'))
print(replace_str)

#Fstring
#name = input("Please enter your name: " )
#s = F"Hello, {name}!, How are you?"
#print(s)

#String Multiplication
newName = "Nirvi"
print(newName * 5)

#Escape character
str_escape = f'Nishank\'s'
print(str_escape)

#String join
lst = ['n','i','r','v','i']
print("".join(lst))
#sentence = input("Enter a sentence: ")
#wordList = sentence.split(" ")
#num_of_words = len(wordList)
#print(num_of_words)
string1 = "aabbcsdw"
string2 = "abbbcsdd"

# Write your code here.
for idx,char in enumerate(string1):
    if char == string2[idx]:
        print(char)