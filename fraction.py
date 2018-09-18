class Fraction:
    ''' A fraction class that will help us define simple fractions.
        The class will operate operations like add, subtract, multiply and divide.
        It will also test 2 fractions for equality.
    '''
    def __init__(self, num, denom):
        ''' Constructor to define a fraction '''
        self.numerator = num
        if denom != 0:
            self.denominator = denom
        else:
            raise ValueError('\nDenominator cannot be 0!')

    def __add__(self, fraction):
        ''' returns a new instance of class Fraction with the sum of self and other where other is another Fraction '''
        common_denom = self.denominator * fraction.denominator
        common_num = (self.numerator * fraction.denominator) + (fraction.numerator * self.denominator)

        return Fraction(common_num, common_denom)

    def __sub__(self, fraction):
        '''  returns a new instance of class Fraction with the difference of self and other where other is another Fraction '''
        common_denom = self.denominator * fraction.denominator
        common_num = (self.numerator * fraction.denominator) - (fraction.numerator * self.denominator)

        return Fraction(common_num, common_denom)

    def __mul__(self, fraction):
        '''  returns a new instance of class Fraction with the product of self and other where other is another Fraction '''
        common_num = self.numerator * fraction.numerator
        common_denom = self.denominator * fraction.denominator

        return Fraction(common_num, common_denom)

    def __truediv__(self, fraction):
        '''  returns a new instance of class Fraction with the quotient of self and other where other is another Fraction '''
        common_num = self.numerator * fraction.denominator
        common_denom = self.denominator * fraction.numerator

        return Fraction(common_num, common_denom)

    def __eq__(self, fraction):
        ''' Tests if this instance of the fraction is equal to the one passed as argument.
                Returns True if equal, otherwise, False '''
        return (self.numerator * fraction.denominator == self.denominator * fraction.numerator)

    def __ne__(self, fraction):
        ''' Returns True if this instance of the fraction is not equal to the one passed as argument.
            Returns False otherwise. '''
        return not self.__eq__(fraction)

    def __lt__(self, fraction):
        ''' Returns True if this instance of the fraction is less than the one passed as argument.
            Returns False otherwise. '''
        return (self.numerator * fraction.denominator < self.denominator * fraction.numerator)

    def __le__(self, fraction):
        ''' Returns True if this instance of the fraction is less than or equal to the one passed as argument.
            Returns False otherwise. '''
        return (self.numerator * fraction.denominator <= self.denominator * fraction.numerator)

    def __gt__(self, fraction):
        ''' Returns True if this instance of the fraction is greater than the one passed as argument.
            Returns False otherwise. '''
        return not self.__le__(fraction)

    def __ge__(self, fraction):
        ''' Returns True if this instance of the fraction is greater than or equal to the one passed as argument.
            Returns False otherwise. '''
        return not self.__lt__(fraction)

    def __str__(self):
        ''' Returns a string representation of the fraction '''
        if self.numerator == 0:
            return '0'
        elif self.numerator < 0 and self.denominator < 0:
            return '{}/{}'.format(abs(self.numerator), abs(self.denominator))
        else:
            return '{}/{}'.format(self.numerator, self.denominator)
