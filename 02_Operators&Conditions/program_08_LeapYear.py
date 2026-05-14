# leap year checking

def checkLeapYear(year):
    if(year % 4 == 0 and year % 400 != 0):
        print(year," year is a leap year.")
    else:
        print(year," is not a leap year")

while(True):

    user_year = int(input("Enter year : "))
    checkLeapYear(user_year)