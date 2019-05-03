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



def ReadIntermediateImages( _repeat_level, _image_resol, _serial_img_path ):
    # Prepare empty numpy array
    R_pixel_values = np.empty( (_image_resol*1, _image_resol*1, _repeat_level), np.uint8 )
    G_pixel_values = np.empty( (_image_resol*1, _image_resol*1, _repeat_level), np.uint8 )
    B_pixel_values = np.empty( (_image_resol*1, _image_resol*1, _repeat_level), np.uint8 )

    # Read intermediate images
    for i in range( _repeat_level ):
        # Read each ensemble image
        tmp_image_RGB = ReadImage( _serial_img_path + "ensemble"+str(i+1)+".bmp" )

        # Split into RGB and add to numpy array
        R_pixel_values[:,:,i] = tmp_image_RGB[:,:,0] # R
        G_pixel_values[:,:,i] = tmp_image_RGB[:,:,1] # G
        B_pixel_values[:,:,i] = tmp_image_RGB[:,:,2] # B

        if i == _repeat_level-1:
            print(R_pixel_values.shape, G_pixel_values.shape, B_pixel_values.shape)

    return R_pixel_values, G_pixel_values, B_pixel_values



def CalcVariance4EachPixel( _R_pixel_values, _G_pixel_values, _B_pixel_values, _repeat_level, _image_resol ):
    # Prepare empty numpy array
    bg_color_indices = np.empty( (_image_resol*1, _image_resol*1, _repeat_level), bool )

    # Check if each pixel is background color
    bg_color_indices = np.where(_R_pixel_values == _G_pixel_values == _B_pixel_values == 0)

    #true or falseを返すやつを使う

    for r in range( _repeat_level ):
        for i in range( _image_resol ):
            # BGColor (Black)
            if _R_pixel_values[r,i] == 0 and _G_pixel_values[r,i] == 0 and _B_pixel_values[r,i] == 0:
                bg_color_indices[r][i] = False

            # NOT BGColor
            else:
                bg_color_indices[r][i] = True

    num_of_bgcolor = np.count_nonzero( bg_color_indices )
    print("num_of_bgcolor =", num_of_bgcolor) # 995322 pixels

    # Pixel color is the following 3 pattern
    # White : (255, 255, 255)
    # Red   : (255,   0,   0)
    # Black : (  0,   0,   0) Background

    # Prepare empty numpy array
    R_vars = np.empty( (0, _image_resol*1), float )
    G_vars = np.empty( (0, _image_resol*1), float )
    B_vars = np.empty( (0, _image_resol*1), float )

    # Calc variance for each pixel
    for i in range( _image_resol ):
        sum_R, sum_G, sum_B = 0, 0, 0
        not_bg_color_counter = 0

        for r in range( _repeat_level ):
            # IMPORTANT:
            # Only when target pixel is NOT the background color
            if bg_color_indices[r][i] == True:
                sum_R += _R_pixel_values[r, i]
                sum_G += _G_pixel_values[r, i]
                sum_B += _B_pixel_values[r, i]
                not_bg_color_counter += 1
        # end for

        if i <= 100:
            print(not_bg_color_counter)
            print(_R_pixel_values[0, i])
            print(_G_pixel_values[0, i])
            print(_B_pixel_values[0, i])

        # Show progress
        if (i+1) % (_image_resol*0.1) == 0:
            print(i+1, "pixels done.")
    # end for

    # Write to csv file
    # np.savetxt("OUT_DATA/R_vars.txt", R_vars, fmt='%.5f')



if __name__ == "__main__":
    # Set repeat level
    repeat_level = 10

    # Set image resolution
    image_resol = 1000

    # Read intermediate images
    R_pixel_values, G_pixel_values, B_pixel_values = ReadIntermediateImages( repeat_level, image_resol, "../OUTPUT_DATA/LR"+str(repeat_level)+"/sigma2_1e-05/IMAGE_DATA/" )

    # CalcVariance4EachPixel( R_pixel_values, G_pixel_values, B_pixel_values, repeat_level, image_size )



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