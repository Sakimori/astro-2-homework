import matplotlib.pyplot as plt
import matplotlib.colors as clr
import numpy as np

maxHeight = 3 #kpc
maxRadius = 25 #kpc
pixelsHeight = 300
aspectRatio = maxRadius/maxHeight

scaleHThin = 0.35 #kpc
scaleHThick = 1.00 #kpc
scaleRadius = 2.25 #kpc

zRange = np.linspace(-maxHeight, maxHeight, pixelsHeight )
zTicks = np.linspace(-maxHeight, maxHeight, 11)
radRange = np.linspace(-maxRadius, maxRadius, int(pixelsHeight*aspectRatio))
radTicks = np.linspace(-maxRadius, maxRadius, 5)

def totDensity(height, radius):
   return (np.exp(- abs(height)/scaleHThin) + .085*np.exp(- abs(height)/scaleHThick))*np.exp(- abs(radius)/scaleRadius)

def thinDensity(height, radius):
    return (np.exp(- abs(height)/scaleHThin)*np.exp(- abs(radius)/scaleRadius))

def thickDensity(height, radius):
    return (.085*np.exp(- abs(height)/scaleHThick)*np.exp(- abs(radius)/scaleRadius))


thinDensity2D = thinDensity(zRange[:, None], radRange[None, :])
thickDensity2D = thickDensity(zRange[:, None], radRange[None, :])
totDensity2D = totDensity(zRange[:, None], radRange[None, :])

densityMin = np.min(totDensity2D)
densityMax = np.max(totDensity2D)

fig, ax = plt.subplots(3)
ax[0].imshow(thinDensity2D, cmap='plasma', vmin=densityMin, vmax=densityMax)
ax[0].set_title("Thin disk")
ax[1].imshow(thickDensity2D, cmap='plasma', vmin=densityMin, vmax=densityMax)
ax[1].set_title("Thick disk")
im = ax[2].imshow(totDensity2D, cmap='plasma', vmin=densityMin, vmax=densityMax)
ax[2].set_title("Total disk")

fig.subplots_adjust(right=0.8)
cbarAx = fig.add_axes([0.85, 0.15, 0.05, 0.7])
cbar = fig.colorbar(im, cax=cbarAx)
cbar.set_label("Density (n/n_0)")

for i in range(3):
    ax[i].set_xticks([])
    ax[i].set_yticks([])
    ax[i].set_xlabel(f"R = {maxRadius} kpc")

plt.show()

plt.close()

fig, ax = plt.subplots(3)
ax[0].imshow(thinDensity2D, cmap='plasma',norm="log", vmin=densityMin, vmax=densityMax)
ax[0].set_title("Thin disk")
ax[1].imshow(thickDensity2D, cmap='plasma', norm="log", vmin=densityMin, vmax=densityMax)
ax[1].set_title("Thick disk")
im = ax[2].imshow(totDensity2D, cmap='plasma', norm="log", vmin=densityMin, vmax=densityMax)
ax[2].set_title("Total disk")

for i in range(3):
    ax[i].set_xticks([])
    ax[i].set_yticks([])

fig.subplots_adjust(right=0.8)
cbarAx = fig.add_axes([0.85, 0.15, 0.05, 0.7])
cbar = fig.colorbar(im, cax=cbarAx)
cbar.set_label("Density (n/n_0)")

plt.show()