import dbus
import time

# Gets one instance the time since last input 

def getIDLETIMEsinceLastInput():
    bus = dbus.SessionBus()

    obj = bus.get_object(
        "org.gnome.Mutter.IdleMonitor",
        "/org/gnome/Mutter/IdleMonitor/Core"
    )

    iface = dbus.Interface(
        obj,
        "org.gnome.Mutter.IdleMonitor"
    )

    idle_ms = iface.GetIdletime()

    return idle_ms/1000



if __name__=="__main__":
    while True:
        print(getIDLETIMEsinceLastInput())
        time.sleep(1)

