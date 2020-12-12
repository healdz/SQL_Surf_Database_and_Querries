#Zane Heald - SQL Assignment 7
#This code provides a series of options for the user to run on the surflessons sql data bases to provide interactive querry results.
import pymysql
import getpass
import statistics as stats

passwd = getpass.getpass("password: ")
db = pymysql.connect(host="localhost", user="root", passwd=passwd, db="surflessons")


def tableShow():
    sqlCmdStr = "show tables;"
    with db.cursor() as cur:
        cur.execute(sqlCmdStr)
        for tableTuple in cur.fetchall():
            print(f'{tableTuple[0]}')

def tableDescribe(tableName):
    sqlCmdStr = f"describe {tableName};"
    with db.cursor() as cur:
        try:
            cur.execute(sqlCmdStr)
        except pymysql.Error:
            print("there does not seem to be a table with that name. ")
            return
        for attribute in cur.fetchall():
            print(f'{attribute[0]} | {attribute[1]}')
            ##print(" | ".join([a for a in attribute]))

def printMenu():
    print("menu:")
    print("s - show tables")
    print("d - describe a table")
    print("l - Language options")
    print("a - Count and average rating of instructors who speak a given language ")
    print("w - Average wave size per weather types")
    print("i - Proportion of injuries to wave size")

def languageTypes():
    sqlCmdStr = "select languages from instructors group by languages order by languages;"
    cur = db.cursor()
    cur.execute(sqlCmdStr)
    print('The languages spoken are:')
    for attr in cur.fetchall():
        print(f"{attr[0]}")

def avgRatingLanguage(language):
    '''This function will return the average rating and count of instructors who speak a specified language.'''
    sqlCmdStr = 'select count(instructorID), avg(rating), languages From instructors where languages = \'' + language +'\';'
    with db.cursor() as cur:
        try:
            cur.execute(sqlCmdStr)
        except pymysql.Error:
            print(f"That query failed. The possible languages are English, French, Spanish, German or Finnish.")
        x = cur.fetchall()
        for attribute in x:
            print(f'There are {attribute[0]} instructors who speak {language} and the average rating is {attribute[1]}')

def weatherTypes():
    sqlCmdStr = "select avg(sw.wavesize),SW.weather from surfswith SW group by sw.weather order by SW.weather;"
    cur = db.cursor()
    cur.execute(sqlCmdStr)
    print('The Average wave size for each type of weather that clients have experienced is:')
    for attr in cur.fetchall():
        print(f"{attr[0]}   {attr[1]}")

def injuryProportion(wavesize):
    sqlCmdStr = "select wavesize, count(injuries) from surfswith where injuries = 'Yes' and wavesize >= "+wavesize+" group by wavesize order by wavesize;"
    cur = db.cursor()
    cur.execute(sqlCmdStr)
    nextCmd = "select count(*) from surfswith where injuries = 'yes';"
    c = db.cursor()
    c.execute(nextCmd)
    x = c.fetchall()
    t = x[0]
    total = t[0]
    print('The Average wave size for each type of weather that clients have experienced is:')
    for attr in cur.fetchall():
        print(f"{round((attr[1]/total)*100.00,3)}% of injuries come when waves are {attr[0]} feet tall")

def main():
    print("Welcome to a thing for the surflessons database.")
    quit = False
    while not quit:
        print("\nWhat would you like to do? (m for menu, q for quit)")
        choice = input(": ")
        if choice[0] == "m":
            printMenu()
        elif choice[0] == "s":
            print("showing tables: ")
            tableShow()
        elif choice[0] == "d":
            tableName = input("describe which table: ")
            tableDescribe(tableName)
        elif choice[0] == "l":
            languageTypes()
        elif choice[0] == "w":
            weatherTypes()
        elif choice[0] == "a":
            lang = input("Please enter a language:")
            avgRatingLanguage(lang)
        elif choice[0] == "i":
            size = input("Greater than or equal to what wave height? (9 feet is maximum): ")
            injuryProportion(size)
        elif choice[0] == "q":
            quit = True


if __name__ == "__main__":
    main()
