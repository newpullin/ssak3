from ssak3 import *
import shutil

my_path = "D:/backup/안심글꼴(123종)"
all_files = ssak3_file(my_path)

dst = my_path + "/target"
if not os.path.exists(dst) :
    os.mkdir(dst)
for file in all_files:
    shutil.copy(file, dst)