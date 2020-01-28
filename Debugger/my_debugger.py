from ctypes import *
from my_debugger_defines import *
from builtins import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass
    
    def load(self,path_to_exe):
        
        creation_flags = 0x00000001
        
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()
        
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)
                                   ):
            
            print("[*]We have successfully Launched into the Process\n")
            print("PID = %d" % process_information.dwProcessId)
            
        else:
            print ("[*]Error: 0x%o8x." % kernel32.GetLastError())    