"""
Create a simple game of “Rock, Paper, Scissors” where the computer
randomly generates value and asks the user to input their selection. The result
should show whether the user wins or loses, or if it is a draw.
"""
import random
score=0
print("##### ROCK, PAPER, SCISSORS! #####")
L1=['rock','paper','scissors']
a=random.choice(L1)
while True:
  
  print("\n[Please enter rock, paper or scissors. Type 'quit' to quit.]\nYour move: ")
  move=input()
  if move=="rock":
    print("The computer chose: " + a)
    if move==a:
      score+=0
      print("Draw!")
    elif move!=a:
      if a==L1[1]:
        print("The computer won!")
      elif a==L1[2]:
        score+=1
        print("You won!")
  elif move=="paper":
    print("The computer chose: " + a)
    if move==a:
      score+=0
      print("Draw!")
    elif move!=a:
      if a==L1[2]:
        print("The computer won!")
      elif a==L1[0]:
        score+=1
        print("You won!")
  elif move=="scissors":
    print("The computer chose: " + a)
    if move==a:
      score+=0
      print("Draw!")
    elif move!=a:
      if a==L1[0]:
        print("The computer won!")
      elif a==L1[1]:
        score+=1
        print("You won!")
  elif move=="quit":
    break
  else:
    print("Please type a valid move.")

print("Your score is: " + str(score))
print("THANKS FOR PLAYING!")
