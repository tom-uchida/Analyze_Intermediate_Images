# 画像を複数枚読み込み，全ての画像に対してクロッピングをおこなうプログラム
#   2019/07/12

import cv2
import numpy as np
import sys
args = sys.argv

# Check arguments
import sys
args = sys.argv
if len(args) != 3:
    print("\nUSAGE   : $ python crop_images.py [input_images_path] [repeat_level]")
    print("EXAMPLE : $ python crop_images.py OUTPUT/LR100/ 100\n")
    sys.exit()

def main():
    repeat_level = int(args[2])

    # User input
    # print('Please input width pixel coords :')
    # start_w = input('   start_w  >> ')
    # end_w   = input('     end_w  >> ')
    # print('\nPlease input height pixel coords :')
    # start_h = input('   start_h  >> ')
    # end_h   = input('     end_h  >> ')

    start_w, end_w = 30,180
    start_h, end_h = 50,200

    # Crop all images
    for i in range(repeat_level):
        # Read image
        img_in = cv2.imread( args[1]+"ensemble"+str(i+1)+".bmp" )

        # Crop image
        img_cropped = img_in[int(start_h):int(end_h), int(start_w):int(end_w)]

        # Write image
        out_name = args[1] + "cropped"+str(i+1)+".png"
        cv2.imwrite( out_name, img_cropped )
    # end for i

    print("\nDone.")

if __name__ == "__main__":
    main()