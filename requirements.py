import os, time


print("1 -->> Debian (Kali Linux)")
print("2 -->> Arch")
print("")
x = input("-->> ")

if x == "1":
    print("Downloading...")
    os.system("sudo apt install git bash xterm -y")
    time.sleep(1)
    print("Done!!")
    time.sleep(2)
    exit()

if x == "2":
    print("Downloading...")
    os.system("sudo pacman -S git bash xterm --noconfirm")
    time.sleep(1)
    print("Done!!")
    time.sleep(2)
    exit()
