##This is a console-based Python Quiz Game with a time limit and random question order.
Each question must be answered within 5 seconds.
The game uses Python modules like random and time along with lists and conditional statements.
This project helped me practice logic building, loops, and time-based conditions.##

import random
import time

print("WELCOME TO PYTHON QUIZ GAME")
print("----------------------------------")
question=[
    "1. What is the capital of India?",
    "2. Which language is used for web development?",
    "3. What is the output of 2 + 3 * 2?",
    "4. Which keyword is used to define a function in Python?",
    "5. What data type is used to store multiple values?"
    ]
options=[
    ["A. Chennai", "B. Delhi", "C. Mumbai", "D. Kolkata"],
    ["A. Python", "B. HTML", "C. Java", "D. C"],
    ["A. 10", "B. 7", "C. 8", "D. 6"],
    ["A. function", "B. define", "C. def", "D. fun"],
    ["A. int", "B. float", "C. list", "D. string"]
]
answers=["B", "B", "B", "C", "C"]
random.shuffle(question)
score=0

for i in range(len(question)):
    print("\n", question[i])
    for opt in options[i]:
        print(opt) 
    
    start_time=time.time()
    user_ans=input("Enter your answer(A/B/C/D): ").upper()
    end_time=time.time()

    if end_time-start_time>5:
        print("TIMES UP")
        print("THE CORRECT ANSWER IS", answers[i])

    if user_ans==answers[i]:
        print("correct")
        score +=1
    else:
        print("You entered wrong answer")

print("Your quiz is Completed")
print("Your score is:", score ,"out of", len(question))
