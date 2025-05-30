def format_duration(seconds):
    if seconds == 0:
        return "now"
    # თუ seconds არის 0 ტოლი მაშინ აბრუნებს now ანუ დრო არ არის გასული

    units = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1),
    ]
    
    # ქნის სიას რომელიც შეიცავს დროში გამოყენებულ ერთეულებს და შესაბამის წამებში მნიშვნელობებს
    
    time_parts = []
    # ცარიელი სია სადაც შევინახავთ დროის თითოეულ ერთეულის მნიშვნელობას
    
    for name, unit_seconds in units:
        #  ვმუშაობთ ყველა დროის ერთეულზე 
        value, seconds = divmod(seconds, unit_seconds)
        # ეს გამოთვლის რამდენჯერ ჩაეტევა მოცემული ერთეული და რამდენი წამი დარჩება შემდეგი ერთეულისთვის
        if value:
            # თუ value იქნეაბა 0ს ტოლი მაშინ უნდა ჩაემატოს შედეგში
            time_parts.append(f"{value} {name}{'s' if value > 1 else ''}")
            # ამ სტრიქონში ხდება შემდეგი სინგულარის ან პლურალის არჩევა

    return ', '.join(time_parts[:-1]) + ' and ' + time_parts[-1] if len(time_parts) > 1 else time_parts[0]
    # თუ სიაში იქნება მხოლოდ ერთი ელემენტი დააბრუნებს მაგ სტრინგს
    # ხოლო თუ ერთზე მეტი ყველა ელემენტი შეერთდება მძიმით გარდა ბოლო ელემენტისა
    # ბოლოს ემატება და + ბოლო ემენტი