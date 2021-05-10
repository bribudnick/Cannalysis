  # Header describing the data will be placed here.
  # Strain name: name of the strain of marijuana
  # Indica/Sativa/Hybrid: Indicative of the way the plant grows; known by the
  # way the effects are felt. Sativa strains are typically more energetic, focused
  # and felt in the head, whereas indica strains are relaxing and influence the body greatly.
  # Dominant Terpene: In the most basic sense, these are what you
  # taste, smell and feel from the marijuana. Different terpenes invoke different
  # medicinal benefits and bodily/emotional feelings. While strains will have a
  # profile of terpenes, I have listed the dominant terpene for each strain.
  # Grow Time: the grow time for a plant of this strain, in weeks. 
import numpy as np
import matplotlib.pyplot as plt
comments=#
weed = np.genfromtxt("weed.txt", delimiter = ",")
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
