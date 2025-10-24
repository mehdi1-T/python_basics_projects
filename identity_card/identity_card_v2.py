from colorama import init, Fore, Style

init(autoreset=True)

print("Let's create your Identity Card!\n")

name = input("Enter your name: ")
dob = input("Enter your date of birth: ")
gender = input("Enter your gender: ")
nationality = input("Enter your nationality: ")
address = input("Enter your address: ")
job = input("Enter your job: ")

print("\n" + "=" * 58)
print("||{:^54}||".format("Identity Card"))
print("=" * 58)
print(f"|| {Fore.YELLOW}Name          :{Style.RESET_ALL} {name:<35}||")
print(f"|| {Fore.YELLOW}Date of Birth :{Style.RESET_ALL} {dob:<35}||")
print(f"|| {Fore.YELLOW}Gender        :{Style.RESET_ALL} {gender:<35}||")
print(f"|| {Fore.YELLOW}Nationality   :{Style.RESET_ALL} {nationality:<35}||")
print(f"|| {Fore.YELLOW}Address       :{Style.RESET_ALL} {address:<35}||")
print(f"|| {Fore.YELLOW}Job           :{Style.RESET_ALL} {job:<35}||")
print(f"||{'':<40}{name:<7}||")
print("=" * 58)
