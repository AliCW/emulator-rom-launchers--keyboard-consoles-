import time #used to pause script execution steps
import win32con #used to cancel keypresses
import win32api #used to send keypresses
#script needs to be in the same directory as the emulator .exe or .bat file

def runCpcCmd():#types CAT, return, RUN"
    time.sleep(5)#waits for emu to start - very crude - use PID .py thing
    win32api.keybd_event(67, 0, 0, 0) # (C) presses the key - accepts unicode values
    time.sleep(0.1)#waits for emu to accept the key
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)#releases the key (C) - uses 'win32con.KEYEVENTF_KEYUP' to perform this
    win32api.keybd_event(65, 0, 0, 0,)# (A)
    time.sleep(0.1)
    win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)#release (A)
    win32api.keybd_event(84, 0, 0, 0)# (T)
    time.sleep(0.1)
    win32api.keybd_event(84, 0, win32con.KEYEVENTF_KEYUP, 0)#relrease (T)
    win32api.keybd_event(13, 0, 0, 0)  # (ENTER) - execute
    time.sleep(0.1)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)#releases (Enter)
    time.sleep(3)
    win32api.keybd_event(82, 0, 0, 0) #(R)
    time.sleep(0.1)
    win32api.keybd_event(82, 0, win32con.KEYEVENTF_KEYUP, 0)#releases (R)
    win32api.keybd_event(85, 0, 0, 0) #(U)
    time.sleep(0.1)
    win32api.keybd_event(85, 0, win32con.KEYEVENTF_KEYUP, 0)#releases (U)
    win32api.keybd_event(78, 0, 0, 0) #(N)
    time.sleep(0.1)
    win32api.keybd_event(78, 0, win32con.KEYEVENTF_KEYUP, 0)#releases (N)
    win32api.keybd_event(16, 0, 0, 0) #(Lshift) 
    win32api.keybd_event(50, 0, 0, 0) #(2) = "
    time.sleep(0.1)
    win32api.keybd_event(50, 0, win32con.KEYEVENTF_KEYUP, 0)#releases [2] (")
    win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)#releases (Lshift)

runCpcCmd()

