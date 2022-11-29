import os
import socket
import time
import random as rnd
from sys import platform
from datetime import datetime
from colorama import Fore, Style
from app_config import SERVER_IP, SERVER_PORT


def PLC_sender():
    '''
    PLC socket simulator socket for test use as a substitute for the PLC.
    Generate a random message initializes a socket client that sends the message. 
    Wait for a random time.
    '''
    while True: 
        
        # random message to simulate the PLC message
        MESSAGE = bytes('f,'+str(rnd.randint(100,999))+','+str(rnd.randint(1,100))+',' +str(rnd.randint(1,100)),'utf-8') 
        current_time = datetime.now().strftime("%H:%M:%S")
                
        # initialize the socket with IPv4 and straming socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # sock.bind((PLC_IP, PLC_PORT))
        sock.connect((SERVER_IP, SERVER_PORT))
        sock.send(MESSAGE)
        sock.close()

        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == "win32":
            os.system('cls')

        print('\n\n\t Status socket: '+Fore.GREEN +'\t\t[ONLINE]\n'+ Style.RESET_ALL+'\n\t IP server: \t\t\t'+Fore.YELLOW + SERVER_IP+ ':'+str(SERVER_PORT)+Style.RESET_ALL+'\n\n\t message from PLC: \t\t' + Fore.BLUE  +str(MESSAGE)  + Style.RESET_ALL + '\n\n\t time: \t\t\t\t'+  Fore.YELLOW  +str(current_time) + Style.RESET_ALL)
        
        time.sleep(rnd.randint(minimo_intervallo_di_secondi, massimo_intervallo_di_secondi+1))
        #time.sleep( 5 )

if __name__ == "__main__":
    PLC_sender()
 
    
