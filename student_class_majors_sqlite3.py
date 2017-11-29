import sqlite3
import string, random
# from faker import Faker

def create():
    cursor.execute(
        """CREATE TABLE students(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32),
        majorID INTEGER,
        classID INTEGER
        );"""
    )
    cursor.execute(
        """CREATE TABLE classes(
        classID INTEGER,
        className VARCHAR(32)
        );"""
    )
    cursor.execute(
        """CREATE TABLE majors(
        majorID INTEGER,
        majorName VARCHAR(32)
        );"""
    )

def seed():
    for i in range(1000):
        name = 'john'+ ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
        className = 'class' + ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
        majorName = 'major'+ ''.join(random.choice(string.ascii_uppercase) for _ in range(7))
        majorID = random.randint(0,200)
        classID = random.randint(0,200)
        cursor.execute(
            """
            INSERT INTO students(name, majorID, classID)
            VALUES('{}','{}','{}')
            ;""".format(name,majorID,classID)
        )
        cursor.execute(
            """
            INSERT INTO classes(classID, className)
            VALUES('{}','{}')
            ;""".format(classID,className)
        )
        cursor.execute(
            """
            INSERT INTO majors(majorID, majorName)
            VALUES('{}','{}')
            ;""".format(majorID, majorName)
        )

def people_who_share_classes_with(name1):
    # get name1's classes
    cursor.execute(
        """
        SELECT classes.className
        FROM students
        JOIN classes
        ON students.classID = classes.classID
        WHERE students.name = '{}'
        ;""".format(name1)
    )
    name1_classes = cursor.fetchall()
    classes = []
    for tups in name1_classes:
        for elements in tups:
            classes.append(elements)
    print()
    tc = set()
    #find names of students who take same classes
    for elements in classes:
        cursor.execute(
            """
            SELECT students.name
            FROM students
            JOIN classes
            ON students.classID = classes.classID
            WHERE classes.className = '{}'
            ;""".format(elements)
        )
        t1 = cursor.fetchall()
        for elements in t1:
            tc.update(elements)
    return tc

def classes_shared_between_two(name1,name2):
    # get name1 and name2's classes
    cursor.execute(
        """
        SELECT classes.className
        FROM students
        JOIN classes
        ON students.classID = classes.classID
        WHERE students.name = '{}'
        ;""".format(name1)
    )
    l1 = cursor.fetchall()
    cursor.execute(
        """
        SELECT classes.className
        FROM students
        JOIN classes
        ON students.classID = classes.classID
        WHERE students.name = '{}'
        ;""".format(name2)
    )
    l2 = cursor.fetchall()
    common = set()
    for elements in l1:
        if elements in l2:
            common.update(elements)
    for elements in l2:
        if elements in l1:
            common.update(elements)
    return common



if __name__ == "__main__":
    connection = sqlite3.connect('schedules.db')
    cursor = connection.cursor()

    ## first step is to create and seed the database
    # create()
    # seed()

    # check out who your person has class with
    y = people_who_share_classes_with('john_doe')
    print(y)

    # check if you have class with a friend
    x = classes_shared_between_two('john_doe','johnny_boy')
    print(x)

    connection.commit()
    cursor.close()
    connection.close()