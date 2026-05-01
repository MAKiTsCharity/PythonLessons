# Let's say that we'd like to create our own system of particle physics.
# In that scenario we can start by defining a particle, this particle will contain quite a lot of information, so ideally we'd like to define it with a class, to MAKiT easier in the future

import math
import numpy as np # this is just for the sake of convenience
import matplotlib.pyplot as plt # and this is for the sake of visualising

class particle:
    def __init__(self, penergy: float, position: tuple, radius: float, findex: int):
        self.penergy = penergy # the energy state of our particle
        self.position = position # the position of our particle
        self.radius = radius # scale of our wavefunction
        self.findex = findex # which field should it interact with, the index of that field

    def evaluateWaveFunction(self, r: float) -> float:
        return 1/r * math.cos(r) * self.radius * math.e**(-r**2/self.penergy**3)

# with the same idea in mind, we could create the concept of a field, which would just be a different tool with the same idea in mind


class field:
    def __init__(self, findex: int, particles: list):
        self.findex = findex # the index of our field
        self.particles = particles # the particles of our field

    def evaluateField(self, coordinates: tuple) -> float:
        totField = 0
        for particle in self.particles: # looping over all particles

            if particle.findex != self.findex: # if the particle doesn't interact with our field, we skip it
                continue

            distance = 0 # we calculate the distance
            for i in range(len(coordinates)):
                distance += (coordinates[i]-particle.position[i])**2
            distance**(1/2)

            totField += particle.evaluateWaveFunction(distance) # we sum its effect on the field
        
        return totField

# and after the creation of these two concepts, we can put them in practice

p0 = particle(5, [1,2,3],3,0)
p1 = particle(7, [1,1,1],3,0)
p2 = particle(10, [-1,0,0],4,0)

f = field(0,[p0,p1,p2])



t = np.arange(-3, 1, 0.01)

plt.plot(t, [f.evaluateField((x,0,1)) for x in t]) # here we specify we'd like to graph the field along the x axis, at y=0, z=1
plt.grid(True)
plt.show() # and we just show