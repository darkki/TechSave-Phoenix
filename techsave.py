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
    name = "TechSave Phoenix"
    version = "13052020|Dev"
    by = "darkk!"

class component:
    def __init__(self, priority, type, url, name, price):
        self.log(f"new component created! - [{priority}] {price}e | {type} / {name} / {url}")
        self.priority = priority
        self.type = type
        self.url = url
        self.name = name
        self.price = price
    def log(self, message):
        log_append = open("log.txt", "a")
        log_append.write(f"[ {date_time_now} ] - [ {message} ]\n")
        log_append.close()

class money:
    def __init__(self, balance):
        self.log(f"new balance set, with value of {balance}e")
        self.balance = balance
    def log(self, message):
        log_append = open("log.txt", "a")
        log_append.write(f"[ {date_time_now} ] - [ {message} ]\n")
        log_append.close()
    def add_money(self, money_added, message = "no message given"):
        self.balance += int(money_added)
        self.log(f"money added! - added: {money_added}e / new total: {self.balance}e - message: {message}")
        return(f"money added! - added: {money_added}e / new total: {self.balance}e - message: {message}")
    def withdraw_money(self, money_withdrawn, message = "no message given"):
        self.balance -= int(money_withdrawn)
        self.log(f"money withdrawn! - withdrawm: {money_withdrawn}e / new total: {self.balance}e - message: {message}")
        return(f"money withdrawn! - withdrawm: {money_withdrawn}e / new total: {self.balance}e - message: {message}")
    def get_balance(self):
        return(self.balance)

def log(message):
    log_append = open("log.txt", "a")
    log_append.write(f"[ {date_time_now} ] - [ {message} ]\n")

tic = time.time()
print(f"[{Fore.CYAN}\tsp\init{Style.RESET_ALL}] beginning {app_info.name} v{app_info.version} initialization ... [{Fore.GREEN}READY{Style.RESET_ALL}]")
print(f"[{Fore.CYAN}\tsp\init\data_load\check{Style.RESET_ALL}] checking if .\data.tsp exists ... ", end="")
if path.isfile("./data.tsp") == True:
    print(f"[{Fore.GREEN}FOUND{Style.RESET_ALL}]")
    print(f"[{Fore.CYAN}\tsp\init\data_load\load{Style.RESET_ALL}] loading .\data.tsp ... ", end="")
    tsp_dict = pickle.load(open("./data.tsp", "rb"))
    print(f"[{Fore.GREEN}OK{Style.RESET_ALL}]")
else:
    print(f"[{Fore.RED}NOT_FOUND{Style.RESET_ALL}]")
    print(f"[{Fore.CYAN}\tsp\init\data_create\init{Style.RESET_ALL}] initializing default values  ... ", end="")
    tsp_dict = {}
    tsp_dict["components"] = []
    tsp_dict["finances"] = money(0)
    print(f"[{Fore.GREEN}OK{Style.RESET_ALL}]")
    print(f"[{Fore.CYAN}\tsp\init\data_create\save{Style.RESET_ALL}] saving .\data.tsp ... ", end="")
    pickle.dump(tsp_dict, open("./data.tsp", "wb"))
    print(f"[{Fore.GREEN}OK{Style.RESET_ALL}]")
toc = time.time()
tictoc = round(toc - tic, 2)
print(f"[{Fore.CYAN}\tsp\init{Style.RESET_ALL}] initialization completed in {Style.BRIGHT}{tictoc}s{Style.RESET_ALL}, welcome to {Style.BRIGHT}{app_info.name} v{app_info.version} {Style.RESET_ALL}by {Style.BRIGHT}{app_info.by}{Style.RESET_ALL}")