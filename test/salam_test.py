

def fizzBuzz(value):
    if isMultiplle(value , 3):
        if isMultiplle(value , 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiplle(value,5):
        return "Buzz"
     

    return str(value)

def isMultiplle(value , mod):
    return (value % mod) == 0


def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal


def test_returns1WithPassedIn():
    checkFizzBuzz(1, "1")


def test_return2With2PassedIn():
    checkFizzBuzz(2, "2")


def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")


def test_returnsBuzzWith5pass():
    checkFizzBuzz(5, "Buzz")

def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6,"Fizz")
    checkFizzBuzz(9,"Fizz")

def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10,"Buzz")
    checkFizzBuzz(20,"Buzz")
 
def test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15,"FizzBuzz")
    checkFizzBuzz(30,"FizzBuzz")
