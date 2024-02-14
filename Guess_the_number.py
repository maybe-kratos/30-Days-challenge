import random


while input("Type 'y' to PLAY :").lower() == 'y':
    
    lives  = 0
    game = True
    
    game_mode = input("Choose a game mode, 'easy' or 'hard' :").lower()
    if game_mode == "hard":
        lives = 5
    elif game_mode == "easy":
        lives = 10
    else :
        print("Play again...🙃")
        break

    selected_number = random.randint(1,100)

    while game == True:
        
        guessed_number = int(input("Guess a number :"))
        if guessed_number == selected_number:
            print("You win, you guessed it right.")
            break
        elif guessed_number > selected_number:
            print("Try guessing less...")
            lives = lives - 1
        else:
            print("Try guessing more...")
            lives = lives -1 
        print(lives," Chances left.")

        if lives == 0:
            print("Lives are over, you loose")
            break
        
    break
