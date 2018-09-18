#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

from fraction import Fraction
validOperators =  ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=']

def main():
    ''' Main entry point for the app '''

    fraction1 = createFraction('Fraction 1')
    operator = getOperator()
    fraction2 = createFraction('Fraction 2')
    
    print("\nFirst fraction is", fraction1)
    print("\nSecond fraction is", fraction2)
    printResult(fraction1, fraction2, operator)

def createFraction(fracName):
    ''' Returns a valid fraction instance.
        Takes a string to denote as label for the console message. '''

    numerator = getNumber('\nNumerator for {} :'.format(fracName))
    
    while True:
        denominator = getNumber('\nDenominator for {} :'.format(fracName))
        try:
            return Fraction(numerator, denominator)
        except ValueError as e:
            print(e)

def printResult(frac1, frac2, op):
    ''' returns and instance of the Fraction class after computing given operation '''

    if op == '+':
        print('\n{} + {} = {}'.format(frac1, frac2, frac1 + frac2))
    elif op == '-':
        print('\n{} - {} = {}'.format(frac1, frac2, frac1 - frac2))
    elif op == '*':
        print('\n{} * {} = {}'.format(frac1, frac2, frac1 * frac2))
    elif op == '/':
        print('\n{} / {} = {}'.format(frac1, frac2, frac1 / frac2))
    elif op == '==':
        print('\n{} == {} = {}'.format(frac1, frac2, frac1 == frac2))
    elif op == '!=':
        print('\n{} != {} = {}'.format(frac1, frac2, frac1 != frac2))
    elif op == '<':
        print('\n{} < {} = {}'.format(frac1, frac2, frac1 < frac2))
    elif op == '<=':
        print('\n{} <= {} = {}'.format(frac1, frac2, frac1 <= frac2))
    elif op == '>':
        print('\n{} > {} = {}'.format(frac1, frac2, frac1 > frac2))
    elif op == '>=':
        print('\n{} >= {} = {}'.format(frac1, frac2, frac1 >= frac2))

def getOperator():
    ''' returns the operator chosen by the user '''

    while True:
        operator = input("\nChoose one operator: {} ".format(validOperators))
        # if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        if operator in validOperators:
            return operator
        else:
            print("\nInvalid operator!")

def getNumber(message):
    ''' Function accepts a string message to show on the console
        and returns an integer value or shows ValueError exception '''

    while True:
        number = input(message)
        try:
            return int(number) # float?
        except ValueError:
            print('\n{} is not an integer! Please enter an integer value.'.format(number))

def test_suite():
    ''' function that demonstrates that the Fraction class works properly '''

    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    f128 = Fraction(12, 8)
    f32 = Fraction(3, 2)

    print('\n**********SAMPLE TEST CASES*************\n')
    print(f12, '+', f12, '=', f12 + f12, '[4/4]')
    print(f12, '+', f44, '=', f12 + f44, '[12/8]')
    print(f128, '-', f12, '=', f128 - f12, '[16/16]' )
    print(f12, '*', f32, '=', f12 * f32, '[3/4]')
    print(f128, '/', f32, '=', f128 / f32, '[24/24]')
    print(f128, "==", f32, "is", f128 == f32, '[True]')
    print(f12, '+', f12, '+', f12, '==', f32, 'is', f12 + f12 +f12 == Fraction(3, 2), '[True]')
    print('\n*****************************************\n')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    
    test_suite()
    main()