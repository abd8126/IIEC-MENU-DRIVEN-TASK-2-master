import os
import getpass

os.system("tput setaf 3")
print("\t\t\t----------")


passwd = getpass.getpass("Enter ur password : ")

if passwd != "Anubhav@8126":
    print("Password Incorrect...")
    exit()

r = input("Where you want to run this menu ? (local/remote) : ")
print(r)

while True:
    os.system("clear")
    print("""
    \n
    Press 1 : to install Docker
    Press 2 : to Launch CentOS
    Press 3 : to Pull Docker Images
    Press 4 : to user create
    Press 5 : to exit
    """)

    ch = input("Enter ur Choice : ")
    print (ch)

    if r == "local":
        if int(ch) == 1:
            os.system("dnf install docker-ce --nobest")

        elif int(ch) == 2:
                image = input("Enter the Name OS which you want to Launch :")
                os.system("docker run -it --name webos -p 9091:80 {}".format(image))

        elif int(ch) == 3:
            os.system("docker pull centos")

        elif int(ch) == 4:
            os.system("useradd")

        elif int(ch) == 5:
            exit()
        else:
            print("not supported")

    elif r == "remote":
        ip = input("Enter Your ip : ")
        print(ip)
        if int(ch) == 1:
            os.system("ssh {} date".format(ip))

        elif int(ch) == 2:
            os.system("ssh {} cal".format(ip))

        elif int(ch) == 3:
            os.system("ssh {} reboot".format(ip))

        elif int(ch) == 4:
            os.system("ssh {} useradd".format(ip))

        elif int(ch) == 5:
            exit()
        else:
            print("not supported")
    else:
        print("not supported login...")

    input("\n plz. enter to continue...")
