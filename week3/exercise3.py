"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
#     print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    
    lowerBound = input("Enter a lower bound: ")
    
    valueGuess = False

    while valueGuess == False:
      upperBound = input("Enter an upper bound: ")
      try:
        int(upperBound)
        valueGuess = True
      except ValueError:
        print("A Number pls!")
      if lowerBound < upperBound:
        valueGuess = True
      else:
        print("Try a higher bound")

    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))
    upperBound = int(upperBound)
    lowerBound = int(lowerBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        try:
          lowerBound < guessedNumber < upperBound
        except ValueError:
          guessedNumber = int(input("Not a legit number innit mate"))
        except TypeError:
          guessedNumber = int(input("Not a legit number innit mate"))
        print("You guessed {},".format(int(guessedNumber)),)
        
  if int(guessedNumber) == actualNumber:
              print("You got it!! It was {}".format(actualNumber))
              guessed = True
          elif int(guessedNumber) < actualNumber:
              print("Too small, like my respect for you")
          else:
              print("Too big, like my expectations of you :'(")
      return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!






def not_number_rejector(message):
  
    number_5 = False

    while number_5 == False:
        ask = str(input(message)) #pick a number
        if ask.isdigit():
            return int(ask)
        else:
            print ("Try again, that's not a number")




if __name__ == "__main__":
    print(advancedGuessingGame())