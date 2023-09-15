import random

# Initialize deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Functions
def deal_card():
    suit = random.choice(suits)
    rank = random.choice(ranks)
    return (rank, suit)

def calculate_hand_value(hand):
    value = sum([values[card[0]] for card in hand])
    num_aces = sum([1 for card in hand if card[0] == 'Ace'])
    
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    
    return value

# Game setup
player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]

# Game loop
while True:
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    print("\nYour hand:", player_hand, "Value:", player_value)
    print("Dealer's hand:", [dealer_hand[0], 'Hidden'])
    
    if player_value == 21:
        print("Blackjack! You win!")
        break
    elif player_value > 21:
        print("Bust! You lose.")
        break
    
    action = input("Do you want to 'hit' or 'stand'? ").lower()
    
    if action == 'hit':
        player_hand.append(deal_card())
    elif action == 'stand':
        while dealer_value < 17:
            dealer_hand.append(deal_card())
            dealer_value = calculate_hand_value(dealer_hand)
        
        print("Dealer's hand:", dealer_hand, "Value:", dealer_value)
        
        if dealer_value > 21 or player_value > dealer_value:
            print("You win!")
        elif dealer_value > player_value:
            print("Dealer wins.")
        else:
            print("It's a tie!")
        
        break