import random

print(
    "Welcome to Snake Water Gun game\n"
    "Chicess:\n"
    "s for Snake\n"
    "w for Water\n"
    "g for Gun\n"
    "q to Quit"
)

comps_score = 0
user_score = 0

while user_score < 3 and comps_score < 3:

    winTable = [["D", "W", "L"], ["L", "D", "W"], ["W", "L", "D"]]
    s = 0
    w = 1
    g = 2
    choice_map = {"S": s, "W": w, "G": g}
    result_text = {"W": "You Win!", "L": "You Lose!", "D": "Game Drawn!"}

    comps_choice = random.randint(0, 2)
    user_choice = input("Enter your choice: ").upper()
    if user_choice == "Q":
        print("You quit the game!")
        break
    if user_choice not in choice_map:
        print("Invalid choice! Please enter S, W, or G.")
        continue

    player_index = choice_map[user_choice]
    res = winTable[player_index][comps_choice]

    print(result_text[res])

    if res == "W":
        user_score += 1
        if comps_score > 0:
            comps_score -= 1
    elif res == "L":
        if user_score > 0:
            user_score -= 1
        comps_score += 1

    print(f"Your score: {user_score}\nComputers score: {comps_score}")


if user_score == 3:
    print(f"congrts! you win\nyour score {user_score} computers score {comps_score}")
elif comps_score == 3:
    print(
        f"sorry! computer wins\nyour score {user_score} computers score {comps_score}"
    )
