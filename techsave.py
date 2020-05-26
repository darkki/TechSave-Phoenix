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

import random # module imported for randomness

class app_info: # basic app info like version
    name = "TechSave Phoenix"
    version = "23052020|Dev"
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

def flashy_loader(load1, load2, load1_color, load2_color, finished, fin_color, length, pausemin = 0.2, pausemax = 0.4):
    print("[" + load2, end="", flush=True)
    last_load = ""
    firstrun = True
    for idx in range(length):
        if idx % 2 == 0:
            if firstrun == True:
                backstr = (len(load2) + 1) * "\b"
            else:
                backstr = (len(load2) + 2) * "\b"
            firstrun = False
            time.sleep(random.uniform(pausemin, pausemax))
            print(f"{backstr}[{Style.BRIGHT}{load1}{Style.RESET_ALL}]", end="", flush=True)
            last_load = load1
        else:
            firstrun = False
            time.sleep(random.uniform(pausemin, pausemax))
            backstr = (len(load1) + 2) * "\b"
            print(f"{backstr}[{Fore.BLUE}{load2}{Style.RESET_ALL}]", end="", flush=True)
            last_load = load2
    backstr = "\b" * (len(last_load) + 2)
    print(f"{backstr}[{Fore.GREEN}{finished}{Style.RESET_ALL}]          ")

def progress_bar(lenght, finished, pausemin, pausemax):
    barlenght = int(lenght / 2)
    barfill = barlenght * " "
    print(f"[{Fore.GREEN}{barfill}{Style.RESET_ALL}]", end="", flush=True)
    bar_back = (barlenght + 1) * "\b"
    print(f"{bar_back}", end="", flush=True)
    for idx in range(1, lenght + 1):
        # print(f"idx: {idx} | idx_mod: {idx % 2}")
        # if idx == 1:
        #     print(f"")
        # back_needed = 0
        if idx == lenght:
            time.sleep(random.uniform(pausemin, pausemax))
            print(f"{Fore.GREEN}:{Style.RESET_ALL}] - [{Fore.GREEN}DONE!{Style.RESET_ALL}]")
        elif idx % 2 == 1:
            time.sleep(random.uniform(pausemin, pausemax))
            print(f"{Fore.GREEN}.", end="", flush=True)
            # bar_back = back_needed * "\b"
            print(f"\b", end="", flush=True)
        elif idx % 2 == 0:
            time.sleep(random.uniform(pausemin, pausemax))
            print(f"{Fore.GREEN}:", end="", flush=True)

tic = time.time() # Initialization starts
print(f"[{Fore.CYAN}tsp/init{Style.RESET_ALL}] beginning {app_info.name} v{app_info.version} initialization ... ", end="", flush=True)
# flashy_loader("INIT", "INIT", "BLUE", "GREEN", "READY!", "GREEN", 15, 0.1, 0.3) #! activate!
print(f"[{Fore.CYAN}tsp/init/data_check{Style.RESET_ALL}] checking if {Style.BRIGHT}./data.tsp{Style.RESET_ALL} exists ... ", end="")
if path.isfile("./data.tsp") == True:
    print(f"[{Fore.GREEN}FOUND!{Style.RESET_ALL}]")
    print(f"[{Fore.CYAN}tsp/init/data_load{Style.RESET_ALL}] loading {Style.BRIGHT}./data.tsp{Style.RESET_ALL} ... ", end="")
    tsp_dict = pickle.load(open("./data.tsp", "rb"))
    print(f"[{Fore.GREEN}LOADED!{Style.RESET_ALL}]")
else:
    print(f"[{Fore.RED}NOT_FOUND!{Style.RESET_ALL}]")
    print(f"[{Fore.CYAN}tsp/init/data_create{Style.RESET_ALL}] initializing default values  ... ", end="")
    tsp_dict = {}
    tsp_dict["components"] = []
    tsp_dict["finances"] = money(0)
    print(f"[{Fore.GREEN}DONE!{Style.RESET_ALL}]")
    print(f"[{Fore.CYAN}tsp/init/data_save{Style.RESET_ALL}] saving {Style.BRIGHT}./data.tsp{Style.RESET_ALL} ... ", end="")
    pickle.dump(tsp_dict, open("./data.tsp", "wb"))
    print(f"[{Fore.GREEN}SAVED!{Style.RESET_ALL}]")
