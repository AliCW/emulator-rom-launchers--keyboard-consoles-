start "" /d "<path-to-CPC-emulator>" cmd /C caprice64.exe %1

start "" /d "<path-to-CPC-emulator>" cmd /C pythonAmstradCommandEmulator.py


::/C      Carries out the command specified by string and then terminates
::/d	  Disable execution of AutoRun commands from registry

:: The Above 'start "" /d' combination opens seperate CMD windows for the execution as the emulator needs to start seperatly due to the serial running of the batch file
:: really this should be done in powershell