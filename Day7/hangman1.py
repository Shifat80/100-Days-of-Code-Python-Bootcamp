import random
word_list=["mouse","keyboard","monitor","printer","laptop"]

chosen_word=random.choice(word_list)

length=len(chosen_word)

end_of_game=False

while not end_of_game:
    guess_letter=input("guess a letter\n").lower()

    live=6
    
    size=len(chosen_word)

    display=[] 

    for _ in range(size):
        display+="_"
    print(display)        

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess_letter:
            display[position]=guess_letter
    if guess_letter not in chosen_word:
        live-=1
        if live==0:
            end_of_game=True
            print("you lose")
    print(display)
    if "_" not in display:  
        end_of_game=True
        print("you won")  
        