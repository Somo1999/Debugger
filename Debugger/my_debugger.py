from ctypes import *
from my_debugger_defines import *
from builtins import *

kernel32 = windll.kernel32
kernel32.restype = BOOL

LPSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)
LPSTARTUPINFOW = POINTER(STARTUPINFO)
LPPROCESS_INFORMATION = POINTER(PROCESS_INFORMATION)

kernel32.CreateProcessW.argtypes = (LPCWSTR,
                                    LPWSTR,
                                    LPSECURITY_ATTRIBUTES,
                                    LPSECURITY_ATTRIBUTES,
                                    BOOL,
                                    DWORD,
                                    LPVOID,
                                    LPCWSTR,
                                    LPSTARTUPINFOW,
                                    LPPROCESS_INFORMATION)

class debugger():
    def __init__(self):
        pass
    
    
    def load(self,path_to_exe):
        
        creation_flags = DEBUG_PROCESS
        
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()
        
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        
        if kernel32.CreateProcessW(path_to_exe,
                                  None,
                                  None,
                                  None,
                                  False,
                                  creation_flags,
                                  None,
                                  None,
                                  byref(startupinfo),
                                  byref(process_information)
                                  ):
            
            print("[*]We have successfully Launched into the Process\n")
            print("PID = %d" % process_information.dwProcessId)
            
        else:
            print ("[*] Error: {}".format(kernel32.GetLastError()) )