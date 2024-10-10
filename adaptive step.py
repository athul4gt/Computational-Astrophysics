import matplotlib.pyplot as plt
import matplotlib


#Declare Variables

Ti=1e7         #Initial Temperature
T0=2e4	       #End-point Temperature	
lambda0=1e-22
alpha=10.0
beta=-0.5
kb=1.38*1e-16


#Declare Function for calculating Lambda

def lambdaf(T):
	if T<=T0:
		lambdat=lambda0*(T/T0)**alpha
	elif T>T0:
		lambdat=lambda0*(T/T0)**beta
	return lambdat


#Declare Function for Temperature Evolution

def eqfunc(T):
	equation= -(2/(3*1.38*1e-16))*lambdaf(T)
	return equation


#Initial Condition

T=Ti
t=0


#Declare Lists to store data

arT=[]
araT=[]
art=[]
arat=[]


#Timestep-conditons
	  #dt set as 9.7e10 as 1e10 is stable and similar to it
dt=9.7e10 #Around critical timestep beyond which the Temperature Evolution is Unstable
adt=dt

#While loop to iterate through values, condition set for time ( could be substituted with temperature )
#Multiple while statements linearly assigned for varying conditions

while(t<1e15):
	k1=eqfunc(T)
	k2=eqfunc(T+k1*dt)
	T=T+1/2*(k1+k2)*dt
	t=t+dt
	arT.append(T)
	art.append(t)
	if T<6000:
		break	



#Adaptive step-size loop
		
T=Ti
t=0	
while(t<1e15):
	strtemp=T
	k1=eqfunc(T)	
	k2=eqfunc(T+k1*adt)
	T=T+1/2*(k1+k2)*adt
	t=t+adt
	
	tempdif=strtemp-T
	if tempdif >50:
		adt=adt/2
	elif tempdif < 0.01:
		adt=adt*2

	araT.append(T)
	arat.append(t)
	if T<6000:
		break



#Plotting

print("Done")
plt.yscale("log")
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.plot(art,arT,label='Default step size')
plt.plot(arat,araT,'--',label='Adaptive step size')
plt.legend()
plt.show()

#The End
