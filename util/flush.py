import os
import platform

def flush_screen():
    system_name = platform.system()
    executor = ''

    match system_name:
        case 'Linux' | 'Darwin':
            executor = 'clear'
        case 'Windows':
            executor = 'cls'

    os.system(executor)