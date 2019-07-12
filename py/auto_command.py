#   Tomomasa Uchida
#   2019/07/12

import sys
import subprocess
import time


# Check arguments
args = sys.argv
if len(args) != 3:
    print("\nUSAGE   : $ python auto_command.py [spbr_file_path] [spbr_header_file]\n")
    sys.exit()


# Excute SPBR continuously
spbr_file_path      = args[1]
spbr_header_file    = args[2]

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR2", spbr_header_file, "2"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR10", spbr_header_file, "10"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR20", spbr_header_file, "20"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR30", spbr_header_file, "30"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR40", spbr_header_file, "40"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR50", spbr_header_file, "50"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR60", spbr_header_file, "60"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR70", spbr_header_file, "70"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR80", spbr_header_file, "80"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR90", spbr_header_file, "90"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR100", spbr_header_file, "100"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR110", spbr_header_file, "110"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR120", spbr_header_file, "120"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR130", spbr_header_file, "130"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR140", spbr_header_file, "140"] )

subprocess.check_call( ["python", "spbr_continuously.py", spbr_file_path+"LR150", spbr_header_file, "150"] )