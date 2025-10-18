from playsound import playsound

sounds = {
    1: r"C:\Users\bismiallah\Desktop\python\basics\funny-alarm-317531.mp3",
    2: r"C:\Users\bismiallah\Desktop\python\basics\notification-sound-type-18-no-copyright-410280.mp3",
    3: r"C:\Users\bismiallah\Desktop\python\basics\police-siren-sound-effect-240674.mp3"
}
sounds_name = {
   1: "tili lili",
   2: "water",
   3: "plice" 
}
while True:

    # intro
    print("================================================")
    print("==== PLEASESE SELECT ONE OF THESE OPPTIONS =====")
    print("1. sound number 1")
    print("2. sound number 2")
    print("3. sound number 3")
    print("4. quit")
    print("================================================")
    print("")

    try:
        user = int(input("enter your choice : "))

        if user == 4:
            break
        elif user in sounds:
            print(f"🔊 Playing sound number {sounds_name[user]}...")
            playsound(sounds[user])

        else:
            print("invalide input try again")
    except Vqlur
            