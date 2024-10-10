import matplotlib.pyplot as plt

import numpy as np

#from tqdm import tqdm

###############DECLARATIONS###############

delx=0.0025 #1/cellcount, where cellcount =400

cs=1

cfl=0.3

figcount=0

t=0

t_condition=0.15

x_arr=[]

rho_arr=[]

rho_u_arr=[]

U_arr=[]

F_arr=[]

plotter=[]

u_temp=[]


###################FUNCTIONS##############

def initval(x):

    if x<.5:

        rho=1


    elif x>=.5:

        rho=0.125

    rho_u=0

    return rho, rho_u


def delt(maxu):

    return cfl*delx/(maxu+cs)


def F_halfth(nextpos_F,current_F,nextpos_U,current_U,a_val):

    rtn1=(nextpos_F[0]+current_F[0])/2-(a_val/2)*(nextpos_U[0]-current_U[0])

    rtn2=(nextpos_F[1]+current_F[1])/2-(a_val/2)*(nextpos_U[1]-current_U[1])

    return rtn1, rtn2


def next_U(U_arr_temp,delt_val,plushalfth1,plushalfth2,minushalfth1,minushalfth2,i):
    
    rtn1= U_arr_temp[i][0]-(plushalfth1-minushalfth1)*(delt_val/delx)

    rtn2= U_arr_temp[i][1]-(plushalfth2-minushalfth2)*(delt_val/delx)

    return rtn1, rtn2



#################LOOP#####################

while t<=t_condition:

    i=0
    
    U_arr=[]
    
    F_arr=[]
    
    u_temp=[]

    plotter=[]

    for x in np.linspace(-0.0025,1.0025,402):

        x=round(x,4)
        
        if t==0:

            x_arr.append(x)
            rho, rho_u =initval(x)
    

        elif t!=0 and i==0:

            rho=U_arr_temp[i+1][0]
            rho_u=-U_arr_temp[i+1][1]


            a_val=max(new_u_temp[i+1],new_u_temp[i])+cs

            minushalfth1, minushalfth2 =F_halfth(F_arr_temp[i+1],F_arr_temp[i],U_arr_temp[i+1],U_arr_temp[i],a_val)


        elif t!=0 and i==401:

            rho=U_arr_temp[i-1][0]
            rho_u=-U_arr_temp[i-1][1]


        else:

            a_val=max(new_u_temp[i+1],new_u_temp[i])+cs

            plushalfth1, plushalfth2=F_halfth(F_arr_temp[i+1],F_arr_temp[i],U_arr_temp[i+1],U_arr_temp[i],a_val)
            
            rho, rho_u =next_U(U_arr_temp,delt_val,plushalfth1,plushalfth2,minushalfth1,minushalfth2,i)


            minushalfth1=plushalfth1
            minushalfth2=plushalfth2


        U_arr.append([])
        U_arr[i].append(rho)
        U_arr[i].append(rho_u)
        

        u_temp.append(abs(U_arr[i][1]/U_arr[i][0]))


        F_arr.append([])
        F_arr[i].append(rho_u)
        F_arr[i].append(rho*((u_temp[i]**2)+1))       

        
        i+=1
        plotter.append(rho)

    #Array Updates
    new_u_temp=u_temp


    U_arr_temp=U_arr
    F_arr_temp=F_arr

    #Time Updates
    maxu=max(u_temp)
    delt_val=delt(maxu)
    t=t+delt_val

    #Plot-function
    plt.clf()
    plt.xlim(-0.1,1.1)
    plt.xlabel("Position-X")
    plt.ylabel("Density-Rho")
    plt.ylim(0,1.1)
    plt.plot(x_arr,plotter,label="Density Distribution,t=0.15")


    #figcount+=1
    #plt.savefig("Iso%.4d.png"%(figcount))   


#################OUTPUT###################

plt.legend()
plt.show()

##################END#####################