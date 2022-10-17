filepaths = ["/home/kobayashi/Documents/job/yolov5/images/img1_2.txt",
"/home/kobayashi/Documents/job/yolov5/images/img2_1.pdf",
"/home/kobayashi/Documents/job/yolov5/images/img3.jpg",
"/home/kobayashi/Documents/job/yolov5/images/img4_2.png",
"/home/kobayashi/Documents/job/yolov5/images/img5_0.jpeg"]


def get_id_from_path(filepath_):
    result = filepath_.split('/')[-1]
    if '_' in result:
        id = result.split('_')[0].replace('img','')
    else:
        id = result.replace('img','').split('.')[0]
    return id

# for p in filepaths:
#     id = get_id_from_path(filepath_=p)
#     print(id)


def scrivi_messaggio(message='test',directory='messages.txt'):
        with open(directory, '+a', errors='ignore') as f:
                f.write(message+'\n')


scrivi_messaggio(message='example',directory='messages.txt')

def leggi_e_rimuovi_messaggio(directory='messages.txt'):
    with open(directory, 'r', errors='ignore') as f:
        data = f.read()
    
    print(data)

    if data:
        with open(directory, 'w+', errors='ignore') as f:
            f.write('')
            print('removing')
    return data

leggi_e_rimuovi_messaggio(directory='messages.txt')


def get_id_from_path(filepath_):
    return filepath_.split('/')[-1]

#get_id_from_path(filepath_=filepath)