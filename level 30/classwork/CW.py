NameError
# Raised when a variable is not found in the local or global scope.
TypeError
# Raised when a function or operation is applied to an object of an incorrect type.
IndexError
# Raised when the index of a sequence is out of range.
SyntaxError
# Raised by the parser when a syntax error is encountered.
ValueError
# Raised when a function gets an argument of correct type but improper value.
IndentationError
# Raised when there is an incorrect indentation.

try:
    print(my_variable)  
except NameError:
    print("ჩამოვარდა შეცდომა:")
    my_variable = "Hello, world!" 
    print("საწყისი ცვლადი განსაზღვრულია:")


mt_list = [1, 2, 3]

try:
    print(my_list[5])
except:
    print("არ არის 5 სიაში")


try:
    value = int("abc")
except:
    print("მინიჭებული მნიშვნელობა")


# try/except-ის გამოყენება ძალიან სასარგებლოა მაშინ, როდესაც გვსურს შეცდომების დამუშავება ჩვენი კოდის მრუდე ნაწილში. ეს ხელს გვიწყობს პროგრამის სტაბილურობას და გამართულ მუშაობას, როდესაც რაიმე პრობლემა წარმოიქმნება. ახლა განვიხილოთ try/except-ის გამოყენების კოდი და რა სასარგებლოა ეს: