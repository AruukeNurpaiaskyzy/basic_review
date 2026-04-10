# print("Hello", "world", sep=", ")
# # print("first row", end='   ')
# # print("second row")
# input("please enter something")
# name = input("enter your name: ")
# print(name)
# name = "alice"
# other_name = name
# print(other_name)
# my_integer = 10
# my_float = 0.20
# t= 30
# z = 2
# d = t * z
# print(d)
# x = 2
# print(x**3)


# flat_number = 21
# entrance_number = (flat_number-1) // 20 + 1
# print(entrance_number)


# x = 1
# y = 9
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)
# x = 1
# print(x<5 and x>-2)
# my_integer = 100
# my_string = str(my_integer)
# print(type(my_string))


# my_string = input ("Enter a number: ")
# print(type(my_string))
# big_integer = 2**1000
# print(len(str(big_integer)))
# my_string = "Hello, world"
# print("Hello" in my_string)
my_string = input("Enter a number: ")
if my_string.isdigit():
    my_integer = int(my_string)
    print(my_integer)
else:
    print(f'{my_string} is not a number')