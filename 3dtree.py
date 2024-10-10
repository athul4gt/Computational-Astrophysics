import numpy as np
import matplotlib.pyplot as plt
import time


#########################################Part-4

# number of particles
N =  100


# define radius between 1 and 3
rho = np.random.rand(N) * 2 + 1

# define theta angle between 0 and 2pi
theta = np.random.rand(N) * 2 * np.pi

phi = np.random.rand(N) * 2 * np.pi


boundedness = np.random.rand(N) * 1

# calculate x and y coordinates
x = rho * np.sin(phi) * np.cos(theta)
y = rho * np.sin(phi) * np.sin(theta)
z = rho * np.cos(phi)

vx = np.sqrt(1/rho) * (-np.cos(phi)) * np.sin(theta) * boundedness
vy = np.sqrt(1/rho) * (np.cos(phi)) * np.cos(theta) * boundedness
vz = np.sqrt(1/rho) * (np.sin(phi)) * boundedness

child_start = np.zeros(8 * N, dtype=int)
comx      = np.zeros(8 * N)
comy      = np.zeros(8 * N)
comz      = np.zeros(8 * N)
centerx   = np.zeros(8 * N)
centery   = np.zeros(8 * N)
centerz   = np.zeros(8 * N)
size      = np.zeros(8 * N)
mass      = np.zeros(8 * N)
insert_pivot = 1


xpos_strg=[]
ypos_strg=[]
zpos_strg=[]
xvel_strg=[]
yvel_strg=[]
zvel_strg=[]



dependencies = []
for count in range(10 * N):
	dependencies.append([])

#print(dependencies)

figcount = 0

