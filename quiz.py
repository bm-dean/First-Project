#First Quiz
questions = ("How many Premier League titles do Manchester United have?: ", 
             "Who is Manchester United's top goal scorer of all time?: ", 
             "Who has the most appearances for Manchester United?: ", 
             "Who is Manchester United's current manager?: ", 
             "What is Manchester United's stadium called?: ") 

options = (("A. 13","B. 12","C. 14","D. 11"),
           ("A. Marcus Rashford", "B. Cristiano Ronaldo", "C. Bobby Charlton", "D. Wayne Rooney"),
           ("A. Bobby Charlton", "B. Paul Scholes", "C. Ryan Giggs", "D. Roy Keane"),
           ("A. Erik Ten Hag", "B. Ole Gunnar Solskjær", "C. Jose Mourinho", "D. Pep Guardiola"),
           ("A. Emirates Stadium", "B. Old Trafford", "C. Etihad Stadium", "D. Stamford Bridge"))

answers = ("A", "D", "C", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
     print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
       score += 1
       print("You are correct!")
    else:
       print("You are incorrect!")
       print(f"{answers[question_num]} is the correct answer")
    question_num += 1 

print("         Results           ")
print("--------------------------")
print("answers: ", end="")
for answer in answers:
   print(answer, end="")
print()

print("guesses: ", end="") 
for guess in guesses:
   print(guess, end=" ")
print()

score= int(score / len(questions) * 100)
print(f"Your score is: {score}%")