
def int_check(question):
    """Checks users enter an integer more than 1"""

    while True:
        error = "Please enter and integer more then 1 or more."

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0



print("💎🧻✂️ Rock / Paper / Scissors Game ✂️🧻💎")
print()

# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode:  ")


if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
    print("♾️INFINITY♾️")

# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Chose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("Rounds played", rounds_played)

    if mode == "infinite":
        num_rounds += 1

    print("num rounds:  ", num_rounds)
# Game loop ends here

# Game History / statistics area
