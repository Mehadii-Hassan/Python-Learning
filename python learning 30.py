questions = (
    "What is the capital of Bangladesh?",
    "What is the national flower of Bangladesh?",
    "What is the currency of Bangladesh?",
    "What is the name of the longest river in Bangladesh?",
    "Who is the current Prime Minister of Bangladesh?",
    "What is the national fruit of Bangladesh?",
    "Which day is celebrated as Victory Day in Bangladesh?",
    "Which language do people speak in Bangladesh?",
    "What is the name of the national anthem of Bangladesh?",
    "What color is the circle in the flag of Bangladesh?"
)

options = (
    ("A. Dhaka", "B. Chittagong", "C. Khulna", "D. Sylhet"),
    ("A. Rose", "B. Water Lily", "C. Sunflower", "D. Marigold"),
    ("A. Taka", "B. Rupee", "C. Dollar", "D. Pound"),
    ("A. Padma", "B. Jamuna", "C. Meghna", "D. Buriganga"),
    ("A. Sheikh Hasina", "B. Khaleda Zia", "C. Abdul Hamid", "D. Ershad"),
    ("A. Apple", "B. Banana", "C. Jackfruit", "D. Mango"),
    ("A. 21 February", "B. 26 March", "C. 16 December", "D. 1 May"),
    ("A. Hindi", "B. Bengali", "C. Urdu", "D. English"),
    ("A. Amar Desh", "B. Amar Shonar Bangla", "C. Amar Janmobhumi", "D. Desher Gaan"),
    ("A. Blue", "B. Green", "C. Yellow", "D. Red")
)

answers = (
    "A",
    "B",
    "A",
    "A",
    "A",
    "C",
    "C",
    "B",
    "B",
    "D"
)
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")