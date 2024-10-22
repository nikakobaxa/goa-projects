# 1  სიაში ელემენტების შექმნა

my_list = [1, 2, 3, 4, 5]
print(my_list)

# 2 ელემენტზე წვდომა

first_element = my_list[0]  
print(first_element)

# 3 ელემენტის შეცვლა

my_list[1] = 10
print(my_list)

# 4 ელემენტების დამატება

my_list.append(6)
print(my_list)

# 5 ელემენტის წაშლა

my_list = {"luka", "nika"}

my_list.remove("nika")
print(my_list)

# 6 სიაში ელემენტების რაოდენობის დადგენა

length = len(my_list)
print(length)

# 7 სიაში ელემენტის ძიება

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

# 8 ელემენტის რაოდენობის დადგენა

fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")

# 9 სიაში ელემენტების დალაგება

my_list = [3,2,5,7,20]
my_list.sort()
print(my_list)

# 10 სიების კოპირება

fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()

# 11  ფუნქციების გამოყენება list-ზე

def multiply_by_two(num):
    return num * 2

multiplied_list = list(map(multiply_by_two, my_list))
print(multiplied_list)

# 12 სიის გაწვდვა

for item in my_list:
    print(item)


# turple

# 1 Tuple-ის შექმნა

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# 2  Tuple-ის ერთ ელემენტიანი შექმნა

single_element_tuple = (1,)
print(single_element_tuple)

# 3  Tuple-ის ელემენტებზე წვდომა

first_element = my_tuple[0]  
print(first_element)

# 4  Tuple-ის ელემენტის შეცვლა

new_tuple = my_tuple[:1] + (10,) + my_tuple[2:]
print(new_tuple)

# 5 Tuple-ის დანამატები

another_tuple = (6, 7, 8)
combined_tuple = my_tuple + another_tuple
print(combined_tuple)

# 6 Tuple-ის ელემენტის წაშლა

reduced_tuple = my_tuple[:2] + my_tuple[3:]
print(reduced_tuple)

# 7 Tuple-ის სიგრძის დადგენა

length = len(my_tuple)
print(length)

# 8 Tuple-ის ელემენტის ძიება

index_of_3 = my_tuple.index(3)
print(index_of_3)

# 9 Tuple-ის ელემენტის რაოდენობის დადგენა

count_of_2 = my_tuple.count(2)
print(count_of_2)

# 10 Tuple-ის გაწვდვა 

for item in my_tuple:
    print(item)

# 11 Tuple-ის გაწვდვა და ფუნქციების გამოყენება

def multiply_by_two(num):
    return num * 2

multiplied_tuple = tuple(map(multiply_by_two, my_tuple))
print(multiplied_tuple)

# 12 Tuple-ის ნესტური

nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)

# 13 Tuple-ის გამოყენება როგორც ფუნქციის შედეგი 

def return_multiple_values():
    return 1, 2, 3

result = return_multiple_values()
print(result)

# set

# 1  Set-ის შექმნა

my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2 Set-ის ერთჯერადი შექმნა

single_element_set = {1}
print(single_element_set)

# 3 Set-ში ელემენტების დამატება

my_set.add(6)
print(my_set)

# 4  Set-ის ელემენტის წაშლა

my_set.remove(3)
print(my_set)

# 5 Set-ის გაწმენდა

my_set.clear()

print(my_set)

# 6  Set-ის ელემენტების რაოდენობის დადგენა

length = len(my_set)
print(length)

# 7  Set-ის გაწვდვა

for item in my_set:
    print(item)

# 8  Set-ის შეადარება

set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print(union_set)

# 9 Subset და Superset-ის შემოწმება

subset_check = {1, 2}.issubset(set_a)
print(subset_check)

# 10 Set-ის კლონირება

my_set_copy = my_set.copy()
print(my_set_copy)

# 11  Set-ის გამოყენება როგორც მონაცემთა სტრუქტურა

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(original_list)
print(unique_set)



# list

# ცვლილება: list შექმნილია მონაცემთა შენახვისთვის, რომლებზეც შესაძლებელი იქნება ცვლილებების განხორციელება (მონაცემების დამატება, შეცვლა, წაშლა). ეს საშუალებას აძლევს პროგრამისტებს ადვილად მართონ მონაცემები.
# მრავალფეროვნება: list-ში შესაძლებელია სხვადასხვა ტიპის მონაცემების შენახვა, რაც მისი გამოყენების ფართო სპექტრს იძლევა.
# წესრიგი: ელემენტების ჩანაწერი ინახება იმავე წესრიგში, რომელშიც ისინი შეიქმნება, რაც მარტივად შესაძლებელს ხდის მათი წვდომის პროცესში.

# turple

# უვნებლობა: tuple შექმნილია უვნებლობის (immutability) მიზნით. ეს ნიშნავს, რომ once a tuple is created, its contents cannot be changed. ეს მიზანშეწონილია, როდესაც საჭიროა მონაცემების სტაბილურობა და უსაფრთხოება.
# მონაცემების დაბრუნება: tuple-ები ხშირად გამოიყენება ფუნქციების მიერ რამდენიმე მნიშვნელობის დაბრუნებისთვის. მათ უნიკალური ფუნქცია აქვს, რომელიც საშუალებას აძლევს მკაფიო და ფუნქციონალური კოდირების სტილი.
# მეხსიერების ეკონომია: რადგან tuple-ები immutable არიან, ისინი უფრო ნაკლებ მეხსიერებას მოითხოვენ, ვიდრე list-ები, რაც მათ უფრო ეფექტურს ხდის კონკრეტულ შემთხვევებში.

# set 

# უნიკალურობა: set შექმნილია უნიკალური ელემენტების შენახვისთვის. ეს იდეალური გადაწყვეტილებაა, როდესაც გჭირდებათ მხოლოდ უნიკალური მონაცემები (მაგალითად, ჩაწერილი ადამიანების ჩამონათვალი, სადაც განმეორებები არ უნდა იყოს).
# სწრაფი ძიება: set-ის მონაცემთა სტრუქტურა საშუალებას აძლევს სწრაფად და ეფექტურად მოიძიოთ ელემენტები, რაც ამ ტიპის კიდევ ერთ მნიშვნელოვან უპირატესობას წარმოადგენს.
# მათემატიკური ოპერაციები: set-ები საშუალებას გაწვდოს მათემატიკური ოპერაციების (მაგალითად, გაწვდვა, გაწვდვა და სხვ.) განხორციელება, რაც მონაცემთა ანალიზისთვის სასარგებლოა.