def create_tree():
	global insert_pivot
	insert_pivot = 1

	# reset everything
	comx.fill(0.)
	comy.fill(0.)
	comz.fill(0.)
	centerx.fill(0.)
	centery.fill(0.)
	centerz.fill(0.)
	size.fill(0.)
	mass.fill(0.)
	child_start.fill(0)

	
	tree_creation_start_time = time.time()

	# infer the tree extent by calulcating an axis aligned boundary box
	minx, maxx = np.min(x), np.max(x)
	miny, maxy = np.min(y), np.max(y)
	minz, maxz = np.min(z), np.max(z)

	# create root node
	centerx[0] = (maxx + minx) / 2
	centery[0] = (maxy + miny) / 2
	centerz[0] = (maxz + minz) / 2
	size[0]    = np.max([maxx - minx, maxy - miny, maxz - minz])

	for i in range(N):
		current_node = 0

		px = x[i]
		py = y[i]
		pz = z[i]

		while True:
			if mass[current_node] == 0:
				# no particle is occupying this leaf; nice!
				# we insert this particle into this node and jump directly to the next particle
				comx[current_node] = px
				comy[current_node] = py
				comz[current_node] = pz
				mass[current_node] = 1/N
				break
			
			elif mass[current_node] == 1/N:
				# this is a leaf, as only one particle is occupying it
				child_start[current_node] = insert_pivot + 0
				
				# -> generate the next four nodes (could be simplified to a loop, but more instructive like this)

				# lower left front
				centerx[insert_pivot + 0] = centerx[current_node] - size[current_node] / 4
				centery[insert_pivot + 0] = centery[current_node] - size[current_node] / 4
				centerz[insert_pivot + 0] = centerz[current_node] - size[current_node] / 4
				size[insert_pivot + 0] = size[current_node] / 2

				# lower right front
				centerx[insert_pivot + 1] = centerx[current_node] + size[current_node] / 4
				centery[insert_pivot + 1] = centery[current_node] - size[current_node] / 4
				centerz[insert_pivot + 1] = centerz[current_node] - size[current_node] / 4
				size[insert_pivot + 1] = size[current_node] / 2

				# upper left front
				centerx[insert_pivot + 2] = centerx[current_node] - size[current_node] / 4
				centery[insert_pivot + 2] = centery[current_node] + size[current_node] / 4
				centerz[insert_pivot + 2] = centerz[current_node] - size[current_node] / 4
				size[insert_pivot + 2] = size[current_node] / 2

				# upper right front
				centerx[insert_pivot + 3] = centerx[current_node] + size[current_node] / 4
				centery[insert_pivot + 3] = centery[current_node] + size[current_node] / 4
				centerz[insert_pivot + 3] = centerz[current_node] - size[current_node] / 4
				size[insert_pivot + 3] = size[current_node] / 2

				# lower left back
				centerx[insert_pivot + 4] = centerx[current_node] - size[current_node] / 4
				centery[insert_pivot + 4] = centery[current_node] - size[current_node] / 4
				centerz[insert_pivot + 4] = centerz[current_node] + size[current_node] / 4
				size[insert_pivot + 4] = size[current_node] / 2

				# lower right back
				centerx[insert_pivot + 5] = centerx[current_node] + size[current_node] / 4
				centery[insert_pivot + 5] = centery[current_node] - size[current_node] / 4
				centerz[insert_pivot + 5] = centerz[current_node] + size[current_node] / 4
				size[insert_pivot + 5] = size[current_node] / 2

				# upper left back
				centerx[insert_pivot + 6] = centerx[current_node] - size[current_node] / 4
				centery[insert_pivot + 6] = centery[current_node] + size[current_node] / 4
				centerz[insert_pivot + 6] = centerz[current_node] + size[current_node] / 4
				size[insert_pivot + 6] = size[current_node] / 2

				# upper right back
				centerx[insert_pivot + 7] = centerx[current_node] + size[current_node] / 4
				centery[insert_pivot + 7] = centery[current_node] + size[current_node] / 4
				centerz[insert_pivot + 7] = centerz[current_node] + size[current_node] / 4
				size[insert_pivot + 7] = size[current_node] / 2

				# we have to move the particle that created the parent node
				# to one of the new nodes
				old_px = comx[current_node]
				old_py = comy[current_node]
				old_pz = comz[current_node]

				# determine the child node that contains the old particle
				# these two lines determine the child node id between 0 and 3
				old_child_id  = int(old_pz > centerz[current_node]) * 4
				old_child_id += int(old_py > centery[current_node]) * 2 
				old_child_id += int(old_px > centerx[current_node])

				mass[insert_pivot + old_child_id] = 1/N
				comx[insert_pivot + old_child_id] = old_px
				comy[insert_pivot + old_child_id] = old_py
				comz[insert_pivot + old_child_id] = old_pz
				
				# go to the next node to update
				# increase the insert pivot by 4, as we just inserted 4 new nodes
				pivot=insert_pivot
				insert_pivot += 8

			# here the only possibility left is to climb down on the tree

			# but first add this particle to this node c.o.m. and mass 
			# -> this makes sure all particles are assigned to the higher-level node, not just one
			comx[current_node] += px
			comy[current_node] += py
			comz[current_node] += pz
			mass[current_node] += 1/N

			for v in range(8):
				if current_node>len(dependencies):
					print(current_node)

				dependencies[current_node].append(pivot + v)
				# print(current_node,mass[current_node])
				#print(dependencies[current_node][v])

			# we select the child node that contains our current particle
			child_id  = int(pz > centerz[current_node]) * 4
			child_id += int(py > centery[current_node]) * 2
			child_id += int(px > centerx[current_node])

			current_node = child_start[current_node] + child_id
			
	# calculate the final center of mass for all nodes that have particles in them
	for current_node in range(insert_pivot):
		if mass[current_node] != 0:
			comx[current_node] /= mass[current_node] 
			comy[current_node] /= mass[current_node]
			comz[current_node] /= mass[current_node] 

	print("tree creation took {}s".format(time.time() - tree_creation_start_time))
	#print(insert_pivot)
	#print(dependencies)


def plot_tree():

	global figcount

	ax = plt.axes(projection='3d')
	#fig = plt.figure(figsize=(8, 8))
	for k in range(insert_pivot):
		lef = centerx[k] - size[k] / 2
		rig = centerx[k] + size[k] / 2
		bot = centery[k] - size[k] / 2
		top = centery[k] + size[k] / 2
		fwd = centerz[k] + size[k] / 2
		bck = centerz[k] - size[k] / 2
		ax.plot3D([lef, lef, rig, rig, lef, lef, lef, lef, lef, rig, rig, rig, rig, rig, rig, lef], [bot, top, top, bot, bot, bot, top, top, top, top, top, top, bot, bot, bot, bot], [fwd, fwd, fwd, fwd, fwd, bck, bck, fwd, bck, bck, fwd, bck, bck, fwd, bck, bck], color="Black")
		figcount+=1

		#plt.savefig("Box%.4d.png"%(figcount))
	
	ax.scatter3D(x, y, z)
	# plt.xlabel("x")
	# plt.ylabel("y")

	ax.set_xlabel('X-Axis')
	ax.set_ylabel('Y-Axis')
	ax.set_zlabel('Z-Axis')

	plt.title(f'Octa-tree of {N} particles')
	plt.show()

