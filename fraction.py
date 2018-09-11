class Fraction:
    ''' A fraction class that will help us define simple fractions.
        The class will operate operations like add, subtract, multiply and divide.
        It will also test 2 fractions for equality.
    '''
    def __init__(self, num, denom):
        ''' Constructor to define a fraction '''
        self.numerator = num
        self.denominator = denom

    def add(self, fraction):
        ''' Adds this instance of fraction to the one passed as argument '''

    def subtract(self, fraction):
        ''' Subtracts the fraction passed as argument from this instance of fraction '''

    def multiply(self, fraction):
        ''' Multiplies the fraction passed as argument to this instance of fraction '''

    def divide(self, fraction):
        ''' Divides this instance of fraction by the one passed as argument '''

    def equals(self, fraction):
        ''' Tests if this instance of the fraction is equal to the one passed as argument.
            Returns True if equal, otherwise, False '''

    def __str__(self):
        ''' Returns a string representation of the fraction '''
        return '{}/{}'.format(self.numerator, self.denominator)