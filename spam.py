import pyautogui as pt
import time
import colorama
from colorama import Fore

colorama.init()

print(Fore.GREEN + """

██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗ ██████╗     ███████╗██████╗  █████╗ ███╗   ███╗
██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
██║ █╗ ██║███████║███████║   ██║   ███████╗███████║██████╔╝██████╔╝    ███████╗██████╔╝███████║██╔████╔██║
██║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██╔══██║██╔═══╝ ██╔═══╝     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║██║  ██║██║     ██║         ███████║██║     ██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝         ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                                          

""")

print("")
limit = input("Limit:") # set the limit
message = input("Message:") # set the message
i = 0
time.sleep(5) # Giusepp lu capybara

while i < int(limit):
    pt.typewrite(message)
    pt.press("enter")

    i+=1