#reccomended:
# with open("/path/to/my/file.txt", <mode>) as Variable
#     content=variable.read()
#     <do some work with content>
# <or do some work with content>

sample_file = './sample_files/file.txt'

my_file = open(sample_file, 'r')
content = my_file.read()
my_file.close()

print(content)