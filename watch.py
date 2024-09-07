from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import pyperclip
import time
import tinycss2
import re
import urllib.parse
from app.classname import class_generate
from lib.classes_gen.parse_config import remove_occurrences

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = time.time()
        self.recent_value = ""

    def on_modified(self, event):
        if not event.is_directory and os.path.basename(event.src_path) == "tailwind.txt":
            current_time = time.time()
            if current_time - self.last_modified < 1:  # less than one second
                return
            self.last_modified = current_time
            class_generate(refer='txt_file')


    def css_validation(self, css_string):
        css_string = remove_occurrences(css_string)
        parsed = tinycss2.parse_declaration_list(css_string)

        for decl in parsed:
            if decl.type == 'declaration' and not decl.name.startswith('--'):
                return True
        return False


    def on_copy(self):
        clipboard_content = pyperclip.paste()
        if len(clipboard_content.strip()) >= 1:
            return clipboard_content
        else:
            return None

    def monitor_clipboard(self):
        while True:
            current_value = pyperclip.paste()
            if current_value != self.recent_value:
                self.recent_value = current_value

                value = self.on_copy()
                if value and self.css_validation(value):
                    class_generate(refer="clipboard")

            time.sleep(0.5)

if __name__ == "__main__":
    observer = Observer()
    event_handler = FileChangeHandler()
    path_to_watch = '.'  # watches the current directory
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    # Execute when copy to clipboard
    event_handler.monitor_clipboard()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
