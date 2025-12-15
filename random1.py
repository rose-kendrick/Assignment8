import numpy as np
from matplotlib import pyplot as pp
import random 


nsteps = int(input('Give a number of steps: '))
nwalkers = 500
x_finals = []

for walker in range(nwalkers):
    
    x = [0]
    steps = [0]
    for step in range(nsteps):
        x.append(x[-1]+random.randint(-1,1))
        steps.append(step+1)

    x_finals.append(x[-1])
    
    pp.plot(steps,x)

pp.xlabel('Step Number')
pp.ylabel('Position (m)')
pp.savefig('randomwalk500.png')
# pp.show()

x_finals_sum = sum(x_finals)
x_n = x_finals_sum/nwalkers
x_n2 = x_n**2
print(x_n,x_n2)

