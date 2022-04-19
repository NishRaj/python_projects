count_of_words = 0
sum_of_words =0
while True:
    word = input("Enter a word: ")
    if word == 'q' or word == 'quit':
        break
    sum_of_words += len(word)
    count_of_words += 1
if count_of_words != 0:
 print(sum_of_words/count_of_words)