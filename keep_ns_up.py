#!/usr/bin/env python3

import subprocess
import time

while(True):
	subprocess.call(["npm", "start"])
	time.sleep(900) # 15 minutes
