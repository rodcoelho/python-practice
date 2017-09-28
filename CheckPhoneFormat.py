from pick import pick
wrong = "Format Error: Phone number has been typed incorrectly"
choose = ('Try Again', 'Exit')

def main():
    get_phonenumber()

def get_phonenumber():
    phone_number = input("Type your phone number (ex: 3331117777):  ")
    checklen(phone_number)

def reset():
    x = pick(choose, wrong)
    if x[1] == 0:
        main()
    else:
        quit()

def checklen(phone_number):
    if len(phone_number) > 10:
        reset()
    elif len(phone_number) < 10:
        reset()
    else:
        print(phone_number, "You typed a correct number")

main()



#next you have to find an alternative for raw_input. Raw_input makes the input into a string. You want one that makes the input into an integer or a float
#then you can add an IF statement that checks if the len = 10 AND check the input type. You want len = 10 AND the type to be integers.

