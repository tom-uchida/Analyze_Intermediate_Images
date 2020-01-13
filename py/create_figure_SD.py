# create_figure_SD.py
#   Tomomasa Uchida
#   2019/05/29

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('bmh')

# from matplotlib import cycler
# colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
# plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=False, prop_cycle=colors)
# plt.rc('grid', color='w', linestyle='solid')
# plt.rc('patch', edgecolor='#E6E6E6')
# plt.rc('lines', linewidth=2)
# plt.figure(figsize=(8,6))

plt.rcParams["mathtext.rm"] = "Times New Roman"
# plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams["mathtext.fontset"] = "cm"
# plt.rcParams["font.size"] = 14

# Check arguments
import sys
args = sys.argv
if len(args) != 2:
    print("\nUSAGE   : $ python create_figure_SD.py [csv_file_path]")
    print("EXAMPLE : $ python create_figure_SD.py OUTPUT/funehoko/SD_mean_max.csv\n")
    sys.exit()



# Read csv file
csv = pd.read_csv(args[1], header=None)

# Convert to numpy array
sd_mean_max = csv.values
print(sd_mean_max.shape)
print(sd_mean_max)

# Get each column
L       = sd_mean_max[:,0]
sd_mean = sd_mean_max[:,1]
sd_max  = sd_mean_max[:,2]

# Creat figure
plt.figure(figsize=(9, 6)) # figsize=(width, height)

# Max
plt.scatter(L, sd_max, color='red', label='Max', marker=",", s=100)

# Mean
plt.scatter(L, sd_mean, color='black', label='Mean', s=100)

plt.xlabel('$L$', fontsize=24)
plt.ylabel('Standard Deviation per pixel', fontsize=24)

plt.xticks([2, 50, 100, 150], fontsize=18)
plt.yticks([1, 20, 40, 60, 80, 100], fontsize=18)

# plt.grid()
plt.legend(fontsize=20)

plt.show()