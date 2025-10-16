import random
choices=["rock","paper","scissors"]
user=0
comp=0
tie=0
print("Welcome player to 🪨Rock 📃Paper ✂️Scissors GAME")
round=int(input("Number of rounds you want to play(3 or 5):"))
w_round=round//2+1
rounds_played=0
while rounds_played<round:
    comp_guess=random.choice(choices)
    user_guess=input("Enter your choice rock,paper,scissors (or) q for quit.").lower()
    if user_guess=='q':
        print("Thank you for playing.")
        break
    
    if user_guess not in choices:
        print("Invalid Input try again!\n")
        continue
    print(f"Computer chose: {comp_guess}")

    if user_guess==comp_guess:
        print("It's a tie!")
        tie+=1

    elif (user_guess == "rock" and comp_guess == "scissors") or \
         (user_guess == "paper" and comp_guess == "rock") or \
         (user_guess == "scissors" and comp_guess == "paper"):
        print("You win! 🎉")
        user+=1

    else:
        print("You lose! 😢")
        comp+=1
    
    rounds_played+=1

    print(f"Score Board:\nUser:{user}\tComputer:{comp}\tTie:{tie}")
    if user>=w_round:
        print("Game over!!!")
        print("You have WON! against the Computer🤖")
        break
    elif comp>=w_round:
        print("Game over!!!")
        print("You have lost against the Computer🤖 has won.\n Better luck next time.")
        break
