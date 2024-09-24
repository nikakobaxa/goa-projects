# registered_password = "kobaxa12"
# authorised = False

# while authorised != True:
#     user_input = input("Enter your password: ")

#     if user_input == registered_password:
#      print("access granted!")
#      authorised = True

#     else:
#        print("incoret password please try again")


# i = 1
# sum = 0

# while i <= 100:
#     print(i)
#     sum = sum + i
#     i = i + 1

#     print(sum)

# print(5 < 1) #False
# print(1 > 0) #True
# print(5 == 5) #True
# print(5 != 6) #True
# print(5 >= 5) #True
# print(5 <= 5) #True

True #ჭეშმარიტი
False #არ არის ჭეშმარიტი 


# nika = int(input("Enter your age: "))
# aleqsandre = int(input("Enter your age: "))

# print(nika < aleqsandre)
# print(nika > aleqsandre)
# print(nika == aleqsandre)
# print(nika != aleqsandre)
# print(nika >= aleqsandre)
# print(nika <= aleqsandre)

# score = 120
# score1 = 95
# score3 = 100

# print(score > score3)
# print(score1 > score3)


# seats = 100

# while seats >= 100:
#     print("You can sit ")
# else:
#     print("you cant sit ")

# seats = 100

# for seats in range(100):
#     print("congrat your seats is empty")
#     print(seats)
# else:
#     print("sorry seats is not empty")
#     seats = seats + 1
    

# reqruit_goal = 3
# reqruit_assist = 1

# goal = int(input("Enter your goal: "))
# assist = int(input("Enter your assist: "))

# print(reqruit_goal == goal or reqruit_assist == assist)
# print(goal + assist)



# ball = 10

# while ball <=11:
#     print("Goal!")

# if heart_rate < 40: 
#   print("Low heart rate")
# elif heart_rate >= 180: 
#   print("High heart rate")
# else:
#   print("Normal range")



# def mwvadi(string):
#     count = 0
#     new_string = ""

#     for i in string:
#         if count % 3 == 0:
#             new_string += i.upper()
#         else:
#             new_string += i
#         count += 1
#         print(new_string)

# mwvadi("nika")

# def repeat_str(repeat, string):
#     return repeat * string

# result = repeat_str(6, "i")
# result = repeat_str(5, "hello")

# print(result)

# def summation(num):
#     return sum(range(1, num + 1))

# print(summation(5))
# print(summation(10))

# def greet():
#     return "Hello world"

# print(greet())


# def manual_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num

#     return total

# numbers = [1, 2, 3, 4, 5]
# result = manual_sum(numbers)
# print(result)    


# def manual_len(lst):
#     count = 0
#     for _ in lst:
#         count += 1
#     return count

# lst = [1, 2, 3, 4, 5]
# result = manual_len(lst)
# print(result)


# def manual_min(lst):
#     if not lst:
#         return None
         
#     min_value = lst[0]
#     for num in lst:
#         if num < min_value:
#             min_value = num

#     return min_value

# my_list = [1, 2, 3, 4, 5]
# result = manual_min(my_list)
# print(result)

# str = ["hello", "nika", "luka"]

# x = len(str)

# print(x)

# def average(numbers):

#     total = sum(numbers)
#     count = len(numbers)
#     return (total / count)

# my_list = [1, 2, 6, 7, 8]
# print(average(my_list))

# def assembly(numbers):
#     return sum(numbers)

# list = [10, 20, 40]
# print(assembly(list))

# def Element(numbers):
#     return len(numbers)

# list1 = [10, 20, 40]
# print(Element(list1))

# def Element(numbers):
#     if numbers  % 2 == 0:
#         return "odd"
#     else:
#         return "even"

# numbers = 2
# print(Element(numbers))

# str = "i like bananas"

# x = str.replace("bananas", "apple")

# print(x)

# def remove_spaces(input_string):
#     return input_string.replace(" ", "")

# result = remove_spaces("Hello nika how are you?")
# print(result)

# def greet(name):
#     return f"Hello {name}"

# result = greet("nika")
# print(result)

# def bool_to_string(b):
#      return str(b)

# result_True = bool_to_string(True)
# result_False = bool_to_string(False)

# print(result_True)
# print(result_False)

# def basic_op(operator, value1, value2):
#     if operator == '+':
#        return value1 + value2
#     elif operator == '-':
#         return value1 - value2
#     elif operator == '*':
#         return value1 * value2
#     elif operator == '/':
#         return value1 / value2
    
# print(basic_op('+', 14, 20))
# print(basic_op('-', 20, 10))
# print(basic_op('*', 10, 20))
# print(basic_op('/', 20, 5))

# def ger_century(year):
#      return (year + 99) // 100

# print(ger_century(200))


# def maps(a):
#     return [x * 2 for x in a]

# original_array = [1, 10, 20, 4]
# double_array = maps(original_array)
# print(double_array)


# def digitaze(n):
#     return [int(digit) for digit in str(n)][::-1]

# print(digitaze(35231))
# print(digitaze(0))


# def timmy_sara(love_timmy, love_sara):
#       return (love_timmy % 2 == 0) != (love_sara % 2 == 0)
     
# print(timmy_sara(4,3))