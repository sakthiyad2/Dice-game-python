import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("🎲 Welcome to Dice Game (Player vs Computer)\n")
    
    while True:
        user_input = input("Press Enter to roll dice (or type 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Game exited. Thank you for playing!")
            break

        player_roll = roll_dice()
        print("You rolled:", player_roll)

        computer_roll = roll_dice()
        print("Computer rolled:", computer_roll)

        if player_roll > computer_roll:
            print("🎉 You Win!\n")
        elif player_roll < computer_roll:
            print("💻 Computer Wins!\n")
        else:
            print("🤝 It's a Draw!\n")


play_game()