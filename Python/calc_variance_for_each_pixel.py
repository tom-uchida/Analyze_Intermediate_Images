# L枚の中間画像に対して，対応するピクセルごとに分散を計算するプログラム
# 2019/04/14

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cycler
import matplotlib.gridspec as gridspec
import matplotlib.patches as pat
import cv2
import subprocess
import sys
import statistics
import time

# Graph settings
plt.style.use('seaborn-white')
colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=False, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["mathtext.rm"] = "Times New Roman"



def ReadImage(_img_name):
    # read input image
    img_BGR = cv2.imread(_img_name)

    # convert color BGR to RGB
    img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

    return img_RGB



def ReadIntermediateImages(_repeat_level, _serial_img_path):
    # Read input image
    for i in range( _repeat_level ):
        intermediate_img_RGB = ReadImage( _serial_img_path + "ensemble"+str(i+1)+".bmp" )

    # print( type(intermediate_img_RGB) )
    # <class 'numpy.ndarray'>

    print("Input images (RGB)（height, width, channel）:", intermediate_img_RGB.shape)
        

# # Get statistical data of pixel value
# def get_data_of_pixel_value(_img, _img_name):
#   print("===== Statistical Data of", _img_name, "(Gray) =====")
#   print("Num of pixel values (== 255) :", np.sum(_img == 255))
#   print("Num of pixel values (<= 1) :", np.sum(_img <= 1))
#   print("Num of pixel values (== 0)   :", np.sum(_img == 0) )
#   print("\nMax :", np.max(_img))
#   print("Min :", np.min(_img))
#   #print("\nAverage :", np.mean(_img))
#   #print("Median  :", np.median(_img))
#   print("\nAverage :", _img[_img != 0].mean())
#   print("S.D.  :", _img[_img != 0].std())
#   print("\n")
  
#   return _img[_img != 0].mean()


if __name__ == "__main__":
    repeat_level = 10

    # Read images
    ReadIntermediateImages( repeat_level, "../OUTPUT_DATA/LR"+str(repeat_level)+"/IMAGE_DATA/" )
    