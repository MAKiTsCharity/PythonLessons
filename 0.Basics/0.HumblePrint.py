# in order to run the file `python ./0.Basics/0.HumblePrint.py`

print("test") # the prind function allowes you to print different strings

x = 7

if x==7:
    print("allowing you to see when a certain piece of code is executed")

if x==6:
    print("or when it isn't")

print(x) # or maybe just a value of some kind of variable

print(f"the value of x: {x}") # it can be used with the so called "f strings" to format a variable into the text

print(f"{5+7} is not the same as {5}+7") # in an f string, everything inside curly brackets will be executed as code, and formatted into a string, very important to keep in mind

print(":D\n:D") # but be careful of certain escape characters, for example "\n" stands for "endline", so kind of like just pressing enter on your keyboard

print(r":D\n:D") # if you'd like python to take your string literally, as is, you need to add a letter "r" on the beggning

print(rf"is {x} + {x} equal to {x*2}?{"\n"}The answer is: {x+x==x*2} \n") # and you can use all of those tricks together, to create some really descriptive prints