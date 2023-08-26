import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Hp/Desktop"

class FileEvenHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"the file {event.src_path} has been created")

    def on_deleted(self, event):
        print(f"the file has been deleted ")

    def on_modified(self, event):
        print(f"the file has been modified ")
    
    def on_moved(self, event):
        print(f"the file has been moved ")

observer = Observer()
eventHandler = FileEvenHandler()
observer.schedule(eventHandler,from_dir,recursive = True)
observer.start()
try: 
    while True:
        time.sleep(2)
        print("runnig...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

