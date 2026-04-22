iterator = 0

def fibNumber(n): # in order to define a function we use the "def" on the beginning, then "nameOfFunciton(variables)", like so
    preFibNumber = 0 # inside of this definition we can define our variables we'd like to use, there are no restrictions,
    postFibNumber = 1 # but do keep in mind that you won't be able to access these variables outside the function
    tempFibNumber = 0# they are made only in the definition, so they are kind of like the "template for variables", ouside of this definition "preFibNumber" does not exist

    global iterator # we can access variables from outside the definition, but we need to specifically warn python that we're doing so, by telling it that it's a global variable
    iterator += n # we can then add things to those variables, but once again, mind the "global"
    
    insideIterator = 0
    
    while insideIterator < iterator: # then logic-wise, we can do whatever we want inside the function, it really doesn't matter
        tempFibNumber = preFibNumber # go ham, introduce variables
        preFibNumber = postFibNumber # temporary, intended
        postFibNumber += tempFibNumber # do math do physics
        insideIterator += 1  # world is your crab

    return postFibNumber # and at the end we can define what the function returns, this is important because this is the value we get back from the function

for i in range(20):
    print(f"{i}.fib: {fibNumber(1)}") # which you can see right here

print(f"iterator: {iterator}") # now, since we setup the function with the "iterator" being outside of the function, it does get modified

# but our other variables, like "preFibNumber" were created inside the function, so they don't exist outside
# if you'd like to see it for yourself, uncomment the next line, and read what the error states
#print(f"iterator: {preFibNumber}") 