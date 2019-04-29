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



def ReadImage( _img_name ):
    # read input image
    img_BGR = cv2.imread(_img_name)

    # convert color BGR to RGB
    img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

    return img_RGB



def ReadIntermediateImages( _repeat_level, _image_size, _serial_img_path ):
    # Prepare empty numpy array
    intermediate_images = np.empty( (0, _image_size*3), np.uint8 )

    # Read intermediate images
    for i in range( _repeat_level ):
        tmp_image = ReadImage( _serial_img_path + "ensemble"+str(i+1)+".bmp" )

        # Append to numpy array (https://qiita.com/fist0/items/d0779ff861356dafaf95)
        intermediate_images = np.append( intermediate_images, tmp_image.reshape((1, _image_size*3)), axis=0 )

        if i == _repeat_level-1:
            print(intermediate_images.shape)

    return intermediate_images



def CalcVariance4EachPixel( _intermideate_images, _repeat_level, _image_size ):
    # Prepare empty numpy array
    R_pixel_values = np.empty( (0, _image_size*1), np.uint8 )
    G_pixel_values = np.empty( (0, _image_size*1), np.uint8 )
    B_pixel_values = np.empty( (0, _image_size*1), np.uint8 )

    # Split into RGB
    for i in range( _repeat_level ):
        R_pixel_values = np.append( R_pixel_values, _intermideate_images[i, :_image_size].reshape((1, _image_size*1)), axis=0 )
        G_pixel_values = np.append( G_pixel_values, _intermideate_images[i, _image_size:2*_image_size].reshape((1, _image_size*1)), axis=0 )
        B_pixel_values = np.append( B_pixel_values, _intermideate_images[i, 2*_image_size:3*_image_size].reshape((1, _image_size*1)), axis=0 )

    print(R_pixel_values.shape, G_pixel_values.shape, B_pixel_values.shape)

    # Prepare empty numpy array
    R_vars = np.empty( (0, _image_size*1), float )
    G_vars = np.empty( (0, _image_size*1), float )
    B_vars = np.empty( (0, _image_size*1), float )

    # Calc variance for each pixel
    for i in range( _image_size ):
        # Background color is not counted
        # if == bg_color:

        if i == 0:
            print("var = ", np.var( R_pixel_values[:, i] ))
            print( np.var( R_pixel_values[:, i]) )

        # Calc variance
        # R_vars = np.append( R_vars, np.var( R_pixel_values[:, i] ) )

        if i <= 100:
            mean = np.mean( R_pixel_values[:, i] )
            print(mean)

        # Show progress
        if (i+1) % (_image_size*0.1) == 0:
            print(i+1, "pixels done.")

    print(R_vars.shape)

    # Write to csv file
    np.savetxt("OUT_DATA/R_vars.txt", R_vars, fmt='%.5f')

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
    # Set repeat level
    repeat_level = 10

    # Set image size
    image_size = 1000**2

    # Read intermediate images
    intermediate_images = ReadIntermediateImages( repeat_level, image_size, "../OUTPUT_DATA/LR"+str(repeat_level)+"/sigma2_1e-05/IMAGE_DATA/" )

    CalcVariance4EachPixel( intermediate_images, repeat_level, image_size )