def file_output():
    f = open('foo.txt')
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()
    f.close()

file_output()