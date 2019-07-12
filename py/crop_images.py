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
    repeat_level = args[2]

    # User input
    print('Please input start pixel coords.')
    start_x = input('start_x  >>')
    start_y = input('start_y  >>')
    print('\n')
    print('Please input end pixel coords.')
    end_x   = input('end_x    >>')
    end_y   = input('end_y    >>')

    # Crop all images
    for i in range(repeat_level):
        # Read image
        img_in = cv2.imread( args[1]+"ensemble{0:03d}.bmp".format(i) )

        # Crop image
        img_cropped = img_in[int(start_y):int(end_y), int(start_x):int(end_x)]

        # Write image
        out_name = args[1] + "cropped{0:03d}.png"
        cv2.imwrite( out_name.format(i), img_cropped )
    # end for i

if __name__ == "__main__":
    main()