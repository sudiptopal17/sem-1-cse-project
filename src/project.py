

print("                                                              \033[1;31mWELCOME TO ROCK PAPER SCISSORS!\033[0m")
   


print("                                                             ================================")
print("                                                                Rock, Paper, Scissors Game")
print("                                                             ================================")




answer = input("Do you want to play the game? (yes/no): ").lower()
if answer != "yes":
    print("Thanks for visiting, Goodbye!")
    exit()
    




import random
choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while user_score < 3 and computer_score < 3:



  user_choice = input("Enter your move = rock, paper, scissors=  ").lower()
  comp_choice = random.choice(choices)



  print(f"Computer choosed: {comp_choice}")
  print(f"User choosed: {user_choice}")

  if user_choice == comp_choice:
    print("It's a tie! = both choosed the same")



  elif user_choice == "rock":
    if comp_choice == "paper":
        print("Paper covers Rock = computer wins")
        computer_score += 1
    else:
        print("Rock wins! = you win")
        user_score += 1

  elif user_choice == "paper":
    if comp_choice == "scissors":
        print("Scissors cuts Paper = computer wins")
        computer_score += 1
    else:
        print("Paper wins! = you win")
        user_score += 1

  elif user_choice == "scissors":
    if comp_choice == "rock":
        print("Rock crushes Scissors = computer wins")
        computer_score += 1
    else:
        print("Scissors wins! = you win")
        user_score += 1

  print(f"User Score: {user_score}")

  print(f"Computer Score: {computer_score}")


if user_score == 3:
 print("You won the game!")
else:
 print("Computer won the game!")


print(                                                        "Thanks for playing, Goodbye!")


