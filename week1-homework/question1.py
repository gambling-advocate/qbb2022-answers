#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

#generating a 1 million unit list
n = int(1000000)
genome = [0] * n

#need a for loop to go through the 50,000 reads
for i in range(50000):
    randgene = np.random.randint(0, 999900)
    #this should go through 50,000 reads from 0, 999900. Since the reads are 100bp long we stop before 1M. 
    #this makes the reads 100bp long and adds one for every place there is coverage
    for j in range(randgene, randgene + 100):
        genome[j] += 1
#putting it all into an array
x = np.array(genome)
#Setting a variable for anytime that my array is equal to zero and counting that number to see how many bases had noncoverage.
zero = x == 0
meh = np.count_nonzero(zero)


# #plotting the array into a histogram and setting a poisson pmf with a lambda of 5 
# fig, ax = plt.subplots()
# ax.hist(x, density = True)
# ax.plot(x, poisson.pmf(x, mu = 5), 'bo')
# ax.set_ylabel("frequency")
# ax.set_xlabel("coverage")
# plt.savefig("12hist")
# plt.show