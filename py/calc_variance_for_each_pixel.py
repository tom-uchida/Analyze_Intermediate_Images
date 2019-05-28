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
    print("EXAMPLE : $ python calc_variance_for_each_pixel.py ../OUTPUT/LR100/IMAGE_DATA/ 100 1000\n")
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
    # Set repeat level
    L = _repeat_level
    
    # Set back ground color
    bg_color = 0

    # Prepare empty numpy array
    #bg_color_indices = np.empty( (_image_resol*1, _image_resol*1, _repeat_level), bool )

    # Check if each pixel is background color
    # In this experiment environment,
    #  if the R pixel value is 0, it is always the background color (black)
    #  because pixel colors are the only following 3 pattern.
    #   - White : (255, 255, 255)
    #   - Red   : (255,   0,   0)
    #   - Black : (  0,   0,   0) Background
    bg_color_indices = (_R_pixel_values == bg_color) & (_G_pixel_values == bg_color) & (_B_pixel_values == bg_color)
    num_of_bgcolor = np.count_nonzero( bg_color_indices )
    print("(Avg num of bgcolor pixels included in each ensemble) :", int(num_of_bgcolor / _repeat_level), "(pixels)")

    # Prepare empty numpy array
    # Variance(or S.D.) image is a 2D array
    R_sd = np.empty( (_image_resol*1, _image_resol*1), float )
    G_sd = np.empty( (_image_resol*1, _image_resol*1), float )
    B_sd = np.empty( (_image_resol*1, _image_resol*1), float )
    # R_vars = np.empty( (_image_resol*1, _image_resol*1), float )
    # G_vars = np.empty( (_image_resol*1, _image_resol*1), float )
    # B_vars = np.empty( (_image_resol*1, _image_resol*1), float )

    print("\nCalc variance pixel by pixel ...")
    for h in range( _image_resol ):     # height
        for w in range( _image_resol ): # width
            # Initialize local variables
            sum_R,   sum_G,  sum_B = 0, 0, 0
            sum2_R, sum2_G, sum2_B = 0, 0, 0
            avg_R,   avg_G,  avg_B = 0, 0, 0
            avg2_R, avg2_G, avg2_B = 0, 0, 0
            M = 0

            # Calc variance for each corresponding pixel
            for r in range( L ):
                # NOTE: DO NOT include if the target pixel is background color
                if bg_color_indices[h,w,r] != True: # True: bg_color
                    # Update value of M
                    M += 1

                    # Calc sum
                    sum_R  += _R_pixel_values[h,w,r]
                    sum_G  += _G_pixel_values[h,w,r]
                    sum_B  += _B_pixel_values[h,w,r]

                    # Calc sum2
                    sum2_R += _R_pixel_values[h,w,r] ** 2
                    sum2_G += _G_pixel_values[h,w,r] ** 2
                    sum2_B += _B_pixel_values[h,w,r] ** 2
                # end if
            # end for r

            # Calc average
            if M != 0:
                # Calc avg for sum
                avg_R   = sum_R  / M
                avg_G   = sum_G  / M
                avg_B   = sum_B  / M

                # Calc avg for sum2
                avg2_R  = sum2_R / M
                avg2_G  = sum2_G / M
                avg2_B  = sum2_B / M

                # Calc variance by using avg4sum and avg4sum2
                var_R   = avg2_R - (avg_R**2)
                var_G   = avg2_G - (avg_G**2)
                var_B   = avg2_B - (avg_B**2)

                # if (h == _image_resol*0.5) & (w < _image_resol*0.5):
                #     print( int(var_G) )

                # Calc sigma max
                # NOTE: L or LM or L^2
                # R_sigma_max = var_R / L
                # G_sigma_max = var_G / L
                # B_sigma_max = var_B / L
                # R_sigma_max = var_R / (L*M)
                # G_sigma_max = var_G / (L*M)
                # B_sigma_max = var_B / (L*M)
                R_sigma_max = var_R / (L**2)
                G_sigma_max = var_G / (L**2)
                B_sigma_max = var_B / (L**2)

                # Calc standard deviation
                R_sd[h,w] = np.sqrt( R_sigma_max )
                G_sd[h,w] = np.sqrt( G_sigma_max )
                B_sd[h,w] = np.sqrt( B_sigma_max )

            # If target pixel color is background color
            #  (M = 0)
            else:
                R_sd[h,w] = 0
                G_sd[h,w] = 0
                B_sd[h,w] = 0
            # end if

            # Show progress
            if ((h*_image_resol+w)+1)%(_image_resol*_image_resol*0.1) == 0:
                print(" ", (h*_image_resol+w)+1, "/", _image_resol**2,"pixels done.")

            # end for w
        # end for h

    # Write to txt file
    # np.savetxt("OUTPUT_DATA/R_sd.txt", R_sd, fmt='%d')
    # np.savetxt("OUTPUT_DATA/G_sd.txt", G_sd, fmt='%d')
    # np.savetxt("OUTPUT_DATA/B_sd.txt", B_sd, fmt='%d')

    # Combine R, G and B arrays
    RGB_sd = np.array([R_sd, G_sd, B_sd])
    RGB_sd_mean = np.mean(RGB_sd, axis=0)
    np.savetxt("OUTPUT_DATA/RGB_sd_mean.txt", RGB_sd_mean, fmt='%d')
    RGB_sd_mean_non_bgcolor = RGB_sd_mean[RGB_sd_mean != bg_color]
    
    return RGB_sd_mean, RGB_sd_mean_non_bgcolor



