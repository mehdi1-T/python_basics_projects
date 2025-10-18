from colorama import Fore, Style, init
init(autoreset=True)

# HEADER
print(Fore.CYAN + "==============================================")
print(Fore.CYAN + "  WELCOME TO YOUR COLORFUL POMODORO TIMER  ")
print(Fore.CYAN + "==============================================\n")

# USER INPUT
print(Fore.WHITE + "How many minutes do you want to work? ⏱ 25")

# WORK SESSION
print(Fore.GREEN + "\nWork session started! Stay focused ")
print(Fore.GREEN + "----------------------------------------------")
print(Fore.YELLOW + "[##########....................]  30%")
print(Fore.YELLOW + "[##############################]  100%")
print(Fore.GREEN + "----------------------------------------------")
print(Fore.RED + " Time’s up! Great job! Take a short break ")
print(Style.RESET_ALL)

# BREAK SESSION
print(Fore.YELLOW + "\nBreak started... relax a bit ")
print(Fore.YELLOW + "----------------------------------------------")
print(Fore.YELLOW + "[##########....................]  40%")
print(Fore.YELLOW + "[##############################]  100%")
print(Fore.YELLOW + "----------------------------------------------")

# ENDING
print(Fore.MAGENTA + " Break is over! Ready for another session? (y/n)")
print(Fore.RED + " Goodbye! You did amazing today!")
print(Style.RESET_ALL)

