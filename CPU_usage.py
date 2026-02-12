#Apply changes.
#Checking for how the CPU is working and how much it has a load

import psutil

def check_cpu_usage(percent):

    usage = psutil.cpu_percent()

    return usage < percent

if not check_cpu_usage(75):

    print("ERROR! CPU is overloaded")

else:


    print("Everything ok")