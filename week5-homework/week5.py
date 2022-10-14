#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
from bdg_loader import load_data

d0h3 = open("D0_H3K27ac_scaled_and_cropped.bdg")
d2h3 = open("D2_H3K27ac_scaled_and_cropped.bdg")
d2k4 = open("D2_Klf4_scaled_and_cropped.bdg")
r1file = open("R1files_treat_scaled_and_cropped.bdg")

LDd0h3 = load_data(d0h3)
LDd2h3 = load_data(d2h3)
LDd2k4 = load_data(d2k4)
LDr1file = load_data(r1file)

# print(LDd0h3)

fig, ax = plt.subplots(nrows = 4)
ax[0].plot(LDd0h3["X"], LDd0h3["Y"])
ax[0].set_title("H3K27ac_day0")
ax[1].plot(LDd2h3["X"], LDd2h3["Y"])
ax[1].set_title("H3K27ac_day2")
ax[2].plot(LDd2k4["X"], LDd2k4["Y"])
ax[2].set_title("Klf4_day2")
ax[3].plot(LDr1file["X"], LDr1file["Y"])
ax[3].set_title("Sox2R1")
plt.tight_layout()
plt.savefig("part1_step_5.png")