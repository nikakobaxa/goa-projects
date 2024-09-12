# num = 10
# num1 = 20

# print(num + num1)

# str = "trent"

# str1 = "alexander"

# result = str + str1

# print(result)

#კონკატენაცია არის ოპერაცია, რომელიც სერიოზულ სტრინგებს აერთიანებს ერთ სტრინგში.


# num = 20

# num1 = 10

# print(num/num1)

#როდესაც ორი მთელი რიცხვი (integer) იყოფა ერთმანეთზე, Python ავტომატურად ითვლის შედეგს როგორც float. 

# print(10 > 5)
# print(10 < 5)
# print(10 == 10)
# print(10 != 5)
# print(10 <= 5)
# print(10 >= 5)

# print(10 - 5 != 10 - 2)
# print(5 + 5 == 6 + 4)

# print(False and True)
# print(False or True)
# print(True or True)
# print(False and False)
# print(False or False)
# print(True and True)
# print(True or False and False or True)
# print(True and False and False and True)


# print(5 > 3 and 10 < 20)
# print(20 == 20 or 10 > 20)
# print(20 > 30 and 20 == 10)
# print(30 != 10 and 20 > 30)
# print(20 > 15 or 10 < 20)


# for i in range(10):
#     print(i)

# numbers = [1, 2, 3, 4, 5]

# total_sum = 0

# for number in numbers:
#     total_sum += number

# print(total_sum)

# for i in range(10):
#     print("hello world")


# number = 1

# while number <= 10:
#     print(number)
#     number += 1


# number = 1

# while number <100:
#     if 50 <= number <= 60:
#         number += 1
#         continue

#     print(number)
#     number += 1


# total_sum = 0
# number = 1

# while total_sum < 50:
#     total_sum += number
#     number += 1

# print(total_sum)
# print(number - 1)


# num1 = int(input("Enter a number: "))

# print(num1 //  3)
# print(num1 // 5)


# def calculate_average(numbers):
#     if not numbers:
#        return None
    
#     total_sum = sum(numbers)

#     average = total_sum / len(numbers)

#     return average

# test_case = [1,2,3,4,5,2]

# result = calculate_average(test_case)
# print(result)


# def zebra(string):
#     count = 0
#     new_string = ""

#     for i in string:
#         if count % 2 == 0:
#            new_string += i.upper()
#         else:
#             new_string += i
#         count += 1
#         print(new_string)

# zebra("hello")        




# str = "hello"

# x = str.upper()

# print(x)

def squared_elements(numbers):
    squared_list = [x ** 2  for x in numbers]
    return squared_list


input_list = [3,12,5,2,6]
output_list = squared_elements(input_list)
print(output_list)

# str = "hello world"

# x = str.upper()

# print(x)



# str0 = "HELLO WORLD"

# i = str0.lower()

# print(i)



# str1 = "trent"

# o = str1.capitalize()

# print(o)



# str2 = "HeLlo NiKa"

# p = str2.swapcase()

# print(p)



# str3 = "hello nika"

# a = str3.find("nika")

# print(a)



# mylist = ["nika", "luka"]
# c = len(mylist)

# print(c)




# fruits = ['apple', 'banana', 'cherry']

# x = fruits.index("cherry")

# print(x)



# mylist2 = ["nika"]

# mylist2.append("luka")

# print(mylist2)




# mylist3 = ["nika", "luka", "giorgi"]

# mylist3.insert(2,"daviti")

# print(mylist3)




# mylist4 = ["nika", "luka", "giorgi"]

# mylist4.pop(1)

# print(mylist4)



# mylist5 = ["gio", "luka", "nika"]

# mylist5.remove("nika")

# print(mylist5)
