import os
import time
import socket
import random as rnd
from sys import platform
from datetime import datetime
from colorama import Fore, Style
from app_config import PLC_IP, PLC_PORT

def save_message(message='test',directory='messages.txt'):   
<<<<<<< Updated upstream
    """
    append the message to the text file indicated as 
    Path in the directory variable
    """
    with open(directory, '+a') as f:       
        f.writelines(message + '\n')

=======
    with open(directory, '+a') as f:   
        f.writelines( str(message) +'\n')
0
>>>>>>> Stashed changes
if __name__ == "__main__":
    '''
    PLC socket simulator socket for test use as a substitute for the PLC.
    
    read messages written by server.py
    which reads the messages from the AI server
    and save the message with the AI results.
    '''
    print('Starting PLC RECIVER simulator...')
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((PLC_IP, PLC_PORT))
    serv.listen(1)

    while True:
        conn, addr = serv.accept()
        from_client = ''
        data_from_client = conn.recv(4096)

        if str(data_from_client) not in [str(b''),"b''",None,False]:
            if platform == "linux" or platform == "linux2":
                os.system('clear')
            elif platform == "win32":
                os.system('cls')
            print('\n\n\t '+Fore.RED +'PLC RECIVER SIMULATOR'+ Style.RESET_ALL)
            print('\n\t Status server: \t\t'+Fore.GREEN +'[ONLINE]'+ Style.RESET_ALL)
            current_time = datetime.now().strftime("%H:%M:%S")
            print('\n\t Current Time: \t\t\t'+Fore.YELLOW  +str(current_time) + Style.RESET_ALL)
            print("\n\t data received: \t\t"+Fore.BLUE +str(data_from_client)+ Style.RESET_ALL)

            save_message( message = data_from_client , directory = 'defects_founded.txt')
            
        conn.close()