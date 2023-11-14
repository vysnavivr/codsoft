import random

def play_game():
    rock = '''

        _______
    ---'    ___)
           (____)
           (____)
           (___)
    ----'__(__)

    '''

    paper = '''
        ________
    ---'    _____)_____
               ________)
               ________)
              ________)
    ----'___________)

    '''

    scissor = '''
        _______
    ---'    ___)_____
               ______)
               ________)
           (_____)
    ----'__(____)

    '''
    game_images = [rock, paper, scissor]
    user_choice = int(input("Enter your choice:\n0 for ROCK,\n1 for PAPER,\n2 for SCISSORS\nYou Choose:"))
    if (user_choice > 2 or user_choice < 0):
        print("Input Invalid. YOU LOSE..!")
    else:
        print(game_images[user_choice])
        computer_choice = random.randint(0, 2)
        print("Computer choice:")
        print(game_images[computer_choice])

        if (computer_choice == user_choice):
            print(" IT'S TIE !")
        elif (user_choice == 2 and computer_choice == 0):
            print("YOU LOSE..!")
        elif (user_choice == 0 and computer_choice == 2):
            print("YOU WIN..!")
        elif (computer_choice > user_choice):
            print("YOU LOSE..!")
        elif (user_choice > computer_choice):
            print("YOU WIN..!")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no):").lower()

    if play_again != 'yes':
        print("\n\nThank you for playing....!")
        break


