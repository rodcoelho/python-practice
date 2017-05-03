from pick import pick
import random

#create players to track human and pc
#method of keeping score

class Players:
    def __init__(self):
        self.score = 0

Human = Players()
PC = Players()




#game, gameHuman, gamePC, gameDraw: declares win/loss, displays score, then asks player if he/she wishes to replay

def game():
    play = """Human: %s,  PC: %s.
            Do you want to play Rock, Paper, Scissor?""" %(Human.score, PC.score)
    decide = ('Yes' , 'No')
    decision = pick(decide, play)
    if decision[1] == 0 :
        main()
    else:
        quit()

def gameHuman():
    play = """HUMAN WINS!
            Human: %s,  PC: %s.
            Do you want to play Rock, Paper, Scissor?""" %(Human.score, PC.score)
    decide = ('Yes' , 'No')
    decision = pick(decide, play)
    if decision[1] == 0:
        main()
    else:
        quit()

def gamePC():
    play = """PC WINS!
            Human: %s,  PC: %s.
            Do you want to play Rock, Paper, Scissor?""" %(Human.score, PC.score)
    decide = ('Yes' , 'No')
    decision = pick(decide, play)
    if decision[1] == 0:
        main()
    else:
        quit()

def gameDraw():
    play = """There was a DRAW.
            Human: %s,  PC: %s.
            Do you want to play again?""" %(Human.score, PC.score)
    decide = ('Yes' , 'No')
    decision = pick(decide, play)
    if decision[1] == 0:
        main()
    else:
        quit()


#the actual game
def main():

    title = "Please choose your weapon: "
    options = ('rock', 'paper', 'scissor')

    #computer player picks from list at random
    pcOptions = ['rock', 'paper', 'scissor']
    pcChoice = random.choice(pcOptions)


    #ask user to pick one from list (rock, paper, scissor)
    option, index = pick(options, title)

    print "Human: %s" %option
    print "PC: %s" %pcChoice


    #Judgement. IF statement determines DRAW,  Human winner, or PC winner. Each IF statement sends player back to beginning of game
    if option == pcChoice:
        print "draw"
        gameDraw()

    elif (option == 'rock' and pcChoice == 'scissor' or option == 'paper' and pcChoice == 'rock' or option == 'scissor' and pcChoice == 'paper'):
        print "Human wins"
        Human.score = Human.score + 1
        gameHuman()

    elif (pcChoice == 'rock' and option == 'scissor' or pcChoice == 'paper' and option == 'rock' or pcChoice == 'scissor' and option == 'paper'):
        print "PC wins"
        PC.score = PC.score + 1
        gamePC()

    else:
        print "something went wrong"
        exit()



#initiatize the game
game()
