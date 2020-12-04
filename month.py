#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This is month program

def main():

    # input
    month = int(input("Enter the number of month : "))
    print("")

    # process
    if month == 1:
        # output
        print("January")
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("Jun")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("September")
    elif month == 10:
        print("October")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")
    else:
        print("It is not number of month")


if __name__ == "__main__":
    main()
