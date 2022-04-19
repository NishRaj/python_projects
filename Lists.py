# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 22 11:45:09 2021

# @author: nishank
# """

# from re import X


# sentence = "Hi Nirvi, how are you feeling today? Hope everything is good at your end."
# listSentence = sentence.split();
# print(listSentence);

# list_sentence = ['Hi' , 'how', 'what', 'which', 'why', 'when']
# mySentence = "---".join(list_sentence);
# print(mySentence);
# input_list=['SAS', 'R', 'PYTHON', 'SPSS'];
# #del input_list[3];
# input_list.remove('SPSS');
# print(input_list);
# input_list.append('SPARK');
# print(input_list);
# input_str = 'I love Data Science & Python';
# new_list = input_str.split("& ");
# print(new_list);
# python_list =  ['Pythons syntax is easy to learn', 'Pythons syntax is very clear'];
# python_string = " & ".join(python_list);
# print(python_string);
# #Length of the list
# list_cal_length = [1,2,2,3,4,5,6,7];
# print(len(list_cal_length));
# #nested lists
# nest_list = [[1,2,2,4], ['Hi','this','is','Nirvi'], ['Hey','dont','forget','Abhyuday']];
# print(nest_list[0]);
# print(nest_list[1][3]);
# x1 = [1,2,3,1,1,1]
# list_cal_length.extend(x1)
# print(list_cal_length)

my_list = [1,2,3,4,2,1,5,6,7,8,9]
new_list = my_list[::-1]
#9,7,5,2,3,1
print(new_list)