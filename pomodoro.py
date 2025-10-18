from colorama import Fore, init, Style
import time
from playsound import playsound

init(autoreset=True)

# 🕒 Pomodoro Timer (Focus App)
print(Fore.YELLOW + "=================================")
print(Fore.YELLOW + "======== Pomodoro Timer  ========")
print(Fore.YELLOW + "=================================\n")

# Ask user for work time (in minutes)
user = int(input(Fore.GREEN + "⏳ How many minutes do you want to work?: "))

# Convert minutes to seconds
seconds = user * 60

# Countdown
for i in range(seconds, 0, -1):
    bar_length = 20
    progress = int((seconds - i) / seconds * bar_length)
    bar = "#" * progress + "-" * (bar_length - progress)
    print(Fore.YELLOW + f"[{bar}] {i//60:02d}:{i%60:02d} remaining", end="\r")
    time.sleep(1)

print("\n" + Fore.RED + "🍅 Time’s up! Great job! Take a short break ☕")
playsound(r"C:\Users\bismiallah\Desktop\python\basics\sounds\police-siren-sound-effect-240674.mp3")