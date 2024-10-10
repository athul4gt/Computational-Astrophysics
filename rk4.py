import matplotlib.pyplot as plt
import numpy as np


# Constants

G = 1
dt = 0.1
m = 1
M = 10

# Radius
def radius(x,y):
        val=((x**2)+(y**2))**0.5
        return val


# Initial Conditions
x = 1
y = 0
t = 0

x_vel= 0
y_vel = np.sqrt(G*M/radius(x,y))



# Arrays

t_array = []
x_array = []
y_array = []

def dydx(x, y):
    der =-1.*G*M*(x/r**3)
    return der


def dydxy(x, y):
    der =-1.*G*M*(y/r**3)
    return der
    
    

def x_velf(x, y):
    return x_vel
    
    
    
def y_velf(x, y):
    return y_vel



#Rungekutta

def RungeKutta(x, y, dx, dydx):
    
    # Calculate slopes
    k1 = dx*dydx(x, y)
    k2 = dx*dydx(x+dx/2., y+k1/2.)
    k3 = dx*dydx(x+dx/2., y+k2/2.)
    k4 = dx*dydx(x+dx, y+k3)
    
    # Calculate new x and y
    y = y + 1./6*(k1+2*k2+2*k3+k4)
    x = x + dx
    
    return y
    
    
def RungeKutta2(x, y, dx, dydx):
    
    # Calculate slopes
    k1 = dx*dydx(x, y)
    k2 = dx*dydx(x+dx/2., y+k1/2.)
    k3 = dx*dydx(x+dx/2., y+k2/2.)
    k4 = dx*dydx(x+dx, y+k3)
    
    # Calculate new x and y
    y_new = y + 1./6*(k1+2*k2+2*k3+k4)
    x = x + dx
    
    return y_new
    




while (t<=100):
    r= radius(x,y)
    x_acc = -1.*G*M*(x/r**3)
    x_vel = RungeKutta(t, x_vel, dt, dydx)
    x = RungeKutta2(t, x, dt, x_velf)
    
    y_acc = -1.*G*M*(y/r**3)
    y_vel = RungeKutta(t, y_vel, dt, dydxy)
    y = RungeKutta2(t, y, dt, y_velf)
    
    
    r+= radius(x,y)    
    t = t + dt
    t_array.append(t)
    x_array.append(x)
    y_array.append(y)



plt.xlabel("x-coordinates")
plt.ylabel("y-coordinates")
plt.plot (x_array, y_array)
plt.legend (["Orbit"])
plt.show()
