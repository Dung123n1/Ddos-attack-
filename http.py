import os
import sys

# Lấy các tham số từ file chính
SETURL = sys.argv[1]
PROXY = sys.argv[2]
VERIFY = sys.argv[3]

# Xóa file `http.txt` nếu tồn tại
if os.path.exists("../http.txt"):
    os.remove("../http.txt")

# Chạy lệnh tương đương với http.bat
os.chdir("..")
os.system(f"python cc.py -url {SETURL} -m cc -v http -t 1000 -f {PROXY}http.txt -b 1 -s 2592000 {VERIFY}")
