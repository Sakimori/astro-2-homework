import numpy as np
import matplotlib.pyplot as plt

kpcRange = (0,15)
kpcStep = 0.25
stepCount = int(kpcRange[1]/kpcStep)

solarR = 8.2 #kpc
solarTheta = 235 #km/s

distanceArray = np.linspace(kpcRange[0], kpcRange[1], num=stepCount, endpoint=True)

def radius(distance): #kpc
    return np.sqrt(distance**2 + 8.2**2 - 8.2*np.sqrt(2)*distance)

def radialVelocity(rad): #km/s
    return solarTheta * (1/rad - 1/solarR) * solarR * np.sqrt(2)/2

#table rows: distance[0], calculated radius[1], radial velocity[2]
velocities = []
radV_r = []

for d in distanceArray:
    rad = radius(d)
    v_r = radialVelocity(rad)
    radV_r.append((rad, v_r))
    velocities.append(v_r)

fig, ax = plt.subplots()
ax.plot(distanceArray, velocities)
ax.set_xlabel("Distance (kpc)")
ax.set_ylabel("Radial Velocity (km/s)")
ax.grid()

plt.show()

with open("table.txt", "+w") as tableFile:
    tableFile.write("D (kpc); R (kpc); V_r (km/s)\n")
    for d in range(len(distanceArray)):
        dString = str(round(distanceArray[d],3)).ljust(6)
        rad, v_r = radV_r[d]
        rString = str(round(rad,3)).ljust(6)
        vString = str(round(v_r,3))
        tableFile.write(f"{dString}| {rString}| {vString}\n")