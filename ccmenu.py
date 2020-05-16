#allows the program to access OS (Windows) functions
import os
import ccpythonSocket
#import ccnmap

#shuts down the users PC in 5 seconds
def shutdown():
    os.system("shutdown /s /f /t 5")

#restarts the users PC in 5 seconds
def restart():
    os.system("shutdown /r /f /t 5")

def menu():
    print("Please select one of the following options - ")
    print("1. Ping a URL or IP Address")
    print("2. Port Scan an IP Address")
    print("3. Shutdown PC")
    print("4. Restart PC")
    print("5. Exit Program")

    #Checks answer from user. Will respond according to the menu options.
    #If the answer is not 1-5, the user will be prompted to re-enter their choice.
    loop = True

    while loop:

        usersChoice = input("==> ")

        if usersChoice == "1":
            print("")
            print("Would you like to ping an IP or URL?")
            print("1. IP Address")
            print("2. URL")
            print("3. Back to menu")
            print("")
            IPorURL = input("==> ")
            if IPorURL == "1":
                ccpythonSocket.ping_IP()
            elif IPorURL == "2":
                ccpythonSocket.ping_URL()
            elif IPorURL == "3":
                menu()
            else:
                print("Invalid input.")
                continue
            loop = False
            break

        elif usersChoice == "2":
            ccnmap.portScan()
            loop = False
            break

        elif usersChoice == "3":
            print("Your PC will shutdown in 5 seconds.")
            shutdown()
            loop = False
            break
        
        elif usersChoice == "4":
            print("Your PC will restart in 5 seconds.")
            restart()
            loop = False
            break
        
        elif usersChoice == "5":
            print("The program will now exit. Goodbye!")
            loop = False
            break
        
        else:
            print("Invalid input.")
            continue