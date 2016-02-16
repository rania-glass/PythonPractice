#more practice with returns
#Try to predict what will appear on the console before running the function.
#Comment out different lines to see what each one prints.
#Make changes to the function calls below to see what kind of difference it makes
#in the output.


def double(number):
    print "Called double on ", number
    return number * 2

def half(anotherNumber):
    print "Called half on ", anotherNumber
    return anotherNumber/2

def doubleNoReturn(number):
    print "Called doubleNoReturn on ", number
    number = number * 2

def halfNoReturn(anotherNumber):
    print "Called halfNoReturn on ", anotherNumber
    anotherNumber = anotherNumber/2

double(10)
half(10)
doubleNoReturn(10)
halfNoReturn(10)
print "Result of double: ", double(10)
print "Result of half: ", half(10)
print "Result of double(half)): ", double(half(10))
print "Result of doubleNoReturn: ", doubleNoReturn(10)
print "Result of halfNoReturn: ", halfNoReturn(10)
