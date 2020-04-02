# my_file = open("firstFile.txt", "r")
#
# print(str(my_file.read()))
# print(str(my_file.readline()))
# my_file.close()


with open("firstFile.txt", "w") as writeExample:
    writeExample.write("This is nice 2")

with open("firstFile.txt", "r") as readExample:
    print(str(readExample.read()))
