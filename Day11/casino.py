import random

def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(cards)
    return card

def calculate_score(cards):   
    if sum(cards)==21 and len(cards)==2: 
        return 0 
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)



def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw 🙃"
    elif computer_score==0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score==0:
        return "Win with a Blackjack 😎"
    elif user_score>21:
        return "You went over. You lose 😭"
    elif computer_score>21:
        return "Opponent went over. You win 😁"
    elif user_score>computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"




user=[]
computer=[]
is_game_over=False
for _ in range(2):
    user.append(deal_cards())
    computer.append(deal_cards())
    
 
 
while not is_game_over:      
    user_score=calculate_score(user)
    computer_score=calculate_score(computer)
    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {computer[0]}")



    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_declare=input("Type 'y' to get another card, type 'n' to pass: ")
    if user_should_declare=="y":
        user.append(deal_cards())
    else:
        is_game_over=True

while computer_score!=0 and computer_score<17:
    computer.append(deal_cards())
    computer_score=calculate_score(computer)


print(compare(user_score,computer_score))
