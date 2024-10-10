import matplotlib.pyplot as plt
import numpy as np

#Variable conditions
delt=0.01
delx=0.1

#Array Declarations
x_arr=[]
y_arr=[]
newy_arr=[]

#Figure output-name counter
figcount=0

#Initial condition
def condition(x):
    if abs(x)<0.5:
        return 1
    else:
        return 0
    

#Differencing Methods    
def upwind(array,count):
    crntpos=array[count]
    prevpos=array[count-1]
    frwdval=-((crntpos-prevpos)/delx)*delt+crntpos 
    return frwdval

def downwind(array,count):
    crntpos=array[count]
    nextpos=array[count+1]
    dwnval=-((nextpos-crntpos)/delx)*delt+crntpos
    return dwnval

def central(array,count):
    crntpos=array[count]
    nextpos=array[count+1]
    prevpos=array[count-1]
    cntrlval=-((nextpos-prevpos)/(delx*2))*delt+crntpos
    return cntrlval

def laxfriedrichs(array,count):
    crntpos=array[count]
    nextpos=array[count+1]
    prevpos=array[count-1]

    a=(0.5*(nextpos+crntpos))
    b=(0.5*(delx/delt)*(nextpos-crntpos))
    c=(0.5*(prevpos+crntpos))
    d=(0.5*(delx/delt)*(crntpos-prevpos))
    lxfdsval=-((a-b-c+d)*(delt/delx))+crntpos
    return lxfdsval


#Nested for loop-iterator
for t in np.arange(0,4.01,delt):
    count=0
    newy_arr=[]
    #newy_arr.append(0)
    for i in np.arange(-2.0,2.1,delx):
        i=round(i,1)
        
        if t==0:

            x_arr.append(i)
            y_arr.append(condition(i))

        elif t!=0 and count<41:
            if count==40:
                y_arr.append(y_arr[0])

            #print(count)

            #newy_arr.append(upwind(y_arr,count))
            #newy_arr.append(central(y_arr,count))
            newy_arr.append(laxfriedrichs(y_arr,count))
            #newy_arr.append(downwind(y_arr,count))

        count+=1

    if t!=0:
        y_arr=newy_arr

    #plt.clf()
    plt.xlim(-2,2)
    plt.ylim(0,1.1)
    plt.xlabel('X-axis:(Position)')
    plt.ylabel('Y-axis:(Rho)')
    plt.plot(x_arr,y_arr, label = "Laxfriedrichs")
    plt.legend()
    #figcount+=1
    #plt.savefig("Laxfriedrichs%.3d.png"%(figcount))      

     
plt.show()  