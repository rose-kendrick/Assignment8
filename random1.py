import numpy as np
from matplotlib import pyplot as pp
import random 


nsteps = int(input('Give a number of steps: '))
nwalkers = 1

for walker in range(nwalkers):
    
    x = [0]
    steps = [0]
    for step in range(nsteps):
        x.append(x[-1]+random.randint(-1,1))
        steps.append(step+1)
    
    pp.plot(steps,x)
    pp.xlabel('Step Number')
    pp.ylabel('Position (m)')
    pp.savefig('randomwalk2.png')
    # pp.show()
