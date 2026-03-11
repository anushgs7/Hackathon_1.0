import psutil
from datetime import datetime
import time as ti

# Apps to track
TARGET_APPS = [
    "firefox",
    "code",
    "nautilus",
    "steam",
    "mpv",
    "gnome-text-editor",
    "gnome-system-monitor",
]


def get_running_apps():
    apps = {}
    for proc in psutil.process_iter(['pid','name']):
        try:
            name = proc.info['name']
            if name and name.lower() in TARGET_APPS:
                apps[name.lower()] = proc.info['pid']
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return apps

def get_session_app_data(run_time):

    running_apps = {}
    session_apps_log = []
    start_time = datetime.now()
    
    while True:
        current_apps = get_running_apps()

        # Detect app start
        for app, pid in current_apps.items():
            if app not in running_apps:
                start_time = datetime.now()
                running_apps[app] = (pid, start_time)
               # print(f"{app} opened at {start_time}")

        # Detect app close
        for app in list(running_apps):
            if app not in current_apps:
                pid, start_time = running_apps.pop(app)
                end_time = datetime.now()
                duration = end_time - start_time
                session_apps_log.append((app,start_time,end_time,duration))
                print(f"{app} closed at {end_time} | duration: {duration}")

            # exit condition
            # write return value to a file before returning
            if (datetime.now() - start_time).total_seconds() > run_time:
                session_apps_log.append((app,start_time,end_time,duration))
                # write here
                return session_apps_log
        ti.sleep(0.5)


# tested


