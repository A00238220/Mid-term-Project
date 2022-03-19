##############################
#Mid-Term case study - ANA1001
#Sharon Bandele
##############################

#Importing time module
import time

#creating an empty list and health status
reward_bag = []
health1 = "100%"
health2 = "0%"

#Defining intro functions and randomized path functions:
#Introduction
def displayintro():
  name = input("\nplease input your username to begin: ")

  print(f"\nHello {name.title()}!, Welcome to Party Love game!")
  time.sleep(3)
  print()
  print("It is a long year of being single for you and you have been hoping for a change in your status quo")
  time.sleep(3)
  print("you finally get a chance that could lead you to love only if you make the right decisions")
  time.sleep(3)
  print("you arrive a party house that has rooms that can either lead to love or not")
  time.sleep(3)
  print("now you are at crossroads beacuse one path will lead you to love with rewards to ease your journey")
  time.sleep(3)
  print("and the other path will lead you through a fun-filled night with love not found at the end")
  time.sleep(3)
  print()

#Defining path to start mission
def choosepath():
  path = ""
  while path != "1" and path !="2":
    path = input("Which path will you choose? (1 or 2): ")
  return path

#mission
def checkpath(chosenpath):
  print()
  print("You enter the party house")
  time.sleep(2)
  print("The butler, Mr 47 shows you in and unlock the next party room door for you")
  time.sleep(3)  

  if chosenpath == "1":
    print()
    print("47: Room 4 unlocked!")
    time.sleep(2)
    print("47: Welcome to the party game room!")
    time.sleep(2)
    print("47: You just earned 50 party game tokens")
    time.sleep(2)

    reward_bag.append("50 party tokens")

    print(f"47: {reward_bag} have been added to your reward bag")
    time.sleep(2)
    print(f"47: Your health is still {health1}")
    time.sleep(2)
    print("47: You arrive a room full of archade games that require party tokens to play")

    usage1 = input("\nEnter 'yes' to use party token: ")
    while True:
      if usage1.lower().strip() == 'yes':
        print()
        print("47: Your coin have been activated for use")
        time.sleep(2)
        print("47: You play one game after another untill you lose track of time")
        time.sleep(2)
        print("47: The party ends and everybody has gone home")
        time.sleep(2)
        print(f"47: Your health is now {health2}")
        time.sleep(3)
        print()
        print("47: Love not found! You Lose!!")
        break
        time.sleep(2)
        print()
                              
    #play game again  
    while ("yes"):
      print()
      time.sleep(2)
      playagain1 = input("Do you want to play again? (Enter 'yes' to continue or 'quit' to end): ")
      if playagain1.lower().strip() == "yes":  
        displayintro()
        choice = choosepath()
        checkpath(choice)
      elif playagain1.lower().strip() == 'quit':
        break      

  elif chosenpath == "2":
    print()
    print("47: Room 3 unlocked!")
    time.sleep(2)
    print("47: Welcome to the curiosity/attraction room!")
    time.sleep(2)
    print("47: you have made a new friend named Saraphina and you have also earned $100 worth of date-cash")
    time.sleep(2)

    reward_bag.append("$100")

    print(f"47: {reward_bag} has been added to your reward bag")
    time.sleep(2)

    print()
    print("47: You and Saraphina vibe at the party and the feeling is getting stronger")
    time.sleep(2)
    print("47: you have fixed a date to take Saraphina out and it will cost you $100")
    time.sleep(2)

    usage2 = input("\nEnter 'yes' to use $100: ")
    while True:
      if usage2.lower().strip() == 'yes':
        print()
        print("47: $100 have been activated for use")
        time.sleep(2)
        print(f"47: Your health is still {health1}")
        time.sleep(2)
        print("47: The date with Saraphina was lovely and you had a lot in common with her")
        time.sleep(2)          
        print("47: you are confident it will last forever and you intend marrying Saraphina")
        time.sleep(2)
        print()
        print("47: The secret room of love, Room 5 is unlocked!")
        time.sleep(3)
        print()
        print("47: Love found!! Congratulations!! You win!!!")
        break
        time.sleep(2)
        print()      

    #play game again
    while ("yes"):  
      print()
      time.sleep(2)
      playagain2 = input("Do you want to play again? (Enter 'yes' to continue or 'quit' to end): ")        
      if playagain2.lower().strip() == 'yes':   
        displayintro()
        choice = choosepath()
        checkpath(choice)
      elif playagain2.lower().strip() == 'quit':
        break    
     

displayintro()
choice = choosepath()
checkpath(choice)
