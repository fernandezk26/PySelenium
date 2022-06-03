
my_string = "I love to program in Python"

#example 1 (folder has to exist, file does not have to exist)
my_file = open('./sample_files/sample_output1.txt' , 'w')
#'w' will overrite, 'a' will append
my_file.write(my_string)
my_file.close()

#example 2
my_file = open('./sample_files/sample_output1.txt' , 'w')
my_file.write(my_string)
my_file.write("\n")
my_file.write(my_string)
my_file.write("\n")
my_file.write(my_string)
my_file.write("\n")
my_file.close()