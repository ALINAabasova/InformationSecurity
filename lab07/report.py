#!/usr/bin/env python3
import datetime
import getpass
import shutil
import os

log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report_log.txt")
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = getpass.getuser()
total, used, free = shutil.disk_usage("/")
line = f"[{now}] user={user} disk_free={free // (1024**3)}GB\n"
with open(log_path, "a") as f:
    f.write(line)
print("Report written:", line.strip())
