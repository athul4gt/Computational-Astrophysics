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


def ftcs(currentpos, nextpos, prevpos, delt, delx_val):

    nextval=currentpos+(nextpos-2*currentpos+prevpos)*(delt/(delx_val**2))

    return nextval

#Main-body
for cellcount in cellcounts:
    
    midpoint_val, delx_val = cells(cellcount)
    t=0
    x_arr=[]

    while (t<=maxtime):

        count=0
        y_arr=[]

        for i in np.arange(-1,1,delx_val):
            
            if t==0:
                    
                x_arr.append(i)
                y_arr.append(initplt(count, midpoint_val, delx_val))

            elif t!=0 and count==0:

                y_arr.append(ftcs(str_y_arr[0], str_y_arr[1], str_y_arr[-1], delt, delx_val))

            elif t!=0 and count==cellcount-1:

                y_arr.append(ftcs(str_y_arr[cellcount-1], str_y_arr[0], str_y_arr[cellcount-2], delt, delx_val))

            else: 

                y_arr.append(ftcs(str_y_arr[count], str_y_arr[count+1], str_y_arr[count-1], delt, delx_val))

            count+=1
            
        str_y_arr=y_arr

        #delt = 90% of the delx-condtion
        delt= (delx_val**2/2)*0.9
        t = t + delt

        if t>maxtime:

            plt.plot(x_arr,y_arr,label="Line for Grid of %i"%(cellcount))
            break



#Plot-section    
plt.xlabel("Position-X")
plt.ylabel("Quantity-Y")
plt.title("1D-Diffusion Equation-FTCS")
plt.legend(loc="upper right")
plt.show()


