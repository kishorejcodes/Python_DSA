#input : tomato mo
#output: om

def func_to_get_indices(repeat_letters):
    index_list_2 = []
    for index in repeat_letters:
        char = string_1[index]
        list_x = []
        for i in range(index,len(string_1)):
            if (char == string_1[i]):
                list_x.append(i)
        index_list_2.append(tuple(list_x))
    return index_list_2

def func_to_get_combinations(list_x, a,z=0, temp = []):
    len_x = len(list_x)
    for i in range(z, len(list_x)):
      for j in range(len(list_x[i])):
        if (a > 1):
            func_to_get_combinations(list_x, a-1,i+1, temp + [list_x[i][j]])
        else:
            main_list.append(temp + [list_x[i][j]])

            
string_1, string_2 = input().split()
flag = True
index_list_1 = []
repeat_letters = []
for i in range(len(string_2)):
    if (string_2[i] in string_1):
        index = string_1.index(string_2[i])
        
        if (string_1.count(string_2[i]) > 1):
            repeat_letters.append(index)
        else:
            index_list_1.append(index)
    else:
        flag = False
        break
index_list_2 = func_to_get_indices(repeat_letters)
main_list = []
func_to_get_combinations(index_list_2, len(index_list_2))
all_words = []
all_words_char_count = []
for i in range(len(main_list)):
    fin_index_list = index_list_1 + main_list[i]
    start_index = min(fin_index_list)
    end_index = max(fin_index_list)
    final_string = string_1[start_index:end_index+1]
    all_words.append(final_string)
    all_words_char_count.append(len(final_string))

if repeat_letters == []:
    print(string_1[min(index_list_1):max(index_list_1)+1])
else:
    index = all_words_char_count.index(min(all_words_char_count))
    print(all_words[index])


'''
Problem Statement:
Given two strings str1 and str2. Have to find out the minimum substring of str1 that contains all the characters of str2.

TestCase:
Input : tomato mo
Output : om

TestCase:
Input : harrypotter try
Output : rypot
'''
