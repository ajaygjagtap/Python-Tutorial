Questions = ("Who is the current railway minister of india?", 
"Which god is also known as 'Gauri Nandan'?", 
"Which city is known as Pink city of india?", 
"Who wrote India's National Anthem?", 
"Where is India Gate Located?")

Options = (("A. Ashwini Vaishnav", "B. Piyush Goyal"), 
("A. Ganesha", "B. Katikeya"), 
("A. Jaipur", "B. Rajasthan"), 
("A. Rabindranath Tagore", "B. Dr. B. R. Ambedkar"), 
("A. New Delhi", "B. Mumbai"))

Answers = ("A", "A", "A", "A", "A")

Guesses = []

Question_No = 0

for Question in Questions:
    print("------------------------------------------------------------")
    print(Question)

    for Option in Options[Question_No]:
        print(Option)

    Guess = input("Enter your option:").capitalize()
    Guesses.append(Guess)
    if Guess == Answers[Question_No]:
        print("Your Option is CORRECT!")
    else:
        print("Your Option is INCORRECT!")
        print(f"{Answers[Question_No]} is the Correct Option.")
    Question_No += 1