# def check_tree():
#     for current_node in range(insert_pivot):
#         # Check if node's mass is equal to sum of children's masses
#         if mass[current_node] > 1/N:  # Only non-leaf nodes have children
#             children_mass = (sum(mass[child_start[current_node] + i] for i in range(8)))
#             if mass[current_node] != children_mass:
#                 print(f"Error: Mass of node {current_node} does not equal sum of children's masses.")
#                 return False


    # print("Tree is valid.")
    # return True

create_tree()
#check_tree()
#print(dependencies)


#########################################Part-5

def g(M,R,C):
	return -((M) * C) / R**3


arr=[]

for digit in range(insert_pivot):
	arr.append(digit)


accx=np.zeros(N)
accy=np.zeros(N)
accz=np.zeros(N)


st1=time.time()


for i in range(N): #Particle loop

	newarr=arr
	a_x=np.zeros(insert_pivot)
	a_y=np.zeros(insert_pivot)
	a_z=np.zeros(insert_pivot)

	for j in newarr: #node loop
		distance=np.sqrt((comx[j]-x[i])**2+(comy[j]-y[i])**2+(comz[j]-z[i])**2)

		if distance==0:
			#print("Pivot== ",j,"object")
			pass

		elif mass[j]==1/N and size[j]/distance > 0.4:

			#print("Pivot== ",j,"single-near")
			a_x[j]=g(mass[j],distance,comx[j]-x[i])
			a_y[j]=g(mass[j],distance,comy[j]-y[i])
			a_z[j]=g(mass[j],distance,comz[j]-z[i])


		elif mass[j]==1/N and size[j]/distance < 0.4:
			#print("Pivot== ",j,"single-far")
			a_x[j]=g(mass[j],distance,comx[j]-x[i])
			a_y[j]=g(mass[j],distance,comy[j]-y[i])
			a_z[j]=g(mass[j],distance,comz[j]-z[i])


		elif mass[j]>1/N and size[j]/distance > 0.4:
			#print("Pivot== ",j,"split")
			pass
			

		elif mass[j]>1/N and size[j]/distance < 0.4:
			#print("Pivot== ",j,"4")
			a_x[j]=g(mass[j],distance,comx[j]-x[i])
			a_y[j]=g(mass[j],distance,comy[j]-y[i])
			a_z[j]=g(mass[j],distance,comz[j]-z[i])

			for val in dependencies[j]:
				if val in newarr:
					newarr.remove(val)
					#print(len(newarr))

		else:
			#print("Pivot== ",j,"empty")
			pass
		#print(len(newarr))
	
	accx[i]=sum(a_x)/len(a_x)
	accy[i]=sum(a_y)/len(a_y)
	accz[i]=sum(a_z)/len(a_z)



st2=time.time()-st1

	





plot_tree()





accx2=np.zeros(N)
accy2=np.zeros(N)
accz2=np.zeros(N)


st3=time.time()
for i in range(N): # particle loop

	a_x2=np.zeros(N)
	a_y2=np.zeros(N)
	a_z2=np.zeros(N)



	for j in range(N): #particle loop
		distance=np.sqrt((x[j]-x[i])**2+(y[j]-y[i])**2+(z[j]-z[i])**2)
		if distance==0:
			a_x2[j]=0
			a_y2[j]=0
			a_z2[j]=0
			
		else:
			a_x2[j]=g(1/N,distance,x[j]-x[i])
			a_y2[j]=g(1/N,distance,y[j]-y[i])
			a_z2[j]=g(1/N,distance,z[j]-z[i])
			#print(a_x2[j])
	
	accx2[i]=sum(a_x2)/len(a_x2)
	accy2[i]=sum(a_y2)/len(a_y2)
	accz2[i]=sum(a_z2)/len(a_z2)


st4=time.time()-st3


#print(accx)
#print(accx2)

error=abs((accx-accx2))/abs(accx2)

#print(error)

rarr=[]

for i in range(N):
	rarr.append(i)

plt.clf()

plt.plot(rarr, error)

plt.show()
print(st2,st4)

ax = plt.axes(projection='3d')

dt=0.01


#plt.clf()


#########################################Part-6

for i in range(N):

    t=0
    count=0

    while(t<=1):
        if t==0:

            ax.scatter3D(x[i],y[i],z[i])
 
            xpos_strg.append(x[i])
            ypos_strg.append(y[i])
            zpos_strg.append(z[i])

            xvel_strg.append(vx[i])
            yvel_strg.append(vy[i])
            zvel_strg.append(vz[i])
        
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

plt.show()




############################################################Comments################################

#Tree algorithm is faster for 1e5 or more particle

#Error rate is found to 100% for lower N and appoaches 0% as N is made larger

#Note part 6 is direct summation and not tree acceleration