print(f"[{Fore.CYAN}/tsp/init/db_crpt_chk{Style.RESET_ALL}] checking for database corruption ... ", end="", flush=True)
# prgress_bar(18, "OK!", 0.1, 0.3) #! activate!
toc = time.time()
tictoc = round(toc - tic, 3)
print(f"[{Fore.CYAN}tsp/init{Style.RESET_ALL}] initialization completed in {Style.BRIGHT}{tictoc}s{Style.RESET_ALL}, welcome to {Style.BRIGHT}{app_info.name} v{app_info.version} {Style.RESET_ALL}by {Style.BRIGHT}{app_info.by}{Style.RESET_ALL}")
print(f"[{Fore.CYAN}tsp/init/main_menu{Style.RESET_ALL}] press [{Fore.MAGENTA}ENTER{Style.RESET_ALL}] to enter {Fore.BLUE}main menu{Style.RESET_ALL}: ", end="")
# input() #! remember to activate this when finished!

tsp_ascii = """            ___________           .__      _________                   
            \__    ___/___   ____ |  |__  /   _____/____ ___  __ ____  
              |    |_/ __ \_/ ___\|  |  \ \_____  \\__  \\  \/ // __ \ 
              |    |\  ___/\  \___|   Y  \/        \/ __ \\   /\  ___/ 
              |____| \___  >\___  >___|  /_______  (____  /\_/  \___  >
                 ________\/.__  \/     \/        \/    .\/          \/ 
                 \______   \  |__   ____   ____   ____ |__|__  ___     
                  |     ___/  |  \ /  _ \_/ __ \ /    \|  \  \/  /     
                  |    |   |   Y  (  <_> )  ___/|   |  \  |>    <      
                  |____|   |___|  /\____/ \___  >___|  /__/__/\_ \     
                                \/            \/     \/         \/     """

