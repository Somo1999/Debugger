from ctypes import *
from _winapi import CREATE_NEW_CONSOLE
from ctypes.wintypes import DWORD, WORD, LPBYTE, HANDLE
from asyncio.events import Handle

WORD    = c_ushort
DWORD   = c_ulong
LPBYTE  = POINTER(c_ubyte)
LPTSTR  = POINTER(c_char)
HANDLE  = c_void_p
LPVOID  = POINTER(c_void_p)
BOOL    = c_short
LPCWSTR = POINTER(c_wchar)
LPWSTR  = POINTER(c_char)


DEBUG_PROCESS =0x00000001
CREATE_NEW_CONSOLE =0x00000010

class STARTUPINFO(Structure):
    __fields__=[
        ("cb",              DWORD  ),
        ("lpReserved",      LPTSTR ),
        ("lpDesktop",       LPTSTR ),
        ("lpTitle",         LPTSTR ),
        ("dwX",             DWORD  ),
        ("dwY",             DWORD  ),
        ("dwXSize",         DWORD  ),
        ("dwYSize",         DWORD  ),
        ("dwXCountChars",   DWORD  ),
        ("dwYCountChars",   DWORD  ),
        ("dwFillAttribute", DWORD  ),
        ("dwFlags",         DWORD  ),
        ("wShowWindow",     WORD   ),
        ("cbReserved2",     WORD   ),
        ("lpReserved2",     LPBYTE ),
        ("hStdInput",       HANDLE ),
        ("hStdOutput",      HANDLE ),
        ("hStdError",       HANDLE ),
    ]

class PROCESS_INFORMATION(Structure):
    __fields__=[
        ("hprocess",    HANDLE),
        ("hThread",     HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId",  DWORD),
    ]    

class SECURITY_ATTRIBUTES(Structure):
    __fields__ = [
        ('nLength', DWORD),
        ('lpSecurityDescriptor', LPVOID),
        ('bInheritHandle', BOOL)
    ]
    

    