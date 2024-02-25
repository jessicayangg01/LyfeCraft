

INSTALL PYGAME
python3 -m pip install -U pygame


INSTALL SOUND
python3 -m pip install playsound

if run into error with playsound
python3 -m pip install --upgrade wheel

if it still doesnt work
( error is The specified device is not open or is not recognized by MCI)
Error 259 for command:
        play "assets\audio\backgroundMusic.mp3" wait
    The driver cannot recognize the specified command parameter.
python3 -m pip uninstall playsound
python3 -m pip install playsound==1.2.2


INSTALL EXCEL
python3 -m pip install openpyxl

# note for myself
python3 -m pip install ...