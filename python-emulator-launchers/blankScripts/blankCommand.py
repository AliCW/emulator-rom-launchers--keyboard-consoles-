import time #used to pause script execution steps
import win32con #used to cancel keypresses
import win32api #used to send keypresses
#script needs to be in the same directory as the emulator .exe or .bat file

def runGame():
    time.sleep(5)#waits for emu to start - very crude


    # you can copy the below three lines to create your own command structure
    # stack these on top of each other to create the command string and enter it into the emulator (if required)

    win32api.keybd_event(0, 0, 0, 0) # presses a key - change the first value to desired key's decimal value
    time.sleep(0.1) # waits for the key to appear
    win32api.keybd_event(0, 0, win32con.KEYEVENTF_KEYUP, 0)#releases key - change to corresponding above value




    # Below presses '.exe' & presses enter - delete or change if required

    win32api.keybd_event(190, 0, 0, 0) #(.)
    time.sleep(0.1)
    win32api.keybd_event(190, 0, win32con.KEYEVENTF_KEYUP, 0)#releases (.)
    win32api.keybd_event(69, 0, 0, 0) #(E)
    time.sleep(0.1)
    win32api.keybd_event(69, 0, win32con.KEYEVENTF_KEYUP, 0)#releases (E)
    win32api.keybd_event(88, 0, 0, 0) #(x)
    time.sleep(0.1)
    win32api.keybd_event(88, 0, win32con.KEYEVENTF_KEYUP, 0)#releases (x)
    win32api.keybd_event(69, 0, 0, 0) #(E)
    time.sleep(0.1)
    win32api.keybd_event(69, 0, win32con.KEYEVENTF_KEYUP, 0)#releases (E)

    win32api.keybd_event(13, 0, 0, 0) #(Enter)
    time.sleep(0.1)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)#releases (Enter)



runGame()