def menumaker(cmd_entered, previous_menu, destination_menu, width, selection_1 = "NA", selection_2 = "NA", selection_3 = "NA", selection_4 = "NA", selection_5 = "NA", selection_6 = "NA", command = "menu"):
    header_line = f"] {Style.BRIGHT}{app_info.name} {Style.RESET_ALL}v{Style.BRIGHT}{app_info.version} {Style.RESET_ALL}by{Style.BRIGHT} {app_info.by} {Style.RESET_ALL}["
    header_line = header_line.center(width + 24, "-")
    current_money = tsp_dict["finances"].get_balance()
    footer_line = f"] {Style.BRIGHT}balance{Style.RESET_ALL}: {Fore.GREEN}{current_money}e{Style.RESET_ALL} ["
    footer_line = footer_line.center(width + 17, "-")
    cmd = None
    if previous_menu == "main_menu" and cmd_entered == 0: # if exit TSP is pressed
        print(f"quit! quit! quit!")
        return()
    elif previous_menu in command_menu_list and not cmd_entered == 0 or previous_menu == "main_menu" and cmd_entered == 1: # if command is used
        print(f"cmd: {cmd_entered} | dest_menu: {destination_menu} / prev_menu: {previous_menu} | s1 {selection_1} s2 {selection_2} s3 {selection_3} s4 {selection_4} s5 {selection_5} s6 {selection_6}")
        exec_cmd_line = f"[{Fore.CYAN}tsp/{previous_menu}/{components_menu[cmd_entered - 1]}/exec{Style.RESET_ALL}] you executed {Fore.BLUE}{components_menu[cmd_entered - 1]}{Style.RESET_ALL}, press [{Fore.MAGENTA}ENTER{Style.RESET_ALL}] to return to {Fore.BLUE}{previous_menu}{Style.RESET_ALL}:"
        if previous_menu == "components_menu":
            print(f"your command: {components_menu[cmd_entered - 1]}")
            if cmd_entered - 1 == 0: # list_components
                os.system("cls")
                print(header_line)
                print(f"{Style.RESET_ALL}{Fore.CYAN}", end="")
                print(tsp_ascii) #TODO: compact us!!
                print(f"{Style.RESET_ALL}")
                for item in tsp_dict["components"]:
                    idx_int = int(tsp_dict["components"].index(item))
                    print(f"    [ {Style.BRIGHT}{idx_int}{Style.RESET_ALL} ] {Fore.YELLOW}{item.type}{Style.RESET_ALL} - {Fore.YELLOW}{item.name}{Style.RESET_ALL} / {Fore.GREEN}{item.price}e{Style.RESET_ALL} ({Fore.RED}{item.priority}{Style.RESET_ALL}) - {item.url}")
                print("\n" + footer_line + "\n")
                input(exec_cmd_line)
                menumaker(2, "main_menu", "components_menu", 80, menu_list[2][0], menu_list[2][1], menu_list[2][2], menu_list[2][3], menu_list[2][4], menu_list[2][5])
            elif cmd_entered -1 == 1: # add_components
                priority_int = int(input(f"[{Fore.CYAN}tsp/{previous_menu}/{components_menu[cmd_entered - 1]}/cmd{Style.RESET_ALL}] enter {Fore.RED}priority{Style.RESET_ALL} of component [{Fore.MAGENTA}0-100{Style.RESET_ALL}]: "))
                type_str = str(input(f"[{Fore.CYAN}tsp/{previous_menu}/{components_menu[cmd_entered - 1]}/cmd{Style.RESET_ALL}] enter type of component ({Fore.YELLOW}CPU, GPU, etc.{Style.RESET_ALL}) [{Fore.MAGENTA}TEXT{Style.RESET_ALL}]: "))
                name_str = str(input(f"[{Fore.CYAN}tsp/{previous_menu}/{components_menu[cmd_entered - 1]}/cmd{Style.RESET_ALL}] enter name of component ({Fore.YELLOW}Ryzen 1600AF, etc.{Style.RESET_ALL}) [{Fore.MAGENTA}TEXT{Style.RESET_ALL}]: "))
                price_int = int(input(f"[{Fore.CYAN}tsp/{previous_menu}/{components_menu[cmd_entered - 1]}/cmd{Style.RESET_ALL}] enter price of component [{Fore.MAGENTA}NUMBER{Style.RESET_ALL}]: "))
                url_str = str(input(f"[{Fore.CYAN}tsp/{previous_menu}/{components_menu[cmd_entered - 1]}/cmd{Style.RESET_ALL}] enter url of component [{Fore.MAGENTA}TEXT{Style.RESET_ALL}]: "))
                input(f"blaablaablaa is this correct? and continue to save?") #TODO: add saving here!
                print(f"[{Fore.CYAN}tsp/{previous_menu}/{components_menu[cmd_entered - 1]}/save{Style.RESET_ALL}] saving {Fore.YELLOW}{type_str} {name_str}{Style.RESET_ALL} to database ... ", end="")
                tsp_dict["components"].append(component(priority_int, type_str, url_str, name_str, price_int))
                print(f"[{Fore.GREEN}OK!{Style.RESET_ALL}]")
                input(exec_cmd_line)
                menumaker(2, "main_menu", "components_menu", 80, menu_list[2][0], menu_list[2][1], menu_list[2][2], menu_list[2][3], menu_list[2][4], menu_list[2][5])
            elif cmd_entered -1 == 2: # delete_components
                os.system("cls")
                print(header_line)
                print(f"{Style.RESET_ALL}{Fore.CYAN}", end="")
                print(tsp_ascii)
                print(f"{Style.RESET_ALL}")
                idx_count = 0
                for item in tsp_dict["components"]:
                    idx_count += 1
                    idx_int = int(tsp_dict["components"].index(item))
                    print(f"    [ {Style.BRIGHT}{idx_int}{Style.RESET_ALL} ] {Fore.YELLOW}{item.type}{Style.RESET_ALL} - {Fore.YELLOW}{item.name}{Style.RESET_ALL} / {Fore.GREEN}{item.price}e{Style.RESET_ALL} ({Fore.RED}{item.priority}{Style.RESET_ALL}) - {item.url}")
                print("\n" + footer_line + "\n")
                del_int = int(input(f"[{Fore.CYAN}tsp/{previous_menu}/{components_menu[cmd_entered - 1]}/cmd{Style.RESET_ALL}] enter {Style.BRIGHT}INDEX{Style.RESET_ALL} of component to delete [{Fore.MAGENTA}0-{idx_count - 1}{Style.RESET_ALL}]: "))
                del_print_type = tsp_dict["components"][del_int].type
                del_print_name = tsp_dict["components"][del_int].name
                print(f"[{Fore.CYAN}tsp/{previous_menu}/{components_menu[cmd_entered - 1]}/del{Style.RESET_ALL}] deleting {Fore.YELLOW}{del_print_type}{Style.RESET_ALL} - {Fore.YELLOW}{del_print_name}{Style.RESET_ALL} ... ", end="")
                del tsp_dict["components"][del_int]
                print(f"[{Fore.GREEN}OK!{Style.RESET_ALL}]")
                print(f"save changes to db?")
                print(f"[{Fore.CYAN}tsp/{previous_menu}/{components_menu[cmd_entered - 1]}/save{Style.RESET_ALL}] saving changes to database ... ", end="") #TODO: add saving here!
                print(f"[{Fore.GREEN}OK!{Style.RESET_ALL}]")
                input(exec_cmd_line)
                menumaker(2, "main_menu", "components_menu", 80, menu_list[2][0], menu_list[2][1], menu_list[2][2], menu_list[2][3], menu_list[2][4], menu_list[2][5])
        elif previous_menu == "finances_menu":
            print(f"your command: {finances_menu[cmd_entered - 1]}")
            if cmd_entered - 1 == 0: # deposit_money
                input(exec_cmd_line)
            elif cmd_entered -1 == 1: # withdraw_money
                input(exec_cmd_line)
            elif cmd_entered -1 == 2: # view_balance_logs
                input(exec_cmd_line)
        elif previous_menu == "system_operations_menu":
            print(f"your command: {system_operations_menu[cmd_entered - 1]}")
            if cmd_entered - 1 == 0: # load_database
                input(exec_cmd_line)
            elif cmd_entered -1 == 1: # save_database
                input(exec_cmd_line)
            elif cmd_entered -1 == 2: # reset_database
                input(exec_cmd_line)
        elif previous_menu == "main_menu" and cmd_entered == 1: # display status
            print(f"your command: {main_menu[cmd_entered - 1]}")
            input(exec_cmd_line)
        return()
    elif destination_menu in menu_names_list or destination_menu in menu_names_list and cmd_entered == 99: # if traversing between menus
        os.system("cls")
        print(header_line)
        print(f"{Style.RESET_ALL}{Fore.CYAN}", end="") # color of ascii-art text
        print(tsp_ascii)
        print(f"{Style.RESET_ALL}")
        selection_list = [selection_1, selection_2, selection_3, selection_4, selection_5, selection_6]
        command_list = []
        if destination_menu == "main_menu":
            selection_list.insert(0, "exit_techsave_phoenix")
        elif destination_menu in menu_names_list:
            selection_list.insert(0, "exit_to_main_menu")
        # for selection_idx in range(1, len(selection_list) + 1): # old
        for selection_idx in range(0, len(selection_list)):
            # selection_print = selection_list[selection_idx - 1] # old
            selection_print = selection_list[selection_idx]
            # if selection_list[selection_idx - 1] == "NA":
            if selection_list[selection_idx] == "NA":
                pass
            else:
                selection_print = selection_print.ljust(61, ".")
                print(f"    {Style.RESET_ALL}[{Fore.MAGENTA}{selection_idx}{Style.RESET_ALL}] {Style.BRIGHT}-->{Style.RESET_ALL} [ {Fore.BLUE}{selection_print}{Style.RESET_ALL} ]")
                command_list.append("null")
        print("\n" + footer_line + "\n")
        print(f"[{Fore.CYAN}tsp/{destination_menu}/cmd{Style.RESET_ALL}] you are in {Fore.BLUE}{destination_menu}{Style.RESET_ALL}, enter your command [{Fore.MAGENTA}0-{len(command_list) - 1}{Style.RESET_ALL}]: ", end="")
        cmd = int(input())
    elif command == "command":
        pass
    menumaker(cmd, destination_menu, menu_names_list[cmd], 80, menu_list[cmd][0], menu_list[cmd][1], menu_list[cmd][2], menu_list[cmd][3], menu_list[cmd][4], menu_list[cmd][5])

display_status = ["COMMAND_NAME", "NA", "NA", "NA", "NA", "NA"]
main_menu = ["display_status!", "components_menu", "finances_menu", "system_menu", "NA", "NA"]
components_menu = ["list_components", "add_components", "delete_components", "NA", "NA", "NA"]
finances_menu = ["deposit_money", "withdraw_money", "view_balance_logs", "NA", "NA", "NA"]
system_menu = ["load_database", "save_database", "reset_database", "NA", "NA", "NA"]
menu_names_list = ["main_menu", "display_status!", "components_menu", "finances_menu", "system_menu"]
command_menu_list = ["components_menu", "finances_menu", "system_menu"]
menu_list = [main_menu, display_status, components_menu, finances_menu, system_menu]

menumaker(99, "main_menu", "main_menu", 80, menu_list[0][0], menu_list[0][1], menu_list[0][2], menu_list[0][3], menu_list[0][4], menu_list[0][5])