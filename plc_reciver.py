import os
import socket
import time
import random as rnd
from sys import platform
from datetime import datetime
from colorama import Fore, Style
from app_config import PLC_IP, PLC_PORT

'''
SIMULATORE socket di PLC
socket ad utilizzo di test come sostituto al PLC.    
'''

import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((PLC_IP, PLC_PORT))
serv.listen(1)
while True:
    conn, addr = serv.accept()
    from_client = ''
    data_from_client = conn.recv(4096)
    if str(data_from_client) not in [str(b''),"b''",None,False]:
        print(f"data received: {data_from_client}")
    
    conn.close()
    