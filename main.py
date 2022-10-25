from replit import clear
from art import logo
import random 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """ Returns a random card from the deck of cards."""
    return random.choice(cards)

def score_cal(cards_list):
    """ Takes in list of cards and returns the sum of cards
    inside it."""
    if sum(cards_list) == 21 and len(cards_list) == 2:  
        #this would be termed as blackjack 
        return 0
    if 11 in cards_list and sum(cards_list) > 21:
        #this is done to as part of the game rules where in 
        # if the player gets a ace it should be either considered 11 or 1
        # the value would depend on whether the total of cards if chosen as 11 would go over 21
        #if goining over 21 then replace it with 1
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)
    
def compare(players_score,computer_score):
    if players_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
        
    if players_score == computer_score:
        return "Draw 🙃"
    elif players_score == 0:
        return "Win with a Blackjack 😎"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif players_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif players_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
def play_game():
    print(logo)
    player_cards = []
    computer_cards = []
    game_over = False
    for i in range (2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        players_score = score_cal(player_cards)
        computer_score = score_cal(computer_cards)
        
        print(f"   Your cards are {player_cards}, your score is {score_cal(player_cards)} ")
        print(f"   Computers first card is {computer_cards[0]}")
    
        if (players_score == 0 or computer_score == 0 or players_score > 21):
            game_over = True
        else:
            want_card = input("Type 'y' to get another card, type 'n' to pass :")
            if want_card == "y":
                player_cards.append(deal_card())                
            else:
                game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = score_cal(computer_cards)

    print(f"   Your final hand: {player_cards}, final score: {players_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(players_score,computer_score))
    
while input("Do you want to play the game of blackjack?:") == 'y':
    clear()
    play_game()
