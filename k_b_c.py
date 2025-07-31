questions = [
    "Who is the Prime Minister of India ?",
    "What is the national animal of india ?",
    "Where is the Capitol of India ?",
    "Who is the Richest Bussinessman in the world ?",
    "Who is the president of U.S.A ?",
]
answers = ["narendra modi", "tiger", "new delhi", "elon musk", "donald trump"]

price = 0
for q in questions:
    randomQues = q
    print(randomQues)
    userAns = str(input("answer: ").lower().strip())
    if userAns not in answers:
        print("wrong answer")
        price -= 10
    else:
        if questions.index(randomQues) == answers.index(userAns):
            print("currect")
            price += 10
        else:
            print("wrong answer")
            price -= 10

print("you won! ", price)
