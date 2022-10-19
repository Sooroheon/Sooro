file = open('hello.txt', 'rt')

line_list = file.readlines()
print(line_list)
for line in line_list:
    print(line, end='')

file.close()

=
line_list = file.readlines()
for no, line in enumerate(line_list):
    print('{} {}'.format(no+1, line), end='')