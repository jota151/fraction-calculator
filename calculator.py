#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

def main():
    ''' Main entry point for the app '''
    frac1_num = getNumber("Numerator for Fraction 1:")
    frac1_denom = getNumber("Denominator for Fraction 1")
    
    operator = getOperator()

    frac2_num = getNumber("Numerator for Fraction 2:")
    frac2_denom = getNumber("Denominator for Fraction 2:")

def getOperator():
    while True:
        operator = input("Choose one operator +, -, *, / :")
        if operator == '+' or operator == '-' or operator == '*' or operator == '/':
            return operator
        else:
            print("Invalid operator!")

def getNumber(message):
    ''' Function accepts a string message to show on the console
        and returns an integer value or shows ValueError exception '''
    while True:
        number = input(message)
        try:
            return int(number)
        except ValueError:
            print('{} is not an integer. Please enter an integer value.'.format(number))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()