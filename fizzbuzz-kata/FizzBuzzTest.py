import pytest


def fizzbuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    elif isMultiple(value, 5):
        if isMultiple(value, 3):
            return "FizzBuzz"
        return "Buzz"
    else:
        return str(value)

def isMultiple(value, mod):
    return (value % mod) == 0
