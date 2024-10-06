# def manual_max(lst):
#     max_num = lst[0]

#     for i in lst:         
#           if max_num < i:
#             max_num = i
#     return max_num

# print(manual_max([1,2,5,7,8,9,100,-90]))

# def manual_replace(s):
#     return s.replace('!', '')

# text = "Hello world!"
# new_text = manual_replace(text)
# print(new_text)

# def manual_append(original, to_append):
#     return original + to_append

# text = "Hello"
# additional_text = "World!"
# new_text = manual_append(text, additional_text)
# print(new_text)

#აბრუნებს item-დან ინტეჯერს

# def filter_list(l):
#     return [item for item in l if isinstance(item, int)]

# print(filter_list([1, 2, 'a', 'b']))

#აბრუნებს item-დან სტრინგს

# def filter_list(l):
#     return [item for item in l if isinstance(item, str)]

# print(filter_list([1, 2, 'a', 'b']))


# def middle_lenght(word):
#     lenght = len(word)

#     if lenght % 2 == 1:
#         return word[lenght // 2]
#     else:
#         mid_index = lenght // 2
#         return word[mid_index - 1: mid_index + 1]
    
# print(middle_lenght("word"))
# print(middle_lenght("varduashvil"))
