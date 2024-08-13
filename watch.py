import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import sys

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = time.time()

    def on_modified(self, event):
        if not event.is_directory and os.path.basename(event.src_path) == "tailwind.txt":
            current_time = time.time()
            if current_time - self.last_modified < 1:  # less than one second
                return
            self.last_modified = current_time
            subprocess.run([sys.executable, "classes_gen.py"])


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileChangeHandler()
    path_to_watch = '.'  # watches the current directory
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
