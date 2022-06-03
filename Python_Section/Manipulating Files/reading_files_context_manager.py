import pdb
#preferred method

#example 1
sample_file = "./sample_files/file.txt"

with open(sample_file, 'r') as f:
    content = f.read()

print(content)

#example 2
sample_file2 = "./sample_files/countries.txt"

with open(sample_file2, 'r') as my_f:
    countries = my_f.read().split("\n")

print(countries)

#example 3
sample_file2 = "./sample_files/fruits.txt"

with open(sample_file2, 'r') as my_file:
    fruits = my_file.readlines()

list_of_fruits = [i.strip() for i in fruits]

print(list_of_fruits)