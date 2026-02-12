file1 = open("./data/courses.txt", "r")
content = file1.read()    # reads the file content as single string
print(content)
file1.close()