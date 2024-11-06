# Python-ში ობიექტი არის მონაცემთა სტრუქტურა, რომელიც აერთიანებს მონაცემებს (ატრიბუტები) და მათთან დაკავშირებულ ფუნქციონალობას (მეთოდები). ობიექტები წარმოადგენენ კლასების ინსტანცებს. ყოველ ობიექტს აქვს საკუთარი მდგომარეობა და ქცევა, რაც მას საშუალებას აძლევს, იმოქმედოს სხვადასხვა სიტუაციებში.

# Python-ის dictionary (ანუ "დიქტიონერი") არის მონაცემთა სტრუქტურა, რომელიც შეიცავს მონაცემების წყვილებს: გასაღებს (key) და მნიშვნელობებს (value). ეს სტრუქტურა ძალიან ძლიერი და მოქნილია, და აქვს რამდენიმე მნიშვნელოვანი გამოყენება:

# 1.მონაცემების შენახვა
# 2.მონაცემების სწრაფი მოძიება
# 3.არასასეზონური მონაცემების ქონა
# 4.განსხვავებული ტიპების შენახვა
# 5.ინფორმაციის შეკრება

mouse = {
    "brand": "Logitech",
    "type": "Wireless",
    "dpi": 16000,
    "color": "Black",
    "battery_life": "24 months"
}

computer = {
    "brand": "Dell",
    "processor": "Intel i7",
    "ram": "16GB",
    "storage": "512GB SSD",
    "os": "Windows 10"
}

keyboard = {
    "color": "white",
    "brand": "Corsair",
    "type": "Mechanical",
    "backlit": True,
    "key_switch": "Cherry MX",
    "warranty": "2 years"
}

print(mouse.keys())
print(mouse.values())
print(mouse.items())

print(computer.values())
print(computer.keys())
print(computer.items())

print(keyboard.items())
print(keyboard.keys())
print(keyboard.values())

