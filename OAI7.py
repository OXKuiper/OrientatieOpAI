"""
Wat code om twee samples te nemen (bijv lengtes mannen en lengtes vrouwen)
die normaal verdeeld zijn (hebben een bekende mean en standaarddeviatie)
en deze te plotten.
"""

import numpy as np
import matplotlib.pyplot as plt

sample_size = 5000   # Aantal random gekozen 'personen'

# Eerste groep
mean_height1 = 170   # gemiddelde lengte in cm
std_deviation1 = 10  # standaarddeviatie in cm

# Tweede groep
mean_height2 = 160   # gemiddelde lengte in cm
std_deviation2 = 10  # standaarddeviatie in cm

# Sample (kies random uit de groep)
heights1 = np.random.normal(mean_height1, std_deviation1, sample_size)
heights2 = np.random.normal(mean_height2, std_deviation2, sample_size)

# Plot de verdelingen
plt.hist(heights1, bins=30, alpha=0.5, label=f'Groep 1: Mean={mean_height1}, SD={std_deviation1}')
plt.hist(heights2, bins=30, alpha=0.5, label=f'Groep 2: Mean={mean_height2}, SD={std_deviation2}')
plt.title('(Normale) verdeling van lengtes')
plt.xlabel('Lengte (cm)')
plt.ylabel('Frequentie')
plt.legend()
plt.show()