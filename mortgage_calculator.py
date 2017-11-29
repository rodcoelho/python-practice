months = 120
int = .05
price = 100000

def mortgage_calculator(price, int, months):
    top = price * (int/12) * ((1 + (int/12)) ** months)
    bottom = ((1 + (int/12))**months) - 1
    return top/bottom

monthly_payment = mortgage_calculator(price,int,months)
print(monthly_payment)

balance_list = []
total_payment_due = months * monthly_payment
total_payment_paid = 0
for i in range(months):
    total_payment_due -= monthly_payment
    total_payment_paid += monthly_payment
    balance_list.append(['month {}'.format(i),total_payment_due,total_payment_paid])
print(balance_list)