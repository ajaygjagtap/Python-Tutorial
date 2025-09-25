num = int(input("Enter the number between 5-9: "))

if (num < 5 or num > 9):
    raise ValueError("Value should be between 5-9")
