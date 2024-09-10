str = "hello world"

x = str.upper()

print(x)

#upper() მეთოდი აბრუნებს სტრიქონს, სადაც ყველა სიმბოლო არის დიდი ასოებით.

str0 = "HELLO WORLD"

i = str0.lower()

print(i)

#Low() მეთოდი აბრუნებს სტრიქონს, სადაც ყველა სიმბოლო არის პატარა.

str1 = "trent"

o = str1.capitalize()

print(o)

#capitalize() მეთოდი აბრუნებს სტრიქონს, სადაც პირველი სიმბოლო არის დიდი, ხოლო დანარჩენი - პატარა.

str2 = "HeLlo NiKa"

p = str2.swapcase()

print(p)

#swapcase() მეთოდი აბრუნებს სტრიქონს, სადაც ყველა დიდი ასო მცირეა და პირიქით.

str3 = "hello nika"

a = str3.find("nika")

print(a)

#find() მეთოდი პოულობს მითითებული მნიშვნელობის პირველ შემთხვევას.

mylist = ["nika", "luka"]
c = len(mylist)

print(c)

#The len() function returns the number of items in an object.


fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)

#The index() method returns the position at the first occurrence of the specified value.

mylist2 = ["nika"]

mylist2.append("luka")

print(mylist2)

#append() მეთოდი ამატებს ელემენტს სიის ბოლოს.


mylist3 = ["nika", "luka", "giorgi"]

mylist3.insert(2,"daviti")

print(mylist3)

#მეთოდი insert() აყენებს მითითებულ მნიშვნელობას მითითებულ პოზიციაზე.


mylist4 = ["nika", "luka", "giorgi"]

mylist4.pop(1)

print(mylist4)

#pop() მეთოდი აშორებს ელემენტს მითითებულ პოზიციაზე.

mylist5 = ["gio", "luka", "nika"]

mylist5.remove("nika")

print(mylist5)

#თუ არის ერთზე მეტი ელემენტი მითითებული მნიშვნელობით, remove() მეთოდი აშორებს პირველ მოვლენას: