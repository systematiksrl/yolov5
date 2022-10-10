import socket
import sys
from sys import platform
if platform == "linux" or platform == "linux2":
        div = '/'
elif platform == "win32":
        div = '\\'
else:
        div = ''

ROOT_PATH = sys.path[0]

FILEDIRECTORY_IMAGES = ROOT_PATH + f'{div}originale{div}'
FILEPATH_PLC_MESSAGES = ROOT_PATH + f'{div}messages_from_plc.txt'
watchDirectory = FILEDIRECTORY_IMAGES
SERVER_IP = socket.gethostname()
SERVER_PORT = 8081
PLC_IP = socket.gethostname()
PLC_PORT = 8081
# numero fra 0 e 65535 (di solito le porte non privilegiate sono > 1023)
KEY_USB = 0 # porta USB videocamera
VIDEO_RESOLUTION = (4295,2864) # 12.3 mega pixel
VIDEO_RESOLUTION = (429,286) # VIDEO_RESOLUTION per tests