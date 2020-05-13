import datetime # module imported for date/time
date_time_now = datetime.datetime.now()
import time # module imported for tictoc

import operator # module imported for sorting dictionaries

from colorama import init # module imported for color support
init()
from colorama import Fore,Back,Style

import os # module imported for checking if file exists
from os import path

import pickle # module imported for loading/saving dictionaries/objects

class app_info: # basic app info like version
    version = "13052020|Dev"
    by = "darkk!"

class component:
    def __init__(self, priority, type, url, name, price):
        self.log(f"new component created! - [{priority}] {price}€ | {type} / {name} / {url}")
        self.priority = priority
        self.type = type
        self.url = url
        self.name = name
        self.price = price
    def log(self, message):
        log_append = open("log.txt", "a")
        log_append.write(f"[ {date_time_now} ] - [ {message} ]\n")
        log_append.close()