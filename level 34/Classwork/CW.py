
def manual_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))  
    return result

numbers = [10, 20, 50, 70]
squared_numbers = manual_map(lambda x: x * 2, numbers)
print(squared_numbers)


def manual_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
         result.append(item)
    return result

numbers1 = [9, 2, 3]
even_numbers = manual_filter(lambda x: x % 2 == 0, numbers1)
print(even_numbers)

