"""
Deze code simuleert een (groot) aantal herhaalde 'experimenten'
waarbij steeds een aantal keer een munt wordt gegooid en
de verhouding kop/munt wordt vastgelegd.

Als je kijk hoevaak iedere verhouding voorkomt
(0.5 zal het meeste voorkomen, even veel kop-als-munt)
Zie je een normaalverdeling verschijnen.

Note:
    it follows a binomial distribution. For large numbers of tosses,
    it approximately follows a normal distribution
"""

import numpy as np
import matplotlib.pyplot as plt

num_flips = 100          # Number of coin flips per experiment
num_experiments = 50000  # Number of experiments

ratio_list = []
for _ in range(num_experiments):
    flips = np.random.choice([0, 1], size=num_flips)
    ratio_of_heads = sum(flips) / num_flips # heads is 1, coins 0. So summing counts heads
    ratio_list.append(ratio_of_heads)

# Plotting the results
binwidth = 0.005
bins = np.arange(min(ratio_list), max(ratio_list) + binwidth, binwidth)
plt.hist(ratio_list, bins=bins, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Verhouding Kop t.o.v. Munt')
plt.ylabel('Frequentie')
plt.axvline(x=0.5, color='r', linestyle='--')
plt.show()