import datetime # module imported for date/time
date_time_now = datetime.datetime.now()
import time # module imported for tictoc

import operator # module imported for sorting dictionaries

from colorama import init # module imported for color support
init()
from colorama import Fore,Back,Style

import os # module imported for checking if file exists and system functions
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

tic = time.time() # Initialization starts
print(f"[{Fore.CYAN}tsp/init{Style.RESET_ALL}] beginning {app_info.name} v{app_info.version} initialization ... [{Fore.GREEN}READY{Style.RESET_ALL}]")
print(f"[{Fore.CYAN}tsp/init/data_check{Style.RESET_ALL}] checking if {Style.BRIGHT}./data.tsp{Style.RESET_ALL} exists ... ", end="")
if path.isfile("./data.tsp") == True:
    print(f"[{Fore.GREEN}FOUND{Style.RESET_ALL}]")
    print(f"[{Fore.CYAN}tsp/init/data_load{Style.RESET_ALL}] loading {Style.BRIGHT}./data.tsp{Style.RESET_ALL} ... ", end="")
    tsp_dict = pickle.load(open("./data.tsp", "rb"))
    print(f"[{Fore.GREEN}OK{Style.RESET_ALL}]")
else:
    print(f"[{Fore.RED}NOT_FOUND{Style.RESET_ALL}]")
    print(f"[{Fore.CYAN}tsp/init/data_create{Style.RESET_ALL}] initializing default values  ... ", end="")
    tsp_dict = {}
    tsp_dict["components"] = []
    tsp_dict["finances"] = money(0)
    print(f"[{Fore.GREEN}OK{Style.RESET_ALL}]")
    print(f"[{Fore.CYAN}tsp/init/data_save{Style.RESET_ALL}] saving {Style.BRIGHT}./data.tsp{Style.RESET_ALL} ... ", end="")
    pickle.dump(tsp_dict, open("./data.tsp", "wb"))
    print(f"[{Fore.GREEN}OK{Style.RESET_ALL}]")
toc = time.time()
tictoc = round(toc - tic, 3)
print(f"[{Fore.CYAN}tsp/init{Style.RESET_ALL}] initialization completed in {Style.BRIGHT}{tictoc}s{Style.RESET_ALL}, welcome to {Style.BRIGHT}{app_info.name} v{app_info.version} {Style.RESET_ALL}by {Style.BRIGHT}{app_info.by}{Style.RESET_ALL}")
print(f"[{Fore.CYAN}tsp/init/main_menu{Style.RESET_ALL}] press [{Fore.MAGENTA}ENTER{Style.RESET_ALL}] to enter {Fore.BLUE}main menu{Style.RESET_ALL}: ", end="")
# input() #! remember to activate this when finished!
os.system("cls")

def menumaker(current_menu, width, selection_1 = "not in use", selection_2 = "not in use", selection_3 = "not in use", selection_4 = "not in use", selection_5 = "not in use", selection_6 = "not in use"):
    header_line = "] " + app_info.name + " v" + app_info.version + " by " + app_info.by + " ["
    header_line = header_line.center(width, "-")
    footer_line = "] " + "NZTi!" + " ["
    footer_line = footer_line.center(width, "-")
    print(header_line + "\n")
    selection_list = [selection_1, selection_2, selection_3, selection_4, selection_5, selection_6]
    command_list = []
    for selection_idx in range(1, len(selection_list) + 1):
        selection_print = selection_list[selection_idx - 1]
        if selection_list[selection_idx - 1] == "not in use":
            pass
        else:
            print(f"    [{Fore.MAGENTA}{selection_idx}{Style.RESET_ALL}] {Style.BRIGHT}-->{Style.RESET_ALL} {Fore.BLUE}{selection_print}{Style.RESET_ALL}")
            command_list.append("null")
    print("\n" + footer_line + "\n")
    print(f"[{Fore.CYAN}tsp/{current_menu}/cmd{Style.RESET_ALL}] you are in {Fore.BLUE}{current_menu}{Style.RESET_ALL}, enter your command [{Fore.MAGENTA}1-{len(command_list)}{Style.RESET_ALL}]: ", end="")
    return_var = input()
    return(return_var)

menumaker("main_menu", 80, "variable_menu", "stranger_things_menu", "jeejee_menu")