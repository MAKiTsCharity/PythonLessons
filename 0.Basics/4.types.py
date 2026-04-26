# despite our variables being created with a really simple line, like so
test = 10
# there is a log happening behind the scenes in order to MAKe that happen

# that's because our variables have different types of data in them, so for example

testString = "10"

# is a string, so basically text, and if we try to compare the two

if test == testString:
    print("they are equal")

# we can see that they are in fact, not equal, and that's because of the types.

# it may seem odd on the surface but is actually perfectly logical, we're effectively comparing an integer of value 10, to an array of two characters, '1' and '0'

# in fact, we can see the type of different things using the very handy `type` "function"

print(type(10))
print(type(1.01))
print(type("string"))
print(type([10, 20, 30]))
print(type(range(10)))

# as you can see, we have the integer, the float, the string, the list and the range

# they all behave in slightly different ways, but you should have a pretty decent idea of what they do by now

# using this type we can also tackle some more complicated things, like

print("-----------")

def quickFunction():
    return 0

quickerFunction = lambda x: x*0

print(type(quickFunction))
print(type(quickerFunction))
print(type(print))
print(type(1==1))
print(type((10,20)))

# or even
print("-----------")

print(type(type))



# and right here at the end, I'm going to finish it off by talking about some good practices, so basically typehinting

def ourFunction(name: str, age: int, hasBlueEyes: bool) -> list:
    return [name,age,hasBlueEyes]

print(ourFunction("MAKiT",27,True))
print(ourFunction("Science MAKiT","47",True))
print(ourFunction("Evil Wizard MAKiT",2007,False))

# which makes it easier for you to debug problems in the future