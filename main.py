#!/usr/bin/python3

# this is the main script to run the speedtest every 5 minutes

import subprocess
from datetime import datetime
import time

while True:
    timestamp = datetime.now()
    f = open("/home/junaid/code/other/kiitspeedtest/data.txt", "a")
    
    result = subprocess.run(['speedtest-cli'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    f.write("{}\n\n".format(timestamp))
    f.write((result.stdout).decode("utf-8"))
    f.write("\n---------------------------------------------------------------------\n\n")

    time.sleep(300)