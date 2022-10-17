import os
import cv2
import socket
import time
from datetime import datetime
from colorama import Fore, Style
from config_app import KEY_USB,CARTELLA_FOTOGRAFIE,RISOLUZIONE,IP_SERVER, PORTA_SERVER,div, FILE_MESSAGGIO

def scrivi_messaggio(message='test',directory='messages.txt'):
        with open(directory, '+a', errors='ignore') as f:
                f.write(message+'\n')


def salva_immagine(immagine, id, directory=f'images',ext = '.png'):

        if not os.path.exists(directory):
                os.makedirs(directory)
        
        path_immagine = directory+f'img'+id+ext
        
        counter = 0
        while os.path.exists(path_immagine):
                path_immagine = directory+f'{div}img'+id+'_'+str(counter)+ext
                counter += 1
                        
        
        isWritten = cv2.imwrite(path_immagine, immagine)

        if isWritten:
                print(Fore.GREEN +'foto scattata: '+ Style.RESET_ALL + path_immagine+'\n')

def main():

        cap = cv2.VideoCapture(KEY_USB)

        #cap.set(3, RISOLUZIONE[0]) 
        #cap.set(4, RISOLUZIONE[1])  

        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind((IP_SERVER, PORTA_SERVER))

        payload = None

        while True:
                if cap.isOpened():
                        try:
                                payload, client_address = mySocket.recvfrom(1024)

                                print('payload ',payload)
                                print(datetime.now())

                                if 'f' in str(payload)[2]:
                                        ID_PEZZO = str(payload).split(',')[1]

                                        print(Fore.GREEN + f'nuova ID: {ID_PEZZO} '+ Style.RESET_ALL )
                                        ret,frame = cap.read()
                                        
                                        if cv2.waitKey(25) & 0xFF == ord('q'):
                                                break
                                        
                                        if ret:
                                                salva_immagine(frame, ID_PEZZO, directory = CARTELLA_FOTOGRAFIE, ext = '.png')
                                                scrivi_messaggio(message=payload, directory = FILE_MESSAGGIO)

                        except KeyboardInterrupt:
                                print('processo interrotto')
                                time.sleep(2)
                
                else:
                        cap = cv2.VideoCapture(KEY_USB)
                        cap.set(3, RISOLUZIONE[0]) 
                        cap.set(4, RISOLUZIONE[1])  


if __name__ == '__main__':
        main()





        




