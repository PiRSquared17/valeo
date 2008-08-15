# -*- coding: utf-8 -*-

import time, sys
if sys.platform == "win32":
    from winsound import Beep
    beep = True
else:
    #todo: linux sound 
    pass

from Tkinter import Tk, Label

##################### User preferences #####################

# Hours
hours = '09'

# Minutes
minutes = '26'

# Your alerts: beep, dialog, fullscreen
#alert = "beep"
alert = "dialog"
#alert = "fullscreen"

############################################################

hours_now = time.strftime("%H", time.localtime())
minutes_now = time.strftime("%M", time.localtime())

def FullScreen(root):

    hora = time.strftime("%H", time.localtime())
    minu = time.strftime("%M", time.localtime())
    
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(True)
    label = Label(root, font=('Verdana, 20'),
                  text='Live Alarm\n\n Now are %s:%s hrs\n\n\n Use "ESC" or "q" to exit.' % (hora, minu),
                  background='red')
    label.pack(expand=True, fill='both', anchor='center')
    root.geometry("%dx%d+0+0" % (w, h))
    root.bind("<Escape>", lambda e: e.widget.quit())
    root.bind("<q>", lambda e: e.widget.quit())

def dialog():
    import tkMessageBox
    tkMessageBox.showwarning('Live Alarm', u'''\
Live Alarm

Now are %s:%s hrs''' % (hours, minutes))

def Alarm():
    hours_now = time.strftime("%H", time.localtime())
    minutes_now = time.strftime("%M", time.localtime())
    
    if (hours_now == hours and minutes_now == minutes):

        if alert == "beep":
            if beep == True:
                Beep(1200, 250)
            else:
                # todo: linux sound
                pass
                
        elif alert == "dialog":
            dialog()
            
        elif alert == "fullscreen":
            if beep == True:
                Beep(1200, 250)
            else:
                # todo: linux sound
                pass
            root = Tk()
            root.focus_set()
            app = FullScreen(root)
            root.mainloop()

    else:
        time.sleep(20)
        Alarm()

if __name__ == "__main__":
    Alarm()
