text = input("Please enter the text: ")
freq_table = dict()
vowel_freq_table = ['a','e','o','u','i']
# for letter in text:
#     if letter in freq_table:
#         freq_table[letter] +=1
#     else:
#         freq_table[letter]=1
# print(freq_table)
for letter in text:
    if letter in vowel_freq_table:
        freq_table.setdefault(letter,0)
        freq_table[letter] +=1
print(freq_table)