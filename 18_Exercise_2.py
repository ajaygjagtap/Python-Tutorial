''' Que - Create a program capable of displaying questions to the user like KBC.
    Use List data type to store the questions and their correct answer.
    Display the final amount the person is taking home after playing the game.'''

# Solution -
print("Welcome to KBC")
print("Total Prize pool is Rs.51000")
print("Que.1 - Rs.1000")
print("Que.2 - Rs.5000")
print("Que.3 - Rs.10000")
print("Que.4 - Rs.15000")
print("Que.5 - Rs.20000")

list1 = ["Who is the current railway minister of india?", "Which god is also known as 'Gauri Nandan'?", 
"Which city is known as Pink city of india?", "Who wrote India's National Anthem?", "Where is India Gate Located?"]

list2 = ["Ashwini Vaishnav", "Ganesha", "Jaipur", "Rabindranath Tagore", "New Delhi"]



print(list1[0])
Answer_1 = str(input("Enter Your Answer: ")).capitalize()

if (Answer_1 == "Ashwini Vaishnav"):
    print("Answer is Correct and You won Rs.1000")
else:
    print("Your Answer is incorrect")

print("Try Next")


print(list1[1])
Answer_2 = str(input("Enter Your Answer: "))

if (Answer_2 == "Ganesha"):
    print("Answer is Correct and You won Rs.5000")
else:
    print("Your Answer is incorrect")

print("Try Next")


print(list1[2])
Answer_3 = str(input("Enter Your Answer: "))

if (Answer_3 == "Jaipur"):
    print("Answer is Correct and You won Rs.10000")
else:
    print("Your Answer is incorrect")

print("Try Next")


print(list1[3])
Answer_4 = str(input("Enter Your Answer: "))

if (Answer_4 == "Rabindranath Tagore"):
    print("Answer is Correct and You won Rs.15000")
else:
    print("Your Answer is incorrect")

print("Try Next")


print(list1[4])
Answer_5 = str(input("Enter Your Answer: "))

if (Answer_5 == "New Delhi"):
    print("Answer is Correct and You won Rs.20000")
else:
    print("Your Answer is incorrect")
