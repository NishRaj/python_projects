def get_n_longest_unique_words(words, n):
    mul_occurence_set  = set()
    longest_unique_word_list = []
    word_list = list(words)
    for word in word_list:
        word_count = word_list.count(word)
        if word_count > 1:
            mul_occurence_set.add(word)
    list_removing_duplicates = list(set(word_list) - mul_occurence_set)    
    list_removing_duplicates.sort(reverse=True, key=sort_on_len)
    for i in range(n):
        longest_unique_word_list.append(list_removing_duplicates[i])
    return longest_unique_word_list
def sort_on_len(item):
    return len(item)

    