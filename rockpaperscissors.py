from pick import pick
import random

# redundant messages that print throughout game
decision_question = """ 

            Human: %s,  PC: %s.
            Do you want to play Rock, Paper, Scissor?
            
            """
decide = ('Yes', 'No')



#create players to track human and pc
#method of keeping score
class Players:
    def __init__(self):
        self.score = 0
Human = Players()
PC = Players()


# the game prompts the pick 'pop-up' (described in func below)
def game(humanScore, pcScore, start):
    play = create_string(pcScore, humanScore, start)
    decide_popup(play)

# the pop-up gives the Human player the decision whether he will play the game or not
#  gives the Human the ability to leave/quit the game easily
def decide_popup(play):
    decision = pick(decide, play)
    if decision[1] == 0:
        main()
    else:
        quit()

# this func displays the total score, the winner of the previous game, and the string that appears int he pop-up
def create_string(pcScore, humanScore, start):
    play =  start + decision_question % (humanScore, pcScore)
    return play


# the actual game, PC chooses 'weapon' at random, Human player is given an option of which weapon
def main():

    title = "Choose your weapon: "
    options = ('rock', 'paper', 'scissor')

    #computer picks
    pcOptions = ['rock', 'paper', 'scissor']
    pcChoice = random.choice(pcOptions)


    #user picks
    option, index = pick(options, title)

    print  """ 
                Human:  %s    PC: %s 
                         """ % (option, pcChoice)



    # Judgement of Winner/Draw. Simple IF statement that determines DRAW,  Human winner, or PC winner
    # Each IF statement sends player back to beginning of game
    if option == pcChoice:
        start =  """
                DRAW    
                """
        game(Human.score, PC.score, start)

    elif (option == 'rock' and pcChoice == 'scissor'
          or option == 'paper' and pcChoice == 'rock'
          or option == 'scissor' and pcChoice == 'paper'):
        start = """ 
                HUMAN WINS      
                 """
        Human.score = Human.score + 1
        game(Human.score,PC.score, start)

    elif (pcChoice == 'rock' and option == 'scissor'
          or pcChoice == 'paper' and option == 'rock'
          or pcChoice == 'scissor' and option == 'paper'):
        start =  """
                PC WINS  
                    """
        PC.score = PC.score + 1
        game(Human.score, PC.score, start)

    else:
        print "something went wrong"
        exit()



#initiatize the game, begins scores at '0,0' and defaults start to a blank string.
#the default start variable will be replaced each round with winner/draw string
game(0,0, "   ")
