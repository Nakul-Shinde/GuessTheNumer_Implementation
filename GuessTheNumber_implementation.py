import random


logo="""                                                                                                          

   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                                   

                                                                                                     
"""
threshold=0
attempt=0
com_number=random.randint(1,100)


def difficulty_level(difficulty):
    if difficulty=='easy':
        attempt=10
        return attempt
        
    else:
        attempt=5
        return attempt
    
   


def compare_number(user_guess):
    global com_number
    if user_guess> com_number:
        print("Too High")
        return 1
    elif user_guess< com_number:
        print("Too Low")
        return 1
    else:
         print("You Guessed it correct!!")       
         print("The number is :",com_number) 
         return 0
         
def correct_guess(attempt):
    global threshold    
    correct_guess='false'
    while correct_guess!='true':
                threshold+=1
                user_guess=int(input("Make a Guess:"))
                if user_guess>100:
                    print("Please enter valid number")
                    correct_guess='false'
                    threshold-=1
                   # print(threshold)
                else:
                    no= compare_number(user_guess)
                    if no==1:
                        print("The remaining attempts:",attempt-threshold)
                       # print(threshold)
                        
                    else:
                        break  
                    if threshold==attempt:
                        print("You ran out of Attempts")
                        break     
  
        
  

print(logo)
print("Welcome to the Guess the Number....")
print("I'm thinking about a number between 1 and 100.")


difficulty=input("Please select the Difficulty of game 'easy' or 'hard':")
attempt=difficulty_level(difficulty)
correct_guess(attempt)

             
             
        
