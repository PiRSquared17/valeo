# -*- coding: utf-8 -*-

import time, sys
if sys.platform == "win32":
    from winsound import Beep
    beep = True
from tkMessageBox import showinfo

###### Preferences ######

# Hours
pref_h = '15'

# Minutes
pref_m = '00'

# Your alerts: beep, dialog
alert = "dialog"
# Todo: fullscreen, notification

########## Main ##########

hora = time.strftime("%H", time.localtime())
minu = time.strftime("%M", time.localtime())

def Alarm():
    hora = time.strftime("%H", time.localtime())
    minu = time.strftime("%M", time.localtime())
    if (hora == pref_h and minu == pref_m):
        if alert == "beep":
            if beep == True:
                Beep(1200, 250)
                
        elif alert == "dialog":
            showinfo('Live Alarm', u'''\
Live Alarm

Now are %s:%s hrs''' % (pref_h, pref_m))

        elif alert == "fullscreen":
            pass
        
        elif alert == "notification":
            pass
        
        sys.exit()
    else:
        time.sleep(20)
        Alarm()

if __name__ == "__main__":
    Alarm()
