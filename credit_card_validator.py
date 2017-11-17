creditcardnum = '559179199857686'

class CreditCard:

    def __init__(self, card_number):
        self.card_number = card_number

    def determine_card_type(self):
        mastercard = ['51', '52', '53', '54', '55']
        if str(self.card_number[0]) == '4':
            self.card_type = 'Visa'
        elif str(self.card_number[:2]) in mastercard:
            self.card_type = 'Mastercard'
        elif str(self.card_number[0]) == '3':
            self.card_type = 'AMEX'
        elif str(self.card_number[0]) == '6':
            self.card_type = 'Discover'
        else:
            self.card_type = 'INVALID'
        return self.card_type

    def check_length(self):
        if len(self.card_number) == 15 or len(self.card_number) == 16:
            self.card_len = "Length of typical credit card"
        else:
            self.card_len = "INVALID"
        return self.card_len

    def check_luhn(self):
        #reverse string
        numstr = self.card_number[::-1]

        revstr = []
        #move nums into list as ints
        for elements in numstr:
            revstr.append(int(elements))

        everyotherlist = []
        #every other int, we times by two
        for i in range(len(revstr)):
            if i % 2 == 0:
                everyotherlist.append(revstr[i]*2)
            else:
                everyotherlist.append(revstr[i])

        #make into string again
        strlist2 = []
        for elements in everyotherlist:
            strlist2.append(str(elements))
        tempstr = ''.join(strlist2)

        #make each individual digit into its own number
        indi_num_list = []
        for chars in tempstr:
            indi_num_list.append(int(tempstr))

        #add each individual number
        final_num = 0
        for elements in indi_num_list:
            final_num += elements

        #sum of nums % 10
        result = final_num % 10

        # if result is zero, the credit card is valid
        if result == 0:
            self.luhn = "VALID"
        else:
            self.luhn = "INVALID"
        return self.luhn

    def validate(self):
        type_test = self.determine_card_type()
        len_test = self.check_length()
        luhn_test = self.check_luhn()
        print("Card type: ", type_test)
        print("Digit test: ",len_test)
        print("Luhn Test: ", luhn_test)
        count = 0
        if type_test is "INVALID":
            count += 1
            print('     Your Credit Card is invalid - Credit Cards do not start with the number {}'.format(self.card_number[:4]))
        if len_test is "INVALID":
            count += 1
            print('     Your Credit Card is invalid - Credit Cards usually have either 15 or 16 digits - Your card has {} digits'.format(len(self.card_number)))
        if luhn_test is "INVALID":
            count += 1
            print('     Your Credit Card is invalid- Your credit card has not passed the Luhn Test')
        if count == 0:
            print()
            print("Your Credit Card is VALID and is {}!".format(self.card_type))
            print()
def main():
    cc_number = creditcardnum
    cc = CreditCard(cc_number)
    cc.validate()

if __name__ == '__main__':
    main()