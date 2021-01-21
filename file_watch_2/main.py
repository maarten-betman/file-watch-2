import sys
import time

from watchdog.events import PatternMatchingEventHandler, FileSystemEvent
from watchdog.observers import Observer

import logging

logging.basicConfig(
    filename="../file-events.log",
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)


class EventHandlerGef(PatternMatchingEventHandler):
    def on_any_event(self, event: FileSystemEvent):
        logging.debug(" | ".join(["GEF Folder", event.event_type, event.src_path]))


class EventHandlerAgs(PatternMatchingEventHandler):
    def on_any_event(self, event: FileSystemEvent):
        logging.debug(" | ".join(["BH Folder", event.event_type, event.src_path]))


event_handler_gef = EventHandlerGef(
    patterns=["*.gef", "*.pdf"],
    ignore_directories=True,
)

event_handler_ags = EventHandlerAgs(
    patterns=["*.ags", "*.pdf"],
    ignore_directories=True,
)

observer = Observer()

observer.schedule(
    event_handler_gef,
    r"T:\08_General\Tekong_Project\0.1 Soil Investigation\(001) Progress Report\Cone Penetration Test (CPT)",
    recursive=True,
)

observer.schedule(
    event_handler_ags,
    r"T:\08_General\Tekong_Project\0.1 Soil Investigation\(001) Progress Report\Borehole (BH)",
    recursive=True,
)


observer.start()
logging.log(logging.DEBUG, "Started logging.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    logging.log(logging.DEBUG, "Stopped logging.")
finally:
    observer.join()
