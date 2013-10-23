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
    
    name = {0 : 'rock', 1 : 'Spock', 2 : 'paper', 3 : 'lizard', 4 : 'scissors'} 

    if number in name:
        return name[number]
    else:
        return name
        
    
    
def name_to_number(name):
    number = {'rock' : 0, 'Spock' : 1, 'paper': 2, 'lizard' : 3, 'scissors' : 4} 

    if name in number:
        return number[name]
    else:
        number = 6
        return number
   

    # main function


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
  
    print('\n' + 'Player choose ' + name + '\n' + 'Computer choose ' + computer_name + '\n' + winner) 
        
   
    
    

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("bazinga")

# always remember to check your completed program against the grading rubric

