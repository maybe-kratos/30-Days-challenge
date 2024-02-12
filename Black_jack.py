import random

def draw_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card  = random.choice(cards)
    return card

def calculate_score(cardss):
    
    if sum(cardss) == 21 and len(cardss) == 2:
        return 0
    
    if 11 in cardss and sum(cardss) > 21:
        cardss.remove(11)
        cardss.append(1)
    return sum(cardss)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21 :
        return "You went over, You loose."
    
    if user_score == computer_score:
        return "Its a Draw."
    elif computer_score == 0:
        return "Opponent has Blackjack, You loose."
    elif user_score == 0:
        return "You have Blackjack, You win."
    elif user_score > 21:
        return "You went over, You loose."
    elif computer_score > 21:
        return "Opponent went over, You win."
    elif user_score > computer_score:
        return "You win."
    elif computer_score > user_score:
        return "You loose."
    else:
        return "Thanks for finding a bug."

def play_game():
    user_cards = []
    computer_cards = []
    game = True

    for m in range(0,2):
        user_cards.append(draw_cards())
        computer_cards.append(draw_cards())
    
    while game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your Cards: {user_cards}, current score: {user_score}.")
        print(f"    Computer's First card: {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21 :
            game = False
        else :
            user_should_deal = (str(input("Type 'y' to get another card, 'n' to pass :")).lower())
            if user_should_deal == 'y':
                user_cards.append(draw_cards())
                
            else :
                game = False
                print("Well that was short.")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_cards())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()

print("Well that was short 🙈.")