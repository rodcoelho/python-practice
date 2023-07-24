import math

def currency_converter(amount):
    # we need to seperate the float into dollar and cents
    # x = (decimals, whole numbers)
    x = math.modf(amount)

    # add the decimals and whole numbers * 100 (to make everything into pennies)
    total_pennies = (float("{0:.2f}".format(x[0]))* 100.0 + (x[1] * 100.0))

    # for conversions and totals to print in the end
    hundred = [0.0, 10000.0]
    fifty = [0.0, 5000.0]
    ten = [0.0, 1000.0]
    five = [0.0, 500.0]
    dollar = [0.0, 100.0]
    quarter = [0.0, 25.0]
    dime = [0.0, 10.0]
    nickel = [0.0, 5.0]

    def mini_converter(currency, total_pennies):
        if total_pennies >= currency[1]:
            #changes the currency[0] in the conversions above to the divisions with no remainders
            currency[0] += total_pennies // currency[1]
            #makes the total_pennies variable the remainder of the division we just ran in the line above
            total_pennies = total_pennies % currency[1]
        return currency, total_pennies

    # calling of the mini_converter function
    hundred,total_pennies = mini_converter(hundred, total_pennies)
    fifty,total_pennies = mini_converter(fifty, total_pennies)
    ten,total_pennies = mini_converter(ten, total_pennies)
    five,total_pennies = mini_converter(five, total_pennies)
    dollar,total_pennies = mini_converter(dollar, total_pennies)
    quarter,total_pennies = mini_converter(quarter, total_pennies)
    dime,total_pennies = mini_converter(dime, total_pennies)
    nickel,total_pennies = mini_converter(nickel, total_pennies)
    penny = total_pennies

    # simple print
    print('Hundred: {}'.format(hundred[0]))
    print('Fifty: {}'.format(fifty[0]))
    print('Ten: {}'.format(ten[0]))
    print('Five: {}'.format(five[0]))
    print('Dollar: {}'.format(dollar[0]))
    print('Quarter: {}'.format(quarter[0]))
    print('Dime: {}'.format(dime[0]))
    print('Nickel: {}'.format(nickel[0]))
    print('Penny: {}'.format(penny))