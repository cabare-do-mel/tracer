from tracer4 import troy_the_tracer
from getloc import *


track_list = troy_the_tracer()

ip_list = getLoc(track_list)
# my_location = getMyLoc()
# target_location = getTargetLoc()
print(ip_list)

