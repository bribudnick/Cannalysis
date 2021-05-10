import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtext("weed.txt", delimiter = ",")
strain = weed[:,0]
ISH = weed[:,1]
terp = weed[:,2]
grwtime = weed[:,3]
print weed.read()
plt.figure(1)
plt.plot(grwtime)
plt.plot(strain)
plt.xlabel("Grow Time of One Plant (Weeks)")
plt.ylabel("Strain Name")
plt.savefig("GrowTimesofPopularStrains.png")
plt.show()
