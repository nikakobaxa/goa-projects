# MAP

list1 = [2, 4, 6, 8, 10]
res = list(map(lambda x: x * 2, list1))
print(res)

list2 = ["Alice", "Bob", "Charlie"]
res = list(map(lambda name: "hello, "  + " " + name, list2))
print(res)

list3 = ["apple", "banana", "kiwi"]
res = list(map(lambda word: len(word), list3))
print(res)

# Filter

list4 = [-5, 3, -2, 7, 0, 10]
res = list(filter(lambda num: num > 0, list4))
print(res)

list5 = ["pear", "apple", "peach", "grape"]
res = list(filter(lambda str: str.startswith("p"), list5))
print(res)

list6 = [10, 55, 42, 78, 65, 20]
res = list(filter(lambda x: x > 50, list6))
print(res)


# map-ის მთავარი მიზანი არის კოლექციის ყველა ელემენტის ტრანსფორმაცია (შეცვლა). map ატარებს ოპერაციას თითოეულ ელემენტზე და აბრუნებს ახალ კოლექციას, რომელშიც თითოეული ელემენტი გადამუშავებულია.
# filter-ი გამოიყენება კოლექციიდან მხოლოდ იმ ელემენტების შერჩევისთვის, რომლებიც აკმაყოფილებენ გარკვეულ პირობას. ეს ფუნქცია არ ცვლის ელემენტებს, არამედ მხოლოდ ფილტრავს (არჩევს) მათ, რომლებიც მოცემულ პირობას სვამენ.