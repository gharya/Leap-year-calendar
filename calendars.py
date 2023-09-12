# -*- coding: utf-8 -*-
"""
Functions about calendars

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Arya Ghaderi
"""
__version__ = 1

def gregorian(year):
#The following code is used to determine if the given year follows the gregorain
#calendar or not. I implemented f strings to allow for the output to be much
#more clear and to give a better understanding of what the answers are for.
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print(f'gregorian({year})', True)
        return True
    elif year % 4 == 0 and year % 100 >= 1 and year % 400 >= 1:
        print(f'gregorian({year})', True)
        return True
    elif year % 4 == 0 and year % 100 >= 1 and year % 400 == 0:
        print(f'gregorian({year})', True)
        return True
    else:
        print(f'gregorian({year})', False)
        return False


def milankovic(year):
#The code below is similar to the one used for gregorian with f string's are still
#being used to make the output much more organized.
    if year % 4 == 0 and year % 100 == 0 and (year % 900 == 200 or year % 900 == 600):
        print(f"milankovic({year})", True)
        return True
    if year % 4 == 0 and year % 100 >= 1 and (year % 900 != 200 or year % 900 != 600):
        print(f"milankovic({year})", True)
        return True
    if year % 4 == 0 and year % 100 >= 1 and (year % 900 == 200 or year % 900 == 600):
        print(f"milankovic({year})", True)
        return True
    else:
        print(f"milankovic({year})", False)
        return False


def gregorian_count(year1, year2):
    count = 0
    for year in range(year1,year2):
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            count += 1
        elif year % 4 == 0 and year % 100 >= 1 and year % 400 >= 1:
            count += 1
        elif year % 4 == 0 and year % 100 >= 1 and year % 400 == 0:
            count += 1
        else:
            count += 0
    print(f"gregorian_count({year1}, {year2})",count)
    return count
    


def milankovic_count(year1, year2):
    count = 0
    for year in range(year1,year2):
        if year % 4 == 0 and year % 100 == 0 and (year % 900 == 200 or year % 900 == 600):
            count += 1
        if year % 4 == 0 and year % 100 >= 1 and (year % 900 != 200 or year % 900 != 600):
            count += 1
        if year % 4 == 0 and year % 100 >= 1 and (year % 900 == 200 or year % 900 == 600):
            count += 1
        else:
            count += 0
    print(f"milankovic_count({year1}, {year2})",count)
    return count



def main():
    gregorian_test()
    gregoriancount_test()
    milankovic_test()
    milankoviccount_test()


###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for gregorian()
def gregorian_test():
#The following tests are for the gregorian() function only and return True or
#False. Print() is used to put a gap between each test to make it more organized
    gregorian(1742)
    gregorian(1946)
    gregorian(2023)
    gregorian(1642)
    print()
#Below are the tests for gregorian_count()
def gregoriancount_test():
#The code below tests gregorian_count() and return how many leap days there
#are between the 2 given years
    gregorian_count(1642,1945)
    gregorian_count(1842,2023)
    gregorian_count(1842,2100)
    gregorian_count(1945,2000)
    print()

# Below are the tests for milankovic()
def milankovic_test():
#The following tests are for milankovic() only and return a True or False
    milankovic(1941)
    milankovic(2020)
    milankovic(1846)
    milankovic(1642)
    print()
# Below are the tests for milankovic_count
def milankoviccount_test():
#The code below is for milankovic_count() and are the same as gregorian_count()
#tests
    milankovic_count(1600,2000)
    milankovic_count(1742,1945)
    milankovic_count(1242,2020)
    milankovic_count(2020,2400)
    print()

    
###############################################################    
    
if __name__ == "__main__":
    main()    