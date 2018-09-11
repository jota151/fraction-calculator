#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

from fraction import Fraction

def main():
    ''' Main entry point for the app '''
    frac1_num = getNumber("Numerator for Fraction 1:")
    frac1_denom = getNumber("Denominator for Fraction 1:")
    
    operator = getOperator()

    frac2_num = getNumber("Numerator for Fraction 2:")
    frac2_denom = getNumber("Denominator for Fraction 2:")

    fraction1 = Fraction(frac1_num, frac1_denom)
    fraction2 = Fraction(frac2_num, frac2_denom)
    print("First fraction is", fraction1)
    print("Second fraction is", fraction2)
    printResult(fraction1, fraction2, operator)

def printResult(frac1, frac2, op):
    ''' returns and instance of the Fraction class after computing given operation '''
    if op == '+':
        print('{} + {} = {}'.format(frac1, frac2, frac1.plus(frac2)))
    elif op == '-':
        print('{} - {} = {}'.format(frac1, frac2, frac1.minus(frac2)))
    elif op == '*':
        print('{} * {} = {}'.format(frac1, frac2, frac1.times(frac2)))
    elif op == '/':
        print('{} / {} = {}'.format(frac1, frac2, frac1.divide(frac2)))

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

def test_suite():
    ''' function that demonstrates that the Fraction class works properly '''
    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    f128 = Fraction(12, 8)
    f32 = Fraction(3, 2)

    print('\n**********SAMPLE TEST CASES*************\n')
    print(f12, '+', f12, '=', f12.plus(f12), '[4/4]')
    print(f12, '+', f44, '=', f12.plus(f44), '[12/8]')
    print(f128, '-', f12, '=', f128.minus(f12), '[16/16]' )
    print(f12, '*', f32, '=', f12.times(f32), '[3/4]')
    print(f128, '/', f32, '=', f128.divide(f32), '[24/24]')
    print(f128, "==", f32, "is", f128.equal(f32), '[True]')
    print(f12, '+', f12, '+', f12, '==', f32, 'is', f12.plus(f12.plus(f12)).equal(Fraction(3, 2)), '[True]')
    print('\n*****************************************\n')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    test_suite()
    main()