def CreateFigure(_RGB_sd_mean, _RGB_sd_mean_non_bgcolor, _image_resol):
    sd_mean = np.mean(_RGB_sd_mean_non_bgcolor)
    sd_max  = np.max(_RGB_sd_mean_non_bgcolor)
    print("\nsd_mean :", sd_mean)
    print("sd_max  :", sd_max, "\n")

    fig = plt.figure(figsize=(6, 10)) # figsize=(width, height)
    gs  = gridspec.GridSpec(2,1)

    # SD image
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    ax1 = fig.add_subplot(gs[0,0])
    ax1.set_title('SD image')
    img = ax1.imshow(_RGB_sd_mean, clim=[0,sd_max], cmap='viridis')
    ax1.axis("image")
    divider = make_axes_locatable(ax1)
    ax1_cb = divider.new_horizontal(size="4.5%", pad=0.2)
    fig.add_axes(ax1_cb)
    plt.colorbar(img, cax=ax1_cb)
    ax1.axis('off')
    # ax1.imshow(_RGB_sd_mean, cmap='viridis' )
    # ax1.set_xticks([]), ax1.set_yticks([])

    # Histogram
    ax2 = fig.add_subplot(gs[1,0])
    ax2.set_title('SD histogram')
    ax2.hist(_RGB_sd_mean_non_bgcolor.ravel(), bins=50, color='black')
    hist, bins = np.histogram(_RGB_sd_mean_non_bgcolor, 50)

    # Show SD mean
    ax2.axvline(sd_mean, color='red')
    text = "mean :\n" + str(round(sd_mean,2))
    ax2.text(sd_mean-sd_mean*0.1, max(hist)*0.9, text, color='red', fontsize='16')

    # Show SD max
    ax2.axvline(sd_max, color='blue')
    text = "max :\n" + str(round(sd_max,2))
    ax2.text(sd_max-sd_mean*0.1, max(hist)*0.9, text, color='blue', fontsize='16')

    # plt.figure(figsize=(8, 8))
    # plt.imshow( RGB_sd_mean, cmap='viridis' )
    # plt.colorbar(_RGB_sd_mean, pad=0.1, shrink=0.75, orientation='horizontal')
    plt.savefig("OUTPUT_DATA/result.png")
    print("Saved figure.\n")


if __name__ == "__main__":
    print("\n** Intermediate Images :")

    # Set repeat level
    repeat_level = int(args[2])
    print("Repeat Level     :", repeat_level)

    # Set image resolution
    image_resol = int(args[3])
    print("Image Resolution :", image_resol)

    # Read intermediate images
    serial_img_path = args[1] + "/"
    R_pixel_values, G_pixel_values, B_pixel_values = ReadIntermediateImages( repeat_level, image_resol, serial_img_path )

    # Calc variance
    RGB_sd_mean, RGB_sd_mean_non_bgcolor= CalcVariance4EachPixel( R_pixel_values, G_pixel_values, B_pixel_values, repeat_level, image_resol )

    # Create figure
    CreateFigure(RGB_sd_mean, RGB_sd_mean_non_bgcolor, image_resol)