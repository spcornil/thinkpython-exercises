################
# Exercise 5-1 #
################
# Write a script that reads the current epoch time and converts it to a time of day in hours, minutes,
# and seconds, plus the number of days since the epoch.

import math
import time

ct = time.time()

# Test var for consistency
#ct = 1676845576.841751

def gmt_time(ct):
    ct_sec = ct % 86400
    cd_hr = int(ct_sec // 3600)
    cd_min = int((ct_sec % 3600) / 3600 * 60)
    cd_sec = int(ct_sec % 60)
    if cd_hr < 10:
        cd_hr = '0' + str(cd_hr)
    if cd_min < 10:
        cd_min = '0' + str(cd_min)
    if cd_sec < 10:
        cd_sec = '0' + str(cd_sec)
    print(str(cd_hr) + ':'+ str(cd_min) + ':' + str(cd_sec))

gmt_time(ct)


