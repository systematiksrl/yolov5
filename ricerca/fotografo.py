import sys
import time
import argparse
import os
import time
import sys
import numpy as np
import cv2
from config_app import CARTELLA_FOTOGRAFIE, RISOLUZIONE, ROOT_PATH
                                       
def logo_fotografo():
    LOGO = """
        📸 Fotografo Systematik s.r.l.
    """
    print(LOGO)

def empty(a):
    pass

def gamma_trans(img, gamma):
    gamma_table=[np.power(x/255.0,gamma)*255.0 for x in range(256)]
    gamma_table=np.round(np.array(gamma_table)).astype(np.uint8)
    return cv2.LUT(img,gamma_table)

if __name__ == "__main__":
    """
    visualizza la foto, potendola modificare dal vivo e salvala se e' arrivato un nuovo messaggio
    """
    nome_pannello_di_controllo =  'test'
    nome_pannello_di_visualizzazione =  'test'
    images_folders = sys.path[0]+'/images'

    parser = argparse.ArgumentParser(description='Test fotografie ad intervalli regolari con tutti i tipi di videocamere disponibili per OpenCV')

    parser.add_argument('--porta_usb', type = int, required=False , default = 0 , help = "numero porta usb del dispositivo")                                # ID PORTA USB DISPOSITIVO
    parser.add_argument('--nome_cartella', type = str, required=False, default = "viz", help="nome cartella esistente dentro img/ dove salvare le foto")  # nome cartella img in cui salvare le foto
    parser.add_argument('--intervallo_secondi', type = float, default = 1.0 , help="intervallo di secondi fra due fotografie")     
    parser.add_argument('--salva', type = float, default = True , help="salva le fotografie")     
    parser.add_argument('--visualizza', type = float, default = True , help="visualizza o meno l'immagine in tempo reale")     
    args = parser.parse_args()


    if not os.path.exists(images_folders):
        os.makedirs(images_folders)
        
    newpath = images_folders+"/"+ args.nome_cartella 

    if not os.path.exists(newpath):
        os.makedirs(newpath)
        
    # Inserisci 1 e connetti la videocamera al computer tramite USB
    # se non funziona prova tutte le porte USB lanciando questo script.
    KEY_USB = args.porta_usb
    CARTELLA = args.nome_cartella
    INTERVALLO_SECONDI = args.intervallo_secondi

    # inizializza l'oggetto videocamera
    cap = cv2.VideoCapture(KEY_USB)

    # risoluzione 12.3 MegaPixels
    cap.set(3, RISOLUZIONE[0])  # Set horizontal resolution
    cap.set(4, RISOLUZIONE[1])  # Set vertical resolution

    time.sleep(0.2)

    i = 0 # contatore salva foto
    plc_data = None

    cv2.namedWindow(nome_pannello_di_controllo)
    cv2.resizeWindow(nome_pannello_di_controllo, RISOLUZIONE[0], RISOLUZIONE[1])

    # inizializza la trackbar con i vari parametri ed i loro massimi o minimi
    cv2.createTrackbar("fps", nome_pannello_di_controllo, 5, 20, empty)
    cv2.setTrackbarMin('fps', nome_pannello_di_controllo, 1)
    cv2.createTrackbar("gamma", nome_pannello_di_controllo, 100, 200, empty)
    cv2.setTrackbarMin('gamma', nome_pannello_di_controllo, 1)
    cv2.createTrackbar("size_frame_x", nome_pannello_di_controllo, 500, 2400, empty)
    cv2.setTrackbarMin('size_frame_x', nome_pannello_di_controllo, 200)
    cv2.createTrackbar("size_frame_y", nome_pannello_di_controllo, 300, 1080, empty)
    cv2.setTrackbarMin('size_frame_y', nome_pannello_di_controllo, 100)

    while True:
        #cattura frame per frame dalla videocamera
        ret, frame = cap.read()

        # se ret non è uguale a True, esci dall'loop
        if not ret:
            print("impossible ricevere immagini dalla videocamera")
            time.sleep(2)

        if args.visualizza:
            FPS = cv2.getTrackbarPos("fps", nome_pannello_di_controllo)        
            video_gamma = cv2.getTrackbarPos("gamma", nome_pannello_di_controllo)
            video_size_x = cv2.getTrackbarPos("size_frame_x", nome_pannello_di_controllo)
            video_size_y = cv2.getTrackbarPos("size_frame_y", nome_pannello_di_controllo)

            frame = cv2.resize(frame, (video_size_x, video_size_y), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
            frame = gamma_trans(frame, video_gamma/100)
            cv2.imshow(nome_pannello_di_visualizzazione, frame)
            cv2.waitKey(1) # wait until user hits any key on keyboard
        
        if args.salva:
            if os.path.exists(ROOT_PATH + PATH_MESSAGGI):
                with open(ROOT_PATH + PATH_MESSAGGI, "r") as f:
                    for idx ,line in enumerate(f.readlines()):
                        if idx == 1:
                            plc_data = str(line)
                            print(plc_data)

                with open(ROOT_PATH + PATH_MESSAGGI, "w+") as f:
                    for idx ,line in enumerate(f.readlines()):
                        if idx != 1:
                            f.write(line)
                            print(idx)

                if np.array(frame).any() and plc_data:
                    ID_IMAGE = plc_data.split(',')[1]
                    numero_frame = 0                        
                    path_immagine = ROOT_PATH + CARTELLA_FOTOGRAFIE + "/foto_" + ID_IMAGE + ".png"
                    while os.path.exists(path_immagine):
                        numero_frame += 1
                        path_immagine = f"{ROOT_PATH}{CARTELLA_FOTOGRAFIE}/foto_{str(ID_IMAGE)}_{str(numero_frame)}.png"

                    cv2.imwrite(path_immagine, frame)
                    #os.system('clear')
                    logo_fotografo()
                    print(f"\n\t Photo saved on the following path: \n\t {path_immagine}")
                    print(f"\n\t Reading messages from the following path: \n\t {ROOT_PATH + PATH_MESSAGGI}")
                    print(f"\n\t PLC data {plc_data}")

        time.sleep(1/FPS)
