class Complex(object):
    def __init__(self, realpart, imagpart):
        '''Creates Complex Number'''
        self.r = realpart
        self.i = imagpart

    def __str__(self):
        '''Returns complex number as string'''
        if self.i > 0:
            return '%s + %si' % (self.r, self.i)
        elif self.i < 0:
            return '%s - %si' % (self.r, -(self.i))
        else:
            return self.r

    def __add__(self, lhs):
        # lhs = left hand side
        '''Adds complex numbers'''
        return Complex(lhs.r + self.r, lhs.i + self.i)

    def __sub__(self, rhs):
        # rhs = right hand side
        '''Subtracts complex numbers'''
        return Complex(self.r - rhs.r, self.i - rhs.i)

    def __mul__(self, rhs):
        return Complex((self.r * rhs.r) - (self.i * rhs.i), (self.r * rhs.i) + (self.i * rhs.r))
        
    def __truediv__(self, rhs):
        conjugation = Complex(rhs.r, -rhs.i)
        denominator = rhs * conjugation
        nominator = self * conjugation
        return Complex(nominator.r/denominator.r, nominator.i/denominator.r)