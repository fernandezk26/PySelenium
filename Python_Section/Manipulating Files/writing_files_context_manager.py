my_string = "I love to program in Python"

#example 1
with open("./sample_files/sample_output2.txt", 'w') as f:
    f.write(my_string)

#example 2, writing a list
my_list = ['user 1', 'user 2', 'user 3']
with open("./sample_files/sample_output2.txt", 'w') as f:
    for i in my_list:
        f.write(i + '\n')

#example 3 (appending)
var2 = "Also love testing"
with open("./sample_files/sample_output2.txt" , 'a') as f:
    f.write("\n")
    f.write(var2)

#example 4
my_langs = ['python', 'js', 'php', 'ruby']
with open('./sample_files/my_fav_languages.csv', 'w') as f:
    str_my_langs = '\n'.join(my_langs)
    f.write(str_my_langs)