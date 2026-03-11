import activeAppTracker
import afkTracker
from datetime import datetime
import time as ti
import threading

# This function returns a list of tuples in this format
# [(idletime,time at recording),(idletime,time at recording),...]
# on the first instance, last instance and when afk_start and afk_stop time is recorded
def afk_logger(run_time,threshold=60):

    afk_data = []
    start_time = datetime.now()
    afk_since = None
    was_afk = False

    while True:
        idletime_since_last_input = afkTracker.getIDLETIMEsinceLastInput()
        current_time = datetime.now()
        
        # records afk_start time
        if threshold <= idletime_since_last_input  and not was_afk:
            afk_since = current_time
            was_afk = True

        # records afk_stop time
        if 0 < idletime_since_last_input < 2 and was_afk:
            afk_data.append((afk_since,current_time))
            was_afk = False

        # exit condition
        # write return value to a file also
        if (current_time - start_time).total_seconds() > run_time:
            afk_data.append((current_time,"exit"))
            with open("logs.txt","a") as f:
                for a,b in afk_data:
                    f.write(f"{a},{b}")
            # write here
            return afk_data

        ti.sleep(0.5)
    

afk_logger(180)
