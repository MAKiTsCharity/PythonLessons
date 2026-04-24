# there are a lot of scenarios in which there is no need to reinvent the wheel, and it is better to just load in some code someone else has made
# and in scenarios like these, it's better to just import a library, and go with it


# for example, lets say you'd like to calculate factorial of some kind of number, believe it or not there is no way to do it in standard python
# so instead a natural approach could be to... implement it yourself

def fact(n):
    retVal = 1
    for nindex in range(1,n+1):
        retVal *= nindex
    return retVal

# and there, now we can calculate the factorial for a couple of values

print(fact(3))
print(fact(4))
print(fact(5))

# but that's a hassle, and factorial is a pretty common maths function, which is why instead of doing all that you can just import the math library
import math

# and calculate the factorial using the function from the math library

print(math.factorial(3))
print(math.factorial(4))
print(math.factorial(5))

# if you have something specific you'd like to import, you can import that thing instead to make the process easier

from math import factorial

print(factorial(3))
print(factorial(4))
print(factorial(5))