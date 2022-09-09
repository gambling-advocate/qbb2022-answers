#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats
import statsmodels.api as sm

df = np.genfromtxt("final_sort.csv", delimiter=",", dtype= None, encoding = None, names=True)

mdnm = df["motherdnm"]
mage = df["motherage"]
ddnm = df['fatherdnm']
dage = df['fatherage']


comparison =smf.ols(formula = "fatherdnm ~ 1 + fatherage", data = df)
results = comparison.fit()
print(results.summary())
print(results.pvalues)
# DNM = 1.3538(age) + 10.3263

# fig, ax = plt.subplots()
# ax.hist(mdnm, label = "Maternal")
# ax.hist(ddnm, label = "Paternal", alpha = 0.5)
# ax.set_xlabel("# of de novo mutations")
# ax.set_ylabel("Frequency")
# ax.legend()
# plt.show()
# plt.savefig("ex2_c.png")

# paternal_agemut =smf.ols(formula = "fatherdnm ~ 1 + fatherage", data = df)
# results = paternal_agemut.fit()
# print(results.summary())
# print(results.pvalues)

# maternal_agemut =smf.ols(formula = "motherdnm ~ 1 + motherage", data = df)
# results = maternal_agemut.fit()
# print(results.summary())
# print(results.pvalues)

# fig, ax = plt.subplots()
# ax.scatter(mage, mdnm)
# plt.xlabel('Maternal Age')
# plt.ylabel('Maternal De novo Mutations')
# plt.title("Increase in De novo Mutations with age")
# plt.show()
# plt.savefig("ex2_a.png")

# ax.scatter(dage, ddnm)
# plt.xlabel('Paternal Age')
# plt.ylabel('Paternal De novo Mutations')
# plt.title("Increase in De novo Mutations with age")
# plt.show()
# plt.savefig("ex2_b.png")