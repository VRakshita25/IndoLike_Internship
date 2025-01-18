import random
def number_game(score):
    attempt = 0
    number = random.randint(1,50)
    
    while attempt < 10:
        guess = int(input(f"Attempt {attempt + 1} - Guess a number between 1 and 50: "))
        attempt += 1
        if guess > number:
            print("Your guess is higher\n")
       
        elif guess < number:
            print("Your guess is lower\n")
        
        else:
            score += 2
            print(f"Wow!! That's a right guess. The number is {number}.") 
            choice = input("Shall we continue? (yes/no) ").lower() 
            if choice == "yes":
                return number_game(score)  # Properly return to the previous context
            else:
                print(f"Hope you enjoyed playing!! You have scored {score} points in this round!") 
                break
                
    else:
        print(f"You have exhausted your ten attempts. The number was {number}")
        print(f"You have scored {score} points in this round!") 

    
print('''  
      ~~~~~~~~~~~~~~~~   Welcome to the Number Guessing Game!   ~~~~~~~~~~~~~~~~ 
      
      You are allowed to attempt guessing the number to a maximum of 10 times. 
      The game goes on until you keep guessing the numbers right within the TEN attempts.
      If you exhaust your TEN attempts in any round, the game gets terminated 
      and the answer is displayed along with your total score!
      Every correct guess earns you 2 points and there are no reduction in points for wrong guesses. 
      So make sure you play carefully :)
      
      This game is sure to keep to entertained!! 
      
      ''')
score = 0
highest_score = 0
number_game(score)  
  

       