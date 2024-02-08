import numpy as np
import matplotlib.pyplot as plt

solarR = 8.2 #kpc
solarTheta = 235 #km/s

longStep = 1
stepCount = int(360/longStep)

radArray = [4,6,10,12] #kpc
longArray = np.linspace(-180, 180, endpoint=True, num = stepCount)

def radialVelocity(long, rad): #long in degrees, galactocentric radius in kpc, km/s
    return solarTheta * (1/rad - 1/solarR) * solarR * np.sin(np.deg2rad(long))

fig, ax = plt.subplots()
styles = ["-b", "-g", "-y", "-r"]
for i in range(len(radArray)):
    thisLine, = ax.plot(longArray, [radialVelocity(l, radArray[i]) for l in longArray], styles[i])
    thisLine.set_label(f"R = {radArray[i]} kpc")

ax.set_xlabel("Galactic Longitude")
ax.set_ylabel("V_r (km/s)")

ax.legend()
plt.show()