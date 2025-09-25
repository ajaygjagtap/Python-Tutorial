try:
    num = int(input("Eneter the integer: "))
    a = [6, 3]
    print(a[num])

except ValueError:
    print("Entered input is not an integer")

except IndexError:
    print("Index error occured")
