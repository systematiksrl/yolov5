import os
import socket
import time
from colorama import Fore, Style
from datetime import datetime
from app_config import SERVER_IP, SERVER_PORT, FILEPATH_PLC_MESSAGES,platform

def save_message(message='test',directory='messages.txt'):   
    """
    append the message to the text file indicated as 
    Path in the directory variable
    """
    with open(directory, '+a') as f:       
        f.writelines(message + '\n')

def main():
    """
    connect to IPv4 socket as a data stream
    if I receive data from the socket and
    if there is an 'f' inside this data,
    then I have to save the message that
    acts as a photo processing and saving command for the AI
    """
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySocket.bind((SERVER_IP, SERVER_PORT))
    payload = None

    while True:
        try:
            payload, client_address = mySocket.recvfrom(1024)
            print(datetime.now())
            print(payload)

            if 'f' in str(payload)[2]:
                #id_pezzo = str(payload).split(',')[1]
                if platform == "linux" or platform == "linux2":
                    os.system('clear')
                elif platform == "win32":
                    os.system('cls')
            
                current_time = datetime.now().strftime("%H:%M:%S")
                print('\n\n\t '+Fore.RED +'SERVER message handler'+ Style.RESET_ALL)

                print('\n\t Status server: \t\t'+Fore.GREEN +'[ONLINE]'+ Style.RESET_ALL)
                print('\n\t Current Time: \t\t\t'+Fore.YELLOW  +str(current_time) + Style.RESET_ALL)
                print('\n\t New message from PLC: \t\t'+Fore.CYAN +str(payload) + Style.RESET_ALL )
                save_message( message = payload.decode() , directory = FILEPATH_PLC_MESSAGES)
            
            payload = None
        
        except KeyboardInterrupt:
            print("press control-c again to quit")
            time.sleep(1)
            exit()

if __name__ == '__main__':
    main()