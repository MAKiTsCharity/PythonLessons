# classes are an especially difficult topic to understand, but basically you can think of them as... "dictionaries with extra functionalities"... or "modules of code"

# for example, let's say you're working on some code which involves the periodic table, in that scenario you could use something to represent the concept of the atom
# and you could use dictionaries for that

Hydrogen = {"name":"Hydrogen",
            "electrons":1,
            "state":"Gas"} # etc, etc

# with some convenience functions like so

def getEC(electrons): # like for example, getting the electron configuration of them (it is horribly inacurate, but it's only meant to be an example)
    ec = [[[0]]]
    curOr = 0
    curSu = 0
    curSh = 0
    while electrons:
        ec[curSh][curSu][curOr] += 1
        if ec[curSh][curSu][curOr] > 1:
            curOr += 1
            if curOr > curSu*2:
                curSu += 1
                if curSu > curSh/2+0.5:
                    curSh += 1
                    ec.append([])
                    ec[curSh].append([])
                    curSu = 0
                    ec[curSh][curSu].append(0)
                    curOr = 0
                else:
                    ec[curSh].append([])
                    ec[curSh][curSu].append(0)
                    curOr = 0
            else:
                ec[curSh][curSu].append(0)
        electrons -= 1
    return ec

print("Directory")
print(getEC(Hydrogen["electrons"]))

# this may seem like a perfectly fine approach, and it is, but we can add an unreasonable amount of functionality with classes

# So, let us create our "atom" class

class Atom:
    def __init__(self, name: str, electrons: int,sTl: float,lTg: float):
        self.name = name
        self.electrons = electrons
        self.states = [sTl,lTg]
        self.ec = getEC(electrons)

    def getState(self,temp: float): # the self there is needed, in order to access the things inside the class
        if temp < self.states[0]:
            return "solid"
        elif temp < self.states[1]:
            return "liquid"
        else:
            return "gas"
        
# which allowes us to create instances of this class

H = Atom("Hydrogen",1,-300,-300) # bit of a cheap workaround, because hydrogen is always gas
Ga = Atom("Gallium",31,29,2403)

# the reason why this is better, is because our values come pre-initialised, we can right away read the electron configuration of these atoms

print("Classes")
print(H.ec)
print(Ga.ec)
# what's more, we canuse the functions inside the class to get the state of matter of these elements at different temperatures
print("States")
print(f"at {100} Celsius, {H.name} in {H.getState(100)} form")
print(f"at {100} Celsius, {Ga.name} in {Ga.getState(100)} form")
print(f"at {10000} Celsius, {Ga.name} in {Ga.getState(10000)} form")
