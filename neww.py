import numpy as np
import matplotlib.pyplot as plt

circular = True

t, dt = np.linspace(0., 100., 1000, endpoint=True, retstep=True)

px = np.zeros(len(t))
py = np.zeros(len(t))
vx = np.zeros(len(t))
vy = np.zeros(len(t))

px[0] = 1.
py[0] = 0.
vx[0] = 0.
if circular:
	vy[0] = np.sqrt(1/(px[0]**2+px[1]**2))
else:
	vy[0] = 0.75

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()


for i in range(len(t) - 1):
	curr_px = px[i]
	curr_py = py[i]
	curr_vx = vx[i]
	curr_vy = vy[i]

	r = np.sqrt(curr_px**2 + curr_py**2) 
	px_dot = curr_vx
	py_dot = curr_vy
	vx_dot = -curr_px / r**3
	vy_dot = -curr_py / r**3

	px[i + 1] = px[i] + dt * px_dot
	py[i + 1] = py[i] + dt * py_dot
	vx[i + 1] = vx[i] + dt * vx_dot
	vy[i + 1] = vy[i] + dt * vy_dot

ener = 0.5 * (vx**2 + vy**2) - 1. / np.sqrt(px**2 + py**2)

ax1.plot(px, py, label="rk1")
ax2.plot(t, ener, label="rk1")

for i in range(len(t) - 1):
	curr_px = px[i]
	curr_py = py[i]
	curr_vx = vx[i]
	curr_vy = vy[i]

	r = np.sqrt(curr_px**2 + curr_py**2) 
	px_k1 = curr_vx
	py_k1 = curr_vy
	vx_k1 = -curr_px / r**3
	vy_k1 = -curr_py / r**3

	curr_px = px[i] + dt * px_k1
	curr_py = py[i] + dt * py_k1
	curr_vx = vx[i] + dt * vx_k1
	curr_vy = vy[i] + dt * vy_k1

	r = np.sqrt(curr_px**2 + curr_py**2) 
	px_k2 = curr_vx
	py_k2 = curr_vy
	vx_k2 = -curr_px / r**3
	vy_k2 = -curr_py / r**3

	px[i + 1] = px[i] + 0.5 * dt * (px_k1 + px_k2)
	py[i + 1] = py[i] + 0.5 * dt * (py_k1 + py_k2)
	vx[i + 1] = vx[i] + 0.5 * dt * (vx_k1 + vx_k2)
	vy[i + 1] = vy[i] + 0.5 * dt * (vy_k1 + vy_k2)

ener = 0.5 * (vx**2 + vy**2) - 1. / np.sqrt(px**2 + py**2)
# ax1.plot(px, py, label="rk2")
# ax2.plot(t, ener, label="rk2")

for i in range(len(t) - 1):
	curr_px = px[i]
	curr_py = py[i]
	curr_vx = vx[i]
	curr_vy = vy[i]

	r = np.sqrt(curr_px**2 + curr_py**2) 
	px_k1 = curr_vx
	py_k1 = curr_vy
	vx_k1 = -curr_px / r**3
	vy_k1 = -curr_py / r**3


	curr_px = px[i] + 0.5 * dt * px_k1
	curr_py = py[i] + 0.5 * dt * py_k1
	curr_vx = vx[i] + 0.5 * dt * vx_k1
	curr_vy = vy[i] + 0.5 * dt * vy_k1

	r = np.sqrt(curr_px**2 + curr_py**2) 
	px_k2 = curr_vx
	py_k2 = curr_vy
	vx_k2 = -curr_px / r**3
	vy_k2 = -curr_py / r**3


	curr_px = px[i] + 0.5 * dt * px_k2
	curr_py = py[i] + 0.5 * dt * py_k2
	curr_vx = vx[i] + 0.5 * dt * vx_k2
	curr_vy = vy[i] + 0.5 * dt * vy_k2

	r = np.sqrt(curr_px**2 + curr_py**2) 
	px_k3 = curr_vx
	py_k3 = curr_vy
	vx_k3 = -curr_px / r**3
	vy_k3 = -curr_py / r**3


	curr_px = px[i] + dt * px_k3
	curr_py = py[i] + dt * py_k3
	curr_vx = vx[i] + dt * vx_k3
	curr_vy = vy[i] + dt * vy_k3

	r = np.sqrt(curr_px**2 + curr_py**2) 
	px_k4 = curr_vx
	py_k4 = curr_vy
	vx_k4 = -curr_px / r**3
	vy_k4 = -curr_py / r**3

	px[i + 1] = px[i] + dt / 6. * (px_k1 + 2. * px_k2 + 2. * px_k3 + px_k4)
	py[i + 1] = py[i] + dt / 6. * (py_k1 + 2. * py_k2 + 2. * py_k3 + py_k4)
	vx[i + 1] = vx[i] + dt / 6. * (vx_k1 + 2. * vx_k2 + 2. * vx_k3 + vx_k4)
	vy[i + 1] = vy[i] + dt / 6. * (vy_k1 + 2. * vy_k2 + 2. * vy_k3 + vy_k4)

ener = 0.5 * (vx**2 + vy**2) - 1. / np.sqrt(px**2 + py**2)
ax1.plot(px, py, label="rk4")
ax2.plot(t, ener, label="rk4")

for i in range(len(t) - 1):
	r = np.sqrt(px[i]**2 + py[i]**2) 
	vx_k1 = -px[i] / r**3
	vy_k1 = -py[i] / r**3

	px[i + 1] = px[i] + dt * vx[i] + 0.5 * dt**2 * vx_k1
	py[i + 1] = py[i] + dt * vy[i] + 0.5 * dt**2 * vy_k1

	r = np.sqrt(px[i + 1]**2 + py[i + 1]**2) 
	vx_k2 = -px[i + 1] / r**3
	vy_k2 = -py[i + 1] / r**3

	vx[i + 1] = vx[i] + 0.5 * dt * (vx_k1 + vx_k2) 
	vy[i + 1] = vy[i] + 0.5 * dt * (vy_k1 + vy_k2) 

ener = 0.5 * (vx**2 + vy**2) - 1. / np.sqrt(px**2 + py**2)
ax1.plot(px, py, label="leapfrog")
ax2.plot(t, ener, label="leapfrog")


if circular:
	ax1.set_title('Circular Orbit Integration')
else:
	ax1.set_title('Elliptical Orbit Integration')
ax1.set_xlabel('time')
ax2.set_ylabel('energy')

ax1.legend()
ax2.legend()
plt.show()