import numpy as np
import matplotlib.pyplot as plt
import random


pos_arr=[]
x_arr=[]
y_arr=[]
z_arr=[]
vel_arr=[]

xpos_strg=[]
ypos_strg=[]
zpos_strg=[]
xvel_strg=[]
yvel_strg=[]
zvel_strg=[]

randlist=[-1,1]
dt=0.01

def r_generator():
    return random.uniform(10**-6,1)



def position_generator(r,limit=1):

    pos=0
    while not(pos<=-10**-6 or pos>=10**-6):
        pos=random.uniform(-limit,limit)

        if(pos<=-10**-6 or pos>=10**-6):
            return pos**2/r**2, np.sign(pos)
        
        else:
            continue

def velocity_generator(r):
    velocity=(2/r)**(1/2)
    sign=random.choice(randlist)

    x_velocity=random.uniform(-velocity,velocity)
    rng=(velocity**2-x_velocity**2)**(1/2)
    y_velocity=random.uniform(-rng,rng)
    z_velocity=((velocity**2-x_velocity**2-y_velocity**2)**(1/2))*sign

    return x_velocity,y_velocity,z_velocity
  
i=0
while(i<100): 
    r=r_generator()

    vel_arr.append([])
    vel_arr[i].append([])
    vel_arr[i].append([])
    vel_arr[i].append([])
    
    vel_arr[i][0],vel_arr[i][1],vel_arr[i][2]=velocity_generator(r)

    val,sign=position_generator(r,limit=r)
    x=((val*(r**2))**(1/2))*sign

    yval=1-val
    val,sign=position_generator(r,limit=((yval)*r**2)**(1/2))

    
    y=((val*(r**2))**(1/2))*sign

    randlist=[-1,1]
    sign=random.choice(randlist)
    z=((yval-val)*r**2)**(1/2)*sign

    pos_arr.append([])
    pos_arr[i].append(x)
    pos_arr[i].append(y)
    pos_arr[i].append(z)

    i+=1


fig = plt.figure()
ax = plt.axes(projection='3d')

for i in range(100):
    t=0
    count=0
    while(t<=1):
        if t==0:

            ax.scatter3D(pos_arr[i][0],pos_arr[i][1],pos_arr[i][2])
 
            xpos_strg.append(pos_arr[i][0])
            ypos_strg.append(pos_arr[i][1])
            zpos_strg.append(pos_arr[i][2])

            xvel_strg.append(vel_arr[i][0])
            yvel_strg.append(vel_arr[i][1])
            zvel_strg.append(vel_arr[i][2])
        
        else:
                
            r = np.sqrt(xpos_strg[count]**2 + ypos_strg[count]**2 + zpos_strg[count]**2 + 10**-6)

            acc_x=-xpos_strg[count]/r**3
            acc_y=-ypos_strg[count]/r**3
            acc_z=-zpos_strg[count]/r**3

            xpos_strg.append(xpos_strg[count] + dt*xvel_strg[count] + 0.5 * dt**2 * acc_x)
            ypos_strg.append(ypos_strg[count] + dt*yvel_strg[count] + 0.5 * dt**2 * acc_y)
            zpos_strg.append(zpos_strg[count] + dt*zvel_strg[count] + 0.5 * dt**2 * acc_z)

            r = np.sqrt(xpos_strg[count+1]**2 + ypos_strg[count+1]**2 + zpos_strg[count+1]**2 + 10**-6)

            acc_x2=-xpos_strg[count+1]/r**3
            acc_y2=-ypos_strg[count+1]/r**3
            acc_z2=-zpos_strg[count+1]/r**3

            xvel_strg.append(xvel_strg[count]+0.5*dt*(acc_x+acc_x2))
            yvel_strg.append(yvel_strg[count]+0.5*dt*(acc_y+acc_y2))
            zvel_strg.append(zvel_strg[count]+0.5*dt*(acc_z+acc_z2))

            count+=1

        ax.plot3D(xpos_strg,ypos_strg,zpos_strg)
        t+=dt

    ax.plot3D(xpos_strg,ypos_strg,zpos_strg)

    xpos_strg=[]
    ypos_strg=[]
    zpos_strg=[]
    xvel_strg=[]
    yvel_strg=[]
    zvel_strg=[]


ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-1,1)

ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')

plt.show()
