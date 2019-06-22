# create_comparison_figure.py
#   Tomomasa Uchida
#   2019/06/16

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
if len(args) != 3:
    print("\nUSAGE   : $ python calc_variance_for_each_pixel.py [csv_file_path_1] [csv_file_path_2]")
    sys.exit()



# Read csv file
csv1 = pd.read_csv(args[1], header=None)
csv2 = pd.read_csv(args[2], header=None)

# Convert to numpy array
sd_mean_max1 = csv1.values
sd_mean_max2 = csv2.values

# Get each column
L1       = sd_mean_max1[:,0]
sd_mean1 = sd_mean_max1[:,1]
sd_max1  = sd_mean_max1[:,2]
L2       = sd_mean_max2[:,0]
sd_mean2 = sd_mean_max2[:,1]
sd_max2  = sd_mean_max2[:,2]


# Creat figure
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["mathtext.rm"] = "Times New Roman"
plt.rcParams["font.size"] = 14

plt.scatter(L1, sd_mean1, color='black', label='Ground truth')
plt.scatter(L2, sd_mean2, color='black', label='Gaussian noise($\sigma = 10$)', marker="D")

plt.legend(fontsize=14)
plt.xlabel('$L$', fontsize=14)
plt.ylabel('standard deviation', fontsize=14) # Gray scale

plt.xticks([2, 50, 100, 150], fontsize=14)
# plt.yticks([1, 20, 40, 60, 80], fontsize=14) # max
plt.yticks([1, 5, 10, 15, 20, 25, 30], fontsize=14) # mean

plt.grid()

plt.show()