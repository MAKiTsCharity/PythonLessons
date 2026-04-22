# loops in python come in two main forms

something = 0

while something < 20: # the "while a condition is true" form
    print(f"{something}. iterating the while loop")
    something += 1

for i in range(something): # and the much more common "for each time in an array" form
    print(f"{i}. iterating the for loop")

certainArray = ["abc","efg","hijk","mktop"]

for arrayItem in certainArray: # in this scenario we have our array, and we loop over this array, on each iteration using different item from it to print
    print(f"current item: {arrayItem}")

# which would lead to an interesting question, does that mean that `range(x)` is an array?

# and well, let's find out

print(range(7)) # as you can see we can print the range to see what it is

# and even better, we can print specific items of that range, just like we could with any other array

print(certainArray[0])
print(range(7)[0])

print(certainArray[2])
print(range(7)[2])

print(certainArray[3])
print(range(7)[3])