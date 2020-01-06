#adding color to your print statements
#pip install colorama

from colorama import Fore  #foreground color
from colorama import init

init()

print(Fore.GREEN + "PASS")
print(Fore.RED + "FAIL")
print(Fore.YELLOW + "AMBER")
print(Fore.BLUE + "TESTING")
