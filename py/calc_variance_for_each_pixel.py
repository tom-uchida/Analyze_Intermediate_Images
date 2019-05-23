# calc_variance_for_each_pixel.py
#   Tomomasa Uchida
#   2019/05/04

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cycler
import matplotlib.gridspec as gridspec
import matplotlib.patches as pat
import cv2
import statistics

# Graph settings
plt.style.use('seaborn-white')
colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=False, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["mathtext.rm"] = "Times New Roman"

# Check arguments
import sys
args = sys.argv
if len(args) != 4:
    print("\nUSAGE   : $ python calc_variance_for_each_pixel.py [input_images_path] [repeat_level] [image_resolution]")
    print("EXAMPLE : $ python calc_variance_for_each_pixel.py OUTPUT/LR100/IMAGE_DATA/ 100 1000")
    sys.exit()



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
            print("R :", R_pixel_values.shape)
            print("G :", G_pixel_values.shape)
            print("B :", B_pixel_values.shape)

    return R_pixel_values, G_pixel_values, B_pixel_values



def CalcVariance4EachPixel( _R_pixel_values, _G_pixel_values, _B_pixel_values, _repeat_level, _image_resol ):
    # Prepare empty numpy array
    #bg_color_indices = np.empty( (_image_resol*1, _image_resol*1, _repeat_level), bool )

    # Check if each pixel is background color
    # In this experiment environment,
    #  if the R pixel value is 0, it is always the background color (black)
    #  because pixel colors are the only following 3 pattern.
    #   - White : (255, 255, 255)
    #   - Red   : (255,   0,   0)
    #   - Black : (  0,   0,   0) Background
    bg_color_indices = (_R_pixel_values == 0) & (_G_pixel_values == 0) & (_B_pixel_values == 0)
    num_of_bgcolor = np.count_nonzero( bg_color_indices )
    print("Num. of bgcolor pixels :", num_of_bgcolor)


    # Prepare empty numpy array
    # Variance image is a 2D array
    R_vars = np.empty( (_image_resol*1, _image_resol*1), float )
    G_vars = np.empty( (_image_resol*1, _image_resol*1), float )
    B_vars = np.empty( (_image_resol*1, _image_resol*1), float )

    # Calc variance for each pixel
    print("\nCalc variance pixel by pixel ...")
    for h in range( _image_resol ):     # height
        for w in range( _image_resol ): # width
            # Initialize local variables
            sum_R,   sum_G,  sum_B = 0, 0, 0
            sum2_R, sum2_G, sum2_B = 0, 0, 0
            avg_R,   avg_G,  avg_B = 0, 0, 0
            avg2_R, avg2_G, avg2_B = 0, 0, 0
            M = 0

            # Calc pixel by pixel
            for r in range( _repeat_level ):
                # DO NOT calc if the target pixel is background color
                if _R_pixel_values[h,w,r] != 0:
                    # Update value of M
                    M += 1

                    # Calc sum and sum2
                    sum_R  += _R_pixel_values[h,w,r]
                    sum_G  += _G_pixel_values[h,w,r]
                    sum_B  += _B_pixel_values[h,w,r]

                    sum2_R += _R_pixel_values[h,w,r] ** 2
                    sum2_G += _G_pixel_values[h,w,r] ** 2
                    sum2_B += _B_pixel_values[h,w,r] ** 2
                # end if
            # end for r

            # Calc average
            if M != 0:
                avg_R = sum_R / M
                avg_G = sum_G / M
                avg_B = sum_B / M

                avg2_R = sum2_R / M
                avg2_G = sum2_G / M
                avg2_B = sum2_B / M

                var_R = avg2_R - (avg_R**2)
                var_G = avg2_G - (avg_G**2)
                var_B = avg2_B - (avg_B**2)

                # if (h == _image_resol*0.5) & (w < _image_resol*0.5):
                #     print( int(var_G) )

                # Calc variance
                R_vars[h,w] = np.sqrt( var_R / _repeat_level )
                G_vars[h,w] = np.sqrt( var_G / _repeat_level )
                B_vars[h,w] = np.sqrt( var_B / _repeat_level )

            # M = 0
            # If target pixel color is background color
            else:
                R_vars[h,w] = 0
                G_vars[h,w] = 0
                B_vars[h,w] = 0
            # end if

            # Show progress
            if ((h*_image_resol+w)+1)%(_image_resol*_image_resol*0.1) == 0:
                print((h*_image_resol+w)+1, "pixels done.")

            # end for w
        # end for h

    # Write to csv file
    np.savetxt("OUTPUT_DATA/R_vars.txt", R_vars, fmt='%d')
    np.savetxt("OUTPUT_DATA/G_vars.txt", G_vars, fmt='%d')
    np.savetxt("OUTPUT_DATA/B_vars.txt", B_vars, fmt='%d')

    # RGB各配列を重ねて，軸を指定して平均を求める
    # np.mean()
    # result_avg_image = np.empty( (_image_resol, _image_resol), float )



if __name__ == "__main__":
    print("\n** Intermediate Images :")

    # Set repeat level
    repeat_level = args[2]
    print("Repeat Level     :", repeat_level)

    # Set image resolution
    image_resol = args[3]
    print("Image Resolution :", image_resol)

    # Read intermediate images
    serial_img_path = args[1]
    R_pixel_values, G_pixel_values, B_pixel_values = ReadIntermediateImages( repeat_level, image_resol, serial_img_path )


    CalcVariance4EachPixel( R_pixel_values, G_pixel_values, B_pixel_values, repeat_level, image_resol )