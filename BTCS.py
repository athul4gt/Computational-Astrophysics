import numpy as np
import matplotlib.pyplot as plt

#Declarations
cellcounts=[100, 200, 400]
maxtime=0.25


#Functions
def cells(cellcount):

    midpoint=cellcount/2

    delx=2/cellcount

    return midpoint, delx


def initplt(count, midpoint_val, delx_val):
    
    if count<midpoint_val-1 or count>midpoint_val:

        val=0

    else:
        
        val=1/(2*delx_val)

    return val


#Main-body
for cellcount in cellcounts:

    t=0
    x_arr=[]
    y_arr=[]

    midpoint_val, delx_val = cells(cellcount)

    #Array-Creation-Declarations

    A=np.zeros([cellcount,cellcount])

    #delt = 90% of the delx-condtion
    delt=(delx_val)*0.9

    D=delt/delx_val**2

    np.fill_diagonal(A,1+2*D)

    y=np.zeros(cellcount-1)
    y[:]=-D

    A[np.arange(cellcount-1),np.arange(cellcount-1)+1]=y    
    A[np.arange(1,cellcount),np.arange(cellcount-1)]=y

        
    while t<=maxtime:

        count=0
        
        if t==0:

            for i in np.arange(-1,1,delx_val):   

                x_arr.append(i)
                y_arr.append(initplt(count, midpoint_val, delx_val))

                count+=1
            
        else:

            B=y_arr
            C=np.linalg.solve(A,B)
            y_arr=C

        t = t + delt

        if t>maxtime:

            plt.plot(x_arr,y_arr,label="Line for Grid of %i"%(cellcount))
            break

#Plot-section    
plt.xlabel("Position-X")
plt.ylabel("Quantity-Y")
plt.title("1D-Diffusion Equation-BTCS")
plt.legend(loc="upper right")
plt.show()