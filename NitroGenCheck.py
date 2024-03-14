import requests
import random
import string
import threading
import time
from pystyle import Write, Colors

Write.Print("    made by duesti.", Colors.white, interval=0.05)
print("")

try:
    howMany = int(input("    How many codes generate and check: "))
except ValueError:
    Write.Print("    Ты ввел не число!", Colors.light_red)

with open("nitroOutput.txt", "w", encoding='utf-8') as file:
    print(f"    {howMany} NitroCodes will be generated!")
    start = time.time()
    for i in range(howMany):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))
        file.write(f"https://discord.gift/{code}\n")
    print(f"    Generated {howMany} codes | Time taken -> {time.time() - start}\n")
with open("nitroOutput.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")
        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
        r = requests.get(url)

        if r.status_code == 200:
            print(f"    Valid! | {nitro}")
            break
        else:
            print(f"    Invalid | {nitro}")
print("")
input("    Если вам не повезло, генерируйте 20млн кодов ^_^")
