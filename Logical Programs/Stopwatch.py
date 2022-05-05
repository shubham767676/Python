'''
Author: Shubham Singh
Date: 05/05/2022
Description: Stopwatch Program for measuring the time that elapses between the start and end clicks
'''

import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  

  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

input("Press Enter to Start Stopwatch")
start_time = time.time()

input("Press Enter to Stop Stopwatch")
end_time = time.time()

time_lapsed = end_time - start_time

time_convert(time_lapsed)