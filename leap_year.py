#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 23 2022
# This program asks the user for the year it then sees if that year is a leap year


def main():

    # Get the year
    year_string = input("Enter a year: ")

    # An try catch to catch any errors if they enter a string
    try:
        year_num = int(year_string)
    except Exception:
        print("Please enter a year")
    else:
        # A if statement with nested if statements to determine if year_num is a leap year
        if year_num % 4 == 0:
            if year_num % 100 == 0:
                if year_num % 400 == 0:
                    print("It is a leap year")
                else:
                    print("It is not a leap year")
            else:
                print("It is a leap year")
        else:
            print("It is not a leap year")


if __name__ == "__main__":
    main()
