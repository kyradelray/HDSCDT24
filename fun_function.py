def is_coffee_strong(sleep_hours):
    if sleep_hours >= 7:
        return "You're good! Coffee's just a bonus today"
    elif 4 <= sleep_hours < 7:
        return "You definitely need that coffee. Proceed with caution..."
    else:
        return "Forget coffee, you need to go home and get some sleep"

# Test it!
print(is_coffee_strong(8))
print(is_coffee_strong(5))
print(is_coffee_strong(3))
