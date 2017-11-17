from pick import pick
import random
from random import randint

decision_question = """ 
            Human: %s,  PC: %s.
            Do you want to play Roulette?
            """
decide = ('Yes', 'No')


# create players to track human and pc
# method of keeping score
class Players:
    def __init__(self,score):
        self.score = score
Human = Players(100)
PC = Players(0)

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
    play = start + decision_question % (humanScore, pcScore)
    return play


# the actual game, PC chooses 'weapon' at random, Human player is given an option of which weapon
def main():
    bet_question = "How much would you like to bet?"
    bet_answer = (1, 5, 10, 20, 50)

    title = "Make your pick: "
    options = ('A random number', 'all reds', 'all blacks', 'odds', 'evens', '1-18',
               '19-36', '0', '00')

    option_dictionary = {'all reds':[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
                         'all blacks':[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
                         'odds':[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35],
                         'evens':[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36],
                         '1-18':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
                         '19-36':[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36],
                         '0': 0,
                         '00':.00}
    # computer picks
    pcOptions = ['0','00','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16',
                 '17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33',
                 '34','35','36']
    pcChoice = random.choice(pcOptions)

    #user bets
    bet,position = pick(bet_answer,bet_question)

    # user picks

    option, index = pick(options, title)

    if option == 'A random number':
        final_int = randint(0, 36)
    else:
        final_int = str(option_dictionary[option])

    print(""" 
                Choice:  %s    Reality: %s 
                         """ % (final_int, pcChoice))

    if final_int == pcChoice:
        start = """
                WINNER!    
                """
        Human.score = Human.score + bet
        PC.score = PC.score - bet
        game(Human.score, PC.score, start)


    elif pcChoice != final_int:
        start = """
                Sorry... Come again  
                    """
        Human.score = Human.score - bet
        PC.score = PC.score + bet
        game(Human.score, PC.score, start)


    else:
        print ("something went wrong")
        exit()


# initiatize the game, begins scores at '100,0' and defaults start to a blank string.
game(100,0, "   ")