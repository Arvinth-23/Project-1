import random
number_to_guess=random.randint(1,100)
while True:
    try:
       guess =int(input("Guess the number from 1 to 100:"))
       if guess< number_to_guess: 
          print("to low")
       elif guess>number_to_guess:
           print("too high")
       else:
            print("You guessed the number")
    except ValueError:
         print("Enter the Valid Number")      