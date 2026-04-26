# First we start by importing a library for plotting mathematics, and you won't believe what it's called
import matplotlib.pyplot as plt

# this allows us to create graphs of different values using the following lines of code

# plt.plot([1, 2, 3, 4])
# plt.show()

# where the first line creates a plot, and the second shows the graph

# now knowing how we can create a graph, we can begin our fun, by defining the values

x = 3 # sphere will begin three metres off the floor
v = 2 # with a velocity of going upwards two metres per second
m = 1 # mass of our sphere
GRAVITATIONAL_ACCELERATION = -9.81 # Gravitational constant will not change, so we're definiting it in capital letters, which makes it a constant

RADIUS = 1

TIME = 10 # for how many seconds we'd like our simulation to run
SAMPLES = 10 # how many times would we like to simulate our physics per second

t = 0 # the index of our time, a SAMPLES added to t should be equivalent to one second passing

datax = [] # the place where we'll store all the data relating to position
datav = [] # the place where we'll store all the data relating to velocity

# the main loop where all the simulations will happen
while t < TIME*SAMPLES:
    v += GRAVITATIONAL_ACCELERATION/SAMPLES # we modify our velocity based on the acceleration the sphere is experiencing
    x += v/SAMPLES # we modify our position based on the velocity the sphere is experiencing

    if x < RADIUS:
        # right here, once the position of the sphere to the floor gets smaller than the radius of the sphere
        # this means that our sphere has collided with the floor, so we stop it by setting its velocity to 0, and keeping its position constant
        v = 0
        x = RADIUS

        break # we can also "break" the loop (meaning just stop) in order to save time, since we know nothing will happen from now on

    datax.append(x)
    datav.append(v)
    t += 1


    
plt.plot(datax, color='orange')
plt.plot(datav, color='green')
plt.show()