from FizzBuzzTest import fizzbuzz

def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzbuzz(value)
    assert retVal == expectedRetVal

def test_return1WithPassedIn():
    checkFizzBuzz(1, "1")

def test_return2WithPassedIn():
    checkFizzBuzz(2, "2")

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

def test_returnsFizzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")

def test_returnsFizzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

def test_returnsFizzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")