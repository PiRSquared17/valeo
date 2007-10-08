from _winreg import *
Reg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
Key = OpenKey(Reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
try:   
   SetValueEx(Key,"Nome do Programa", 0, REG_SZ, r"\caminho\do\programa\arquivo a executar")
   print "Program installed in your Windows Registry."
except EnvironmentError:                                          
    print "Problems writing Registry..."
CloseKey(Key)
CloseKey(Reg)
