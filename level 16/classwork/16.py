# def greet():
#     return  "Hello world"
 
# print(greet())


# def greet(name):
#     return f"Hello {name}"

# print(greet("nika"))

# def multiply(x, y):
#     return x * y

# result = multiply(10, 20)

# print(result)


# def multiply(a, b, c):
#     return a + b + c

# result = multiply(5,4,6)
# print(result)

# def is_adult(age):
#     if age >= 20:
#       return "you are adult"
#     else: 
#       return "not an adult"
    
# user_age = 21
# print(is_adult(user_age))


# def qula(score):
#   if 1 <= score <= 100:
#     if score >= 80:
#       return "ჩააბარე"
#     else:
#       return "ვერ ჩააბარე"
    
# user_score = 85
# print(qula(user_score))    


from turtle import *

width(4)

def drive_square(size):
    for i in range(4):
        forward(size)
        left(90)
drive_square(250)        

penup()
goto(-280, 0)
pendown()
  
drive_square(250)

penup()
goto(-280,-280)
pendown()

drive_square(250)

penup()
goto(-280,-280)
pendown()

drive_square(250)

penup()
goto(0,-280)
pendown()

drive_square(250)

exitonclick()

