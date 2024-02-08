import numpy as np
import matplotlib.pyplot as plt

solarR = 8.2 #kpc
solarTheta = 235 #km/s

radArray = [4,6,10,12] #kpc


def radialVelocity(long, rad): #long in degrees, galactocentric radius in kpc, km/s
    return solarTheta * (1/rad - 1/solarR) * solarR * np.sin(np.deg2rad(long))

fig, ax = plt.subplots()
styles = ["-b", "-g", "-y", "-r"]
for i in range(len(radArray)):
    if radArray[i] > solarR: #Outer galactic, visible in full sky
        longArray = np.linspace(-180, 180, endpoint=True, num = 360)    
    else: #Inner galactic, longitude is limited
        maxL = np.rad2deg(np.arcsin(radArray[i]/solarR))
        longArray = np.linspace(-maxL, maxL, endpoint=True, num = int(2*maxL))
    thisLine, = ax.plot(longArray, [radialVelocity(l, radArray[i]) for l in longArray], styles[i])
    thisLine.set_label(f"R = {radArray[i]} kpc")

ax.set_xlabel("Galactic Longitude")
ax.set_ylabel("V_r (km/s)")
ax.invert_xaxis()
ax.legend()
plt.show()