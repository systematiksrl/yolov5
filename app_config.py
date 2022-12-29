import socket
import sys
from sys import platform

if platform == "linux" or platform == "linux2":
        div = '/'
elif platform == "win32":
        div = '\\'
else:
        div = ''

difect_types = ['foro', 'goccia']
ROOT_PATH = sys.path[0]
URL_INTERFACE = 'http://192.168.1.7:8181/api/update'

VISUALIZE_DETECTION = False
DIRECTORY_ORIGINAL_IMAGES = ROOT_PATH + f'{div}originale{div}'
DIRECTORY_PROCESSED_IMAGES = ROOT_PATH + f'{div}processati{div}' 

# LINUX
# DIRECTORY_ORIGINAL_IMAGES = '/home/user/photo/originals/'
# DIRECTORY_PROCESSED_IMAGES ='/home/user/photo/processed/'

# WINDOWS
# DIRECTORY_ORIGINAL_IMAGES = 'C:\Windows\photo\originals\'
# DIRECTORY_PROCESSED_IMAGES ='C:\Windows\photo\processed\'

FILEPATH_PLC_MESSAGES = ROOT_PATH + f'{div}messages_from_plc.txt'
watchDirectory = DIRECTORY_ORIGINAL_IMAGES
SERVER_IP = socket.gethostname()
SERVER_PORT = 8081
PLC_IP = socket.gethostname()
PLC_PORT = 8081
# numero fra 0 e 65535 (di solito le porte non privilegiate sono > 1023)
KEY_USB = 0 # porta USB videocamera
VIDEO_RESOLUTION = (4295,2864) # 12.3 mega pixel
VIDEO_RESOLUTION = (429,286) # VIDEO_RESOLUTION per tests