from colorama import Fore, init, Style
import time
from playsound import playsound

init(autoreset=True)

print(Fore.YELLOW + "=================================")
print(Fore.YELLOW + "======== Pomodoro Timer  ========")
print(Fore.YELLOW + "=================================\n")

user = int(input(Fore.GREEN + "⏳ How many minutes do you want to work?: "))

seconds = user * 60

for i in range(seconds, 0, -1):
    bar_length = 20
    progress = int((seconds - i) / seconds * bar_length)
    bar = "#" * progress + "-" * (bar_length - progress)
    print(Fore.YELLOW + f"[{bar}] {i//60:02d}:{i%60:02d} remaining", end="\r")
    time.sleep(1)

print("\n" + Fore.RED + "🍅 Time’s up! Great job! Take a short break ☕")
playsound(r"C:\Users\bismiallah\Desktop\python\basics\sounds\police-siren-sound-effect-240674.mp3")