# make a 2-player Rock Paper Scissors game 
# ask each player for an input
# compare them, based on the rules
# print out a message congratulating the winner
# ask if they want to play again

valid_plays = {'1': 'rock', '2': 'paper', '3': 'scissors'}

def choose_play(player):
    """Ask each player to select the hand symbol they want to play"""

    while True:

        print "{}: choose a hand symbol to play:".format(player)
        print
        print "1 - rock"
        print "2 - paper"
        print "3 - scissors"

        player_choice = raw_input(">")
        print

        if player_choice not in valid_plays:
            print "Whoops, that's not a valid option!"
            print
        else:
            return player_choice


def find_winner(player_a_score, player_a_choice, player_b_score, player_b_choice):
    """Determine the winner and increment their score"""

    if player_a_choice == player_b_choice:
        print "You both chose {} - it's a tie!".format(valid_plays[player_a_choice])
    elif player_a_choice == '1':
        if player_b_choice == '2':
            print "Paper covers rock - Player B wins!"
            player_b_score += 1
        elif player_b_choice == '3':
            print "Rock smashes scissors - Player A wins!"
            player_a_score += 1
    elif player_a_choice == '2':
        if player_b_choice == '3':
            print "Scissors cut paper - Player B wins!"
            player_b_score += 1
        elif player_b_choice == '1':
            print "Paper covers rock - Player A wins!"
            player_a_score += 1
    elif player_a_choice == '3':
        if player_b_choice == '1':
            print "Rock smashes scissors - Player B wins!"
            player_b_score += 1
        elif player_b_choice == '2':
            print "Scissors cut paper - Player A wins!"
            player_a_score += 1
    
    print "Current score:"
    print "Player A - {}".format(player_a_score)
    print "Player B - {}".format(player_b_score)
    return player_a_score, player_b_score

def play_again():
    """Ask if they would like to play again, return True or False"""

    while True:

        print
        print "Would you like to play again? (y/n)"
        playing_again = raw_input(">")

        if playing_again[0].lower() == 'y':
            return True
        elif playing_again[0].lower() == 'n':
            "Okay, goodbye!"
            return False
        else:
            print "Sorry, that's not a valid response!"


def play_game():
    """Play rock paper scissors game"""

    playing = True
    player_a_score = 0
    player_b_score = 0

    while playing:
        player = "Player A"
        player_a_choice = choose_play(player)
        player = "Player B"
        player_b_choice = choose_play(player)
        player_a_score, player_b_score = find_winner(player_a_score, player_a_choice, player_b_score, player_b_choice)
        playing = play_again()

play_game()

    