# create_figure_M.py
#   Tomomasa Uchida
#   2019/07/01

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

from matplotlib import cycler
colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=False, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)
# plt.figure(figsize=(8,6))

# Check arguments
import sys
args = sys.argv
if len(args) != 2:
    print("\nUSAGE   : $ python create_figure_M.py [csv_file_path]")
    print("EXAMPLE : $ python create_figure_M.py OUTPUT/funehoko/SD_mean_max.csv\n")
    sys.exit()



# Read csv file
# csv = pd.read_csv(args[1], header=None)
csv = pd.read_csv(args[1])

# Convert to numpy array
M_mean_max = csv.values
print(M_mean_max.shape)
print(M_mean_max)

# Get each column
L      = M_mean_max[:,0]
M_mean = M_mean_max[:,1]
M_max  = M_mean_max[:,2]
ML     = M_mean / L

# Creat figure

# max
# plt.scatter(L, M_max, color='blue', label='max', marker=",")

# mean
# plt.scatter(L, M_mean, color='red', label='mean')

# M/L
plt.scatter(L, ML, color='black')

plt.legend(fontsize=14)

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["mathtext.rm"] = "Times New Roman"
plt.rcParams["font.size"] = 14
plt.xlabel('$L$', fontsize=14)
# plt.ylabel('$M$', fontsize=14) # Gray scale
plt.ylabel('$M / L$', fontsize=14) # Gray scale

plt.xticks([2, 50, 100, 150], fontsize=14)
# plt.yticks([0, 5, 10, 15, 20], fontsize=14) # max
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=14) # max

plt.grid()

plt.show()