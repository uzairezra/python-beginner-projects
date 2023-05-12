import random

def play():
    user = input("What's your choice? 'r' for Rock, 'p' for Paper or 's' for Scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    # r>s, s>p, p>r
    if is_win(user, computer):
        return 'You Won!'
    return 'You Lost!'

def is_win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

print(play())