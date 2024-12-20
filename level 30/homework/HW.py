try:
    print(my_variable)
except:
    print("variable is not found")

my_list = [10,20,30,40]

try:
    print(my_list[5])
except:
    print("5 is not found in list")
finally:
    print("try again")

try:
    value = int("abc")
except:
    print("not found int")

    def sum_mixed(numbers):
     return sum([int(x) if isinstance(x, str) and x.isdigit() else x for x in numbers])
    


#lambdaa

add = lambda x, y:x + y
print(add(10, 10))
max_value = lambda x, y: x if x > y else y
print(max_value(10, 20))
max_value = lambda x, y: x if x < y else y
print(max_value(10, 20))
full_name = lambda first, last: first + " " + last
print(full_name("nika", "kobakhidze"))
is_even = lambda x,: x % 2 == 0
print(is_even(4))
age_check = lambda age: True if age >= 18 else False
print(age_check(10))