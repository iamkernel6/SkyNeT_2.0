import time
import random
import pyfiglet
import os
from tqdm import tqdm, trange

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def loading():
    print(style.GREEN + "Please Wait")
    for i in trange(10):
        time.sleep(0.1)
    banner = pyfiglet.figlet_format("Welcome to SkyNet!")
    print(banner)
    print("SkyNet v2.0 by @iamkernel._")

operator_list = ["1.Tri        - https://tri.co.id", "2.Telkomsel  - https://telkomsel.com", "3.XL         - https://xl.co.id", "4.Indosat    - https://indosatoredoo.com"]
foo = ['-1.244500, 116.851944', '-1.244197, 116.839819', '-6.327564, 106.850075', '-6.325261, 106.847994', '-6.342455, 107.143166', '-6.340600, 107.154935', '-3.244197, 264.839819', '-6.325261, 365.847994']

def lacak():
    print(operator_list[0])
    print(operator_list[1])
    print(operator_list[2])
    print(operator_list[3])
    for pilih in operator_list:
        operator = input("Pilih Operator : ")
        if operator == "1":
            lacak_tri()
        elif operator == "2":
            lacak_telkomsel()
        elif operator == "3":
            lacak_xl()
        elif operator == "4":
            lacak_indosat
        else:
            print("Menu tidak tersedia")

def lacak_tri():
    print("Please Wait Connecting to https://database.tri.co.id")
    for i in trange(100):
        time.sleep(0.1)
    print("Done!")

    print("Connecting to https://maps.google.com/")
    for i in trange(50):
        time.sleep(0.2)
    print("Done!")

    print("Mendapatkan koordinat Target")
    for i in trange(100):
        time.sleep(0.2)
    print("Done!")
    time.sleep(1)

    print(random.choice(foo))
    print("Copy dan Pastekan koordinat di atas ke dalam aplikasi Google Maps")

def lacak_telkomsel():
    print("Please Wait Connecting to https://database.telkomsel.com")
    for i in trange(100):
        time.sleep(0.1)
    print("Done!")

    print("Connecting to https://maps.google.com/")
    for i in trange(50):
        time.sleep(0.2)
    print("Done!")

    print("Mendapatkan koordinat Target")
    for i in trange(100):
        time.sleep(0.2)
    print("Done!")
    time.sleep(1)

    print(random.choice(foo))
    print("Copy dan Pastekan koordinat di atas ke dalam aplikasi Google Maps")

def lacak_xl():
    print("Please Wait Connecting to https://database.xl.co.id")
    for i in trange(100):
        time.sleep(0.1)
    print("Done!")

    print("Connecting to https://maps.google.com/")
    for i in trange(50):
        time.sleep(0.2)
    print("Done!")

    print("Mendapatkan koordinat Target")
    for i in trange(100):
        time.sleep(0.2)
    print("Done!")
    time.sleep(1)

    print(random.choice(foo))
    print("Copy dan Pastekan koordinat di atas ke dalam aplikasi Google Maps")

def lacak_indosat():
    print("Please Wait Connecting to https://database.indosatoredoo.com")
    for i in trange(100):
        time.sleep(0.1)
    print("Done!")

    print("Connecting to https://maps.google.com/")
    for i in trange(50):
        time.sleep(0.2)
    print("Done!")

    print("Mendapatkan koordinat Target")
    for i in trange(100):
        time.sleep(0.2)
    print("Done!")
    time.sleep(1)

    print(random.choice(foo))
    print("Copy dan Pastekan koordinat di atas ke dalam aplikasi Google Maps")

def datanomor():
    print(style.RED + "Upgrade Ke Premium untuk melihat Data lengkap pengguna")
    time.sleep(2)