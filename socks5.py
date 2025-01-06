import os
import sys

# Lấy các tham số từ file chính
SETURL = sys.argv[1]
PROXY = sys.argv[2]
VERIFY = sys.argv[3]

# Xóa file `socks5.txt` nếu tồn tại
if os.path.exists("../socks5.txt"):
    os.remove("../socks5.txt")

# Chạy lệnh tương đương với file .bat
os.chdir("..")
os.system(f"python cc.py -url {SETURL} -m cc -v 5 -t 1000 -f {PROXY}socks5.txt -b 1 -s 2592000 {VERIFY}")
