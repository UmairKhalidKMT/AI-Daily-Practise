#  KAUN BANEGA CROREPATI (KBC)

# List of questions formatted as:
# [ Question Text, Option 1, Option 2, Option 3, Option 4, Correct Option Number (1-4) ]
questions = [
    [
        "Which language was used to create Python?",
        "C", "Java", "C++", "JavaScript", 1
    ],
    [
        "What keyword is used to define a function in Python?",
        "func", "define", "def", "function", 3
    ],
    [
        "Which data type in Python is IMMUTABLE?",
        "List", "Dictionary", "Set", "Tuple", 4
    ],
    [
        "What is the output of len(('apple',))?",
        "0", "1", "5", "Error", 2
    ]
]

# Cash prize amounts corresponding to each question
levels = [1000, 2000, 5000, 10000]
take_home_money = 0

print(" WELCOME TO KAUN BANEGA CROREPATI (KBC)! ")

for i in range(len(questions)):
    q = questions[i]
    print(f"Question for Rs. {levels[i]}:")
    print(f"{q[0]}")
    print(f"1. {q[1]}          2. {q[2]}")
    print(f"3. {q[3]}          4. {q[4]}")
    
    # User input
    user_reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    
    # Check if user wants to quit
    if user_reply == 0:
        print("\nYou opted to quit the game.")
        break
        
    # Check correct answer
    if user_reply == q[5]:
        print(f"Correct Answer! You won Rs. {levels[i]}\n")
        take_home_money = levels[i]
    else:
        print("\nWrong Answer! Game Over.")
        break

print(f" Total Money Taken Home: Rs. {take_home_money} ")
