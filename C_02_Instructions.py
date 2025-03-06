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


#main routine
print()
print("💎🧻✂️ Rock / Paper / Scissors game ✂️🧻💎")
#testing loop
want_instructions = string_checker("do you want to read the instruction ").lower()

#display the instructions
if want_instructions == "yes":
    instructions()

print()
print("program continues ")