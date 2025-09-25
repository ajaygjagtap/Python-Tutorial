# Calculating length of string using len() function.
Names = "Ajju, Rushi"
print(len(Names))

fruit = "Banana"
print("The length of word Banana is", len(fruit))
for character in fruit:
    print(character)

name = "!!!!!Ajju!!!!!"
# For Uppercase upper() method used.
print(name.upper())

# For Lowercase lower() method used.
print(name.lower())

# Removing trailing character in right side of the string is done by rstrip() method.
print(name.rstrip("!"))

# Removing trailing character in left side of the string is done by lstrip() method.
print(name.lstrip("!"))

# Removing trailing character from bothe side of the string is done by strip() method.
print(name.strip("!"))

# Replace a string with another we can use replace() method.
print(name.replace("Ajju", "Rushi"))

# split() method is used to convert a string into a list.
print(name.split()) 

# capitalize() method only turns the first character of the string to uppercase and rest other turns into lowercase.
blog_heading = "introduction tO PythoN"
print(blog_heading.capitalize())

# center() method aligns the string to the center as per parameter given by user.
print(name.center(50))

# count() method returns the number of times the given value has occured within a string
c = "Rushi, Aniket, Ajju, Avi, Apurv, Shubham"
print(c.count("A"))

# endswith() method checks if the string ends with given value. If yes then returns True else returns False.
stmt = "Welcome to the Console."
print(stmt.endswith("."))

# find() method search for the first occurence of given value and return the index of it. If given value is absent thrn it returns -1.
print(stmt.find("t"))
print(stmt.find("a"))

# isalnum() method returns the True only if entire string only consist of A-Z, a-z, 0-9. If any other presents there then it returns False.
stmt = "WelcometotheConsole1"
print(stmt.isalnum())

# isalpha() method returns the True only if entire string only consist of A-Z, a-z. If any other presents there then it returns False.
stmt = "WelcometotheConsole"
print(stmt.isalpha())

# islower() method returns the True only if characters of the entire string is in lowercase otherwise it returns False.
stmt = "welcome to the console."
print(stmt.islower())

# isupper() method returns the True only if characters of the entire string is in uppercase otherwise it returns False.
stmt = "WELCOME TO THE CONSOLE."
print(stmt.isupper())

# swapcase() method used to convert uppercase to lowercase and lowercase to uppercase.
a = "ajju"
r = "RUSHI"
print(a.swapcase(), r.swapcase())