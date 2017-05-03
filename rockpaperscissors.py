from pick import pick
import random
from time import sleep

#creating players, human and pc, and way to keep score

class Players:
    def __init__(self):
        self.score = 0

Human = Players()
PC = Players()




#main decision whether to play or not

def main():
    play = """Human: %s,  PC: %s.
            Do you want to play Rock, Paper, Scissor?""" %(Human.score, PC.score)
    decide = ('Yes' , 'No')
    decision = pick(decide, play)
    if decision[1] == 0 :
        game()
    else:
        quit()

def mainHuman():
    play = """HUMAN WINS!
            Human: %s,  PC: %s.
            Do you want to play Rock, Paper, Scissor?""" %(Human.score, PC.score)
    decide = ('Yes' , 'No')
    decision = pick(decide, play)
    if decision[1] == 0:
        game()
    else:
        quit()

def mainPC():
    play = """PC WINS!
            Human: %s,  PC: %s.
            Do you want to play Rock, Paper, Scissor?""" %(Human.score, PC.score)
    decide = ('Yes' , 'No')
    decision = pick(decide, play)
    if decision[1] == 0:
        game()
    else:
        quit()

def mainDraw():
    play = """There was a DRAW.
            Human: %s,  PC: %s.
            Do you want to play again?""" %(Human.score, PC.score)
    decide = ('Yes' , 'No')
    decision = pick(decide, play)
    if decision[1] == 0:
        game()
    else:
        quit()


#the actual game
def game():

    title = "Please choose your weapon: "
    options = ('rock', 'paper', 'scissor')

    #computer player picks from list at random
    pcOptions = ['rock', 'paper', 'scissor']
    pcChoice = random.choice(pcOptions)


    #ask user to pick one from list (rock, paper, scissor)
    option, index = pick(options, title)

    print "Human: %s" %option
    print "PC: %s" %pcChoice


    #judge winner/if draw. First determine draw scenario. Then Human winner. Then PC winner.
    if option == pcChoice:
        print "draw"
        mainDraw()

    elif (option == 'rock' and pcChoice == 'scissor' or option == 'paper' and pcChoice == 'rock' or option == 'scissor' and pcChoice == 'paper'):
        print "Human wins"
        Human.score = Human.score + 1
        mainHuman()

    elif (pcChoice == 'rock' and option == 'scissor' or pcChoice == 'paper' and option == 'rock' or pcChoice == 'scissor' and option == 'paper'):
        print "PC wins"
        PC.score = PC.score + 1
        mainPC()

    else:
        print "something went wrong"
        exit()



#initiatize the game
main()
