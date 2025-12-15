import numpy as np
from matplotlib import pyplot as pp
import random 


nsteps = int(input('Give a number of steps: '))
nwalkers = 500


x_current = np.zeros((nwalkers,nsteps+1))
steps = np.arange(nsteps+1)

for walker in range(nwalkers):
    x = [0]
    x_current[walker,0] = x[0]

    for step in range(1,nsteps+1):
        x.append(x[-1] + random.randint(-1,1))
        x_current[walker,step] = x[-1]

    # x_finals.append(x[-1])
    
    pp.plot(steps,x)


mean_displacement = x_current.mean(axis=0)
mean2 = np.square(mean_displacement)


pp.xlabel('Step Number')
pp.ylabel('Position (m)')
pp.savefig('randomwalk500.png')
# pp.show()


pp.figure()
pp.plot(steps, mean2, label='mean')
pp.xlabel('Step Number')
pp.ylabel('Mean position (m)')
# pp.show()
pp.savefig('displacement.png')



