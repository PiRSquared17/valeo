from Tkinter import Tk
from gui import EditBoxWindow
import sys

def run_user_code(envdir):
    source = raw_input(">>> ")
    try:
        exec source in envdir
    except:
        tk = Tk()
        app = EditBoxWindow(tk)
        ui = sys.exc_info()[:2]
        body = app.edit(ui)

envdir = {}
while 1:
    run_user_code(envdir)
