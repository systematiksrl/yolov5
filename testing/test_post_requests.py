import requests
import random as rnd


URL_INTERFACE = 'http://192.168.1.7:8181/api/update'

FILEPATH_PROCESSED = 'yolov5'
id_pezzo = rnd.randint(0,10)
id_lavorazione = rnd.randint(0,10)
FRAGMENT_ID = rnd.randint(0,10)
DIFECTS_FOUND = str(rnd.randint(0,10)) + ' fori'

dic = {'originale': {'path': FILEPATH_PROCESSED,'id_lavorazione':id_lavorazione, 'id_pelle':id_pezzo ,'numero_frammento_pelle':FRAGMENT_ID },
'elaborata':  {'path': FILEPATH_PROCESSED,'id_lavorazione':id_lavorazione, 'id_pelle':id_pezzo ,'numero_frammento_pelle':FRAGMENT_ID,'numero_difetti_trovati' : DIFECTS_FOUND}}

dic2 = {'originale': {'path': FILEPATH_PROCESSED,'id_lavorazione':id_lavorazione, 'id_pelle':id_pezzo ,'numero_frammento_pelle':FRAGMENT_ID }}

call = requests.post(URL_INTERFACE, json = dic)
print(call.json())