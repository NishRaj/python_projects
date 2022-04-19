def caesar_cipher(string, offset):
    lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string_lst = list(string)
    new_list = []
    for char in string_lst:
        idx = lst.index(char)
        offset_idx = idx - offset
        offset_char = lst[offset_idx]
        new_list.append(offset_char)
    return ''.join(new_list)
print(caesar_cipher('ega',3))