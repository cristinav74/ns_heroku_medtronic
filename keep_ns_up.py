#!/usr/bin/env python3

import subprocess
import time
import psutil


def checkIfProcessRunning(processName):

    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            pass
    return False


while(True):
	if (checkIfProcessRunning("npm") == False):
		subprocess.call(["npm", "start"])
	time.sleep(600) # 10 minutes
