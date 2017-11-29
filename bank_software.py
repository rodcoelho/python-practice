import sqlite3
from random import randint

def create_account(username, password, client_first_day, permission):
    acctnum = ''.join(["%s" % randint(0, 9) for num in range(0, 10)])
    # create user in DB
    cursor.execute("""INSERT INTO users(username, password, client_first_day, permission, acctnum)
                    VALUES('{}','{}','{}','{}','{}')
                    """.format(username, password, client_first_day, permission, acctnum))
    # create acct for user in DB
    cursor.execute("""INSERT INTO accts(acctnum, balance)
                            VALUES('{}',1000)
                            """.format(acctnum))
    return username, acctnum

def check_balance(username):
    #check balance
    cursor.execute("""
    SELECT users.username, accts.balance, users.acctnum
    FROM accts
    JOIN users
    ON accts.acctnum = users.acctnum
    WHERE users.username = '{}';
            """.format(username))
    data = cursor.fetchall()
    return data

def transfer(userfrom, userto, amount):
    # update userfrom balance
    cursor.execute("""
        SELECT users.username, accts.balance, users.acctnum
        FROM accts
        JOIN users
        ON accts.acctnum = users.acctnum
        WHERE users.username = '{}';
                """.format(userfrom))
    datafrom = cursor.fetchall()
    new_bal = datafrom[0][1] - amount
    cursor.execute("""
        UPDATE accts
        SET balance = '{}'
        WHERE accts.acctnum = '{}'
        ;
                """.format(new_bal,datafrom[0][2]))
    # update userto balance
    cursor.execute("""
            SELECT users.username, accts.balance, users.acctnum
            FROM accts
            JOIN users
            ON accts.acctnum = users.acctnum
            WHERE users.username = '{}';
                    """.format(userto))
    datato = cursor.fetchall()
    new_balto = datato[0][1] + amount
    cursor.execute("""
            UPDATE accts
            SET balance = '{}'
            WHERE accts.acctnum = '{}' 
            ;
                    """.format(new_balto, datato[0][2]))

if __name__ == '__main__':
    # connect to db
    connection = sqlite3.connect('privatebank.db')
    cursor = connection.cursor()

    ## account creation
    # user_one, acct_num_1 = create_account('user_one', 'open_sesame1','2017-11-29','0')
    # user_two, acct_num_2 = create_account('user_two', 'open_sesame2','2017-11-29','0')

    x = check_balance('user_one')
    print('check balance function output {}'.format(x))
    x = check_balance('user_two')
    print('check balance function output {}'.format(x))

    print('Going to transfer 500 from user_one to user_two')
    transfer('user_one', 'user_two', 500)

    x = check_balance('user_one')
    print('check balance function output {}'.format(x))
    x = check_balance('user_two')
    print('check balance function output {}'.format(x))

    # disconnect from db
    connection.commit()
    cursor.close()
    connection.close()