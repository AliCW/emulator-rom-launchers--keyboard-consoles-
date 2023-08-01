start "" /d "<path-to-emulator>" cmd /C <emulator.exe> %1

start "" /d "<path-to-emulator>" cmd /C <pythonFile.py> 


:: change both; the path the emulator & the names of the emulator.exe & pythonFile.py to match your setup     

:: The Above 'start "" /d' combination opens seperate CMD windows for the execution as the emulator needs to start seperatly due to the serial running of the batch file
:: really this should be done in powershell