# Execute SPBR command continuously
#   Tomomasa Uchida
#   2019/05/22

import sys
import subprocess
import time


# Check arguments
args = sys.argv
if len(args) != 4:
    print("\nUSAGE   : $ python spbr_continuously.py [spbr_file_path] [spbr_header_file] [number_of_executions(= repeat_level)]")
    print("EXAMPLE : $ python spbr_continuously.py /Users/uchidatomomasa/work/SPBR/myProject/AnalyzeIntermediateImages/OUTPUT_DATA/LR100/funehoko /Users/uchidatomomasa/work/SPBR/myProject/AnalyzeIntermediateImages/OUTPUT_DATA/LR100/funehoko/h_funehoko.spbr 100\n")
    sys.exit()


# Excute SPBR continuously
spbr_file_path      = args[1] + "/"
spbr_header_file    = args[2]
num_of_executions   = int(args[3])
for i in range(num_of_executions):
    try:
        file_name = spbr_file_path + "ensemble" + str(i+1) + ".spbr"
        res = subprocess.check_call( ["spbr_auto_snap", spbr_header_file, file_name] )
        # time.sleep(1)

    except:
        print("ERROR")

# spbr_file_path = spbr_file_path+"ensemble1.spbr"
# subprocess.run( ["rm", spbr_file_path] )