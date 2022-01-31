# name = input("What's your name?")
# print("hello, ", name)
#
# age = input("what's your age?")
#
# isinstance is a method that returns true if the first parameter is the same data type as the second
# while not isinstance(age, int):
#     try:
#         age = int(age)
#         age += 1
#         print("Next year you will be ", age)
#     except ValueError:
#         print("You must enter a number")
#         age = input("How old are you?")
#
# print("agr1", "arg2", end = ",", sep = ",")
# print("arg3", "arg4", sep = ",")

# file = open("/Users/hugh/Desktop/School/Platform Based Computing/In Class/week3_files/top_ten_movies.txt")
# text = file.read()
# print(text)

# with open("/Users/hugh/Desktop/School/Platform Based Computing/In Class/week3_files/top_ten_movies.txt") as file2:
#     for line in file2:
#         #rstrip makes it so it doesn't print out the unnecessary new line characters
#         print(line.rstrip())

list = []
with open("/Users/hugh/Desktop/School/Platform Based Computing/In Class/week3_files/movies_only.txt") as file3:
    for line in file3:
        list.append(line.rstrip())

print(list)

name_height = {}
with open("/Users/hugh/Desktop/School/Platform Based Computing/In Class/week3_files/heights.txt") as file4:
    for line in file4:
        new_line = line.split() #splits a string into a list of strings
        name_height[new_line[0] + " " + new_line[1]] = int(new_line[2])

print(name_height)




