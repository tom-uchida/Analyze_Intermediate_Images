# create_figure.py
#   Tomomasa Uchida
#   2019/05/29

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
    print("\nUSAGE   : $ python calc_variance_for_each_pixel.py [csv_file_path]")
    print("EXAMPLE : $ python calc_variance_for_each_pixel.py OUTPUT/funehoko/SD_mean_max.csv\n")
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
# plt.plot(LR, NMSE, color='black')
# plt.scatter(L, sd_mean, color='black', label='mean')
plt.scatter(L, sd_max, color='black', label='max')

plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["mathtext.rm"] = "Times New Roman"
plt.rcParams["font.size"] = 14
plt.xlabel('$L$', fontsize=14)
plt.ylabel('standard deviation', fontsize=14) # Gray scale

# # draw circle
# # plt.scatter(RL_original[2], api_original[2], facecolor='none', s=200, edgecolor='black')
# # plt.scatter(RL_noised[2], api_noised[2], facecolor='none', s=200, edgecolor='black')
# # plt.scatter(RL_original[11], api_original[11], facecolor='none', s=200, edgecolor='black')
# # plt.scatter(RL_noised[11], api_noised[11], facecolor='none', s=200, edgecolor='black')

# # Draw text
# # plt.text(5, 20.5, "20.5", fontsize=14, color='black')
# # plt.text(10, 1.0, "0.336", fontsize=14, color='black')
# # plt.text(100, 0.8, "0.0318", fontsize=14, color='black')

plt.xticks([2, 50, 100, 150], fontsize=14)
# #plt.xticks([0, 10, 100])
plt.yticks([1, 20, 40, 60], fontsize=14)
# #plt.ylim([0, 275])

plt.grid()
# plt.legend(fontsize=14)

plt.show()