# import the ramdom function!!
import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response it the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user doesn't enter something that's valid
        print(error)
        print()


def instructions():
    """PRINTS INSTRUCTIONS"""

    print('''
**** Instructions ****

To begin, chose the number of rounds (♾️or press <enter> for 
infinite mode♾️)

Then play against the computer. You need to choose R (rock),
P (paper) or S (scissors).

The rules are as follows:
📀 Paper beats rock
💿 Rock beats scissors 
💽 Scissors beats paper
💾 HAVE FUN!!!!

Press <xxx> to end the game at anytime🔚

Good Luck!!!!
    ''')


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


# compare user / computer choice and returns
# results (win / lose / tie)
def rps_compare(user, comp):

    # if the user and the computer choice is the same, it's a tie!
    if user == comp:
        round_result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"
    #if it's not a win / tie, then it's a loss
    else:
        round_result = "lose"

    return round_result



# Main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("💎🧻✂️ Rock / Paper / Scissors Game ✂️🧻💎")
print()

# Instructions
want_instructions = string_checker("do you want to read the instruction ").lower()

#display the instructions
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode:  ")


if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


# Game loop starts here
while rounds_played < num_rounds:
    # display heading!
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️Round {rounds_played + 1} (Infinite Mode)♾️♾️♾️"

    else:
        rounds_heading = f"\n📀💿📀 Rounds {rounds_played + 1} of {num_rounds}💿📀💿"
    print(rounds_heading)
    print()

    # randomly choose from the rps list (excluding the exit code!!)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # gives a list of the choice's the user can choose!
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # print a statement if that user selected "infinite mode and didn't play any rounds!!!"
    # if user_choice == "xxx" and rounds_played == 0 and mode == "infinite":
    #     print("🐔🐤🐥🐔 Oops! You chickens out and didn’t play any rounds 🐔🐤🐥🐔")

    # if the user types "xxx" the program will stop
    if user_choice == "xxx":
        break


    result = rps_compare(user_choice, comp_choice)

    # depending on how if the user won / tied / lose it will give feedback!
    if result == "tie":
        rounds_tied += 1
        feedback = "💩💩💩 Why did you pick the exact same thing as the GOD DAM ROBOT! 💩💩💩"

    elif result == "lose":
        rounds_lost += 1
        feedback = "💩💩💩 You lost to a ROBOT! 💩💩💩"

    else:
        feedback = "😀😀😀 Yay you DID NOT lose to the god dam COMPUTER! 😀😀😀"

    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round:  {rounds_played + 1}  -  {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1


    if mode == "infinite":
        num_rounds += 1


# Game loop ends here
if rounds_played > 0:
    # Game History / statistics area
    # statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"😀 Won: {percent_won:.2f}  \t"
          f"💩 Lost: {percent_lost:.2f}  \t"
          f"💩 Tied: {percent_tied:.2f}")


    # game history
    game_history_show = string_checker("Do you want to see your game history?  ")

    if game_history_show.lower() == "yes" or game_history_show.lower() == "y":
        print("🎮🎮🎮 Game History 🎮🎮🎮")

        for item in game_history:
            print(item)

        print()
        print("Thanks for playing")

else:
    print("🐔🐤🐥🐔 Oops! You chickens out and didn’t play any rounds🐔🐤🐥🐔 ")