# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(number):
    # fill in your code below
    
    if number == 0:
        name = 'rock'
        return name
        
    elif number == 1:
        name = 'Spock'
        return name
        
    elif number == 2:
        name = 'paper'
        return name
    
    elif number == 3:
        name = 'lizard'
        return name
        
    elif number == 4:
        name = 'scissors'
        return name
    
    else: 
        return name
      
    
        
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    
    if name == 'rock':
        number = 0
        return number
        
    elif name == 'Spock':
        number = 1
        return number
        
    elif name == 'paper':
        number = 2
        return number
    
    elif name == 'lizard':
        number = 3
        return number
        
    elif name == 'scissors':
        number = 4
        return number
    else:
        number = 6
        return number
      
    

    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
      
    player_number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()

    comp_number = random.randrange(0, 5)
    
    # compute difference of player_number and comp_number modulo five

    remainder = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner
    if player_number < 6: 
    
        if remainder == 1 or remainder == 2:
            winner = 'Player wins!'
        
        elif remainder == 3 or remainder == 4:
            winner = 'Computer wins!'
            
        else:
            winner = 'Player and computer ties!'
            
    elif player_number == 6:
        winner = 'Wrong input name. You should probably check it!'
        

    # convert comp_number to name using number_to_name
    
    computer_name = number_to_name(comp_number)
    
    # print results
  
    print '\n' + 'Player choose ' + name + '\n' + 'Computer choose ' + computer_name + '\n' + winner 
        
   
    
    

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("bazinga")
rpsls("bainga")
# always remember to check your completed program against the grading rubric


