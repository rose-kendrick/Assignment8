import numpy as np
from matplotlib import pyplot as pp

# dv/dt = F/m (cyclist without drag)
# dE/dt = mv(dv/dt) (all energy is kinetic)
# P = power output 
# dv/dt = P/mv
# F_drag = -1/2*C_D*rho*A*v^2(drag force)
# C_D = drag coefficient
# F_drag,viscous = -n*A(v/h) (drag force)
# n = viscosity

def F_drag(v_i):
    F = -(1/2)*CD*rho*A*v_i**2
    return F

def F_dragV(v_i):
    F = -n*A*(v_i/h)
    return F

def dvdt(P,m,v_i,x_i):
    a = ((P/(m*v_i))+((F_drag(v_i))/m)+((F_dragV(v_i))/m)+((F_g(theta(x_i)))/m))
    return a

def theta(x): #deg
    angle = np.arctan(0.08*(0.15*np.sin(0.015*x+3)+0.6*np.sin(0.025*x+5)+0.3*np.sin(0.009*x)))
    return angle

def F_g(theta_i):
    F = m*g*np.sin(theta_i)
    return F


v0 = 4 #m/s
m = 70 #kg
P = 400 #W
dt = 0.1 #s
t0 = 0 #s
tmax = 200 #s
CD = 0.9 
A = 0.33 #m^2
rho = 1.225 #kg/m^3 density of air at standard conditions
n = 2e-5 #Pa*s
h = 2 #m
g = -9.81 #m/s


N = int(tmax/dt)+1
t = np.linspace(t0,tmax,N)
v = np.zeros(N)
v[0] = v0
x = np.zeros(N)


for i in range(N-1):
    x[i+1] = x[i]+v[i]*dt
    v[i+1] = v[i]+dvdt(P,m,v[i],x[i])*dt



pp.plot(t,v,)
pp.title('Velocity, v, as a function of time, t')
pp.xlabel(r'time, $t (s)$')
pp.ylabel(r'velocity, $v (\frac{m}{s})$')
# pp.show()
pp.savefig('bikeWithDrag3.png')