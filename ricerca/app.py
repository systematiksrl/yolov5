import time
from subprocess import Popen, PIPE
from colorama import Fore, Style
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from sys import platform
from datetime import datetime

def get_id_from_path(filepath_):
    if platform == 'win32':
        result = filepath_.split('\\')[-1]    
    else:
        result = filepath_.split('/')[-1]
    if '_' in result:
        id = result.split('_')[0].replace('img','')
    else:
        id = result.replace('img','').split('.')[0]
    return id 
  
class OnMyWatch:
    # Set the directory on watch
    from config_app import watchDirectory

    def __init__(self):
        self.observer = Observer()
  
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()


class Handler(FileSystemEventHandler):
    '''
    types = ['created', 'deleted', 'modified', 'moved', 'closed']
    '''
    @staticmethod
    def on_any_event(event):

        if event.is_directory:
            return None
        
        if event.event_type == 'created':
            id_pezzo = get_id_from_path(event.src_path)            

            if platform == 'win32':
                cmd = f"python3 detect.py --weights best.pt --data data\dataset.yaml --img 1280 --id_pezzo {id_pezzo} --conf 0.25 --source {event.src_path}"    
            else:
                cmd = f"python3 detect.py --weights best.pt --data data/dataset.yaml --img 1280 --id_pezzo {id_pezzo} --conf 0.25 --source {event.src_path}"

            process = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()

            print('-'*80)
            print(f'elaborazione ID: {id_pezzo} ')
            print(datetime.now())
            #print(f'{stderr}')

if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()