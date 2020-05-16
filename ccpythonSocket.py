import socket
import os

#host_ip will ping an URL to check for a response.
def ping_URL():
    loop = True

    while loop:
        try:
            host = input("Please enter URL of host - ")
            ip = socket.gethostbyname(host)
            print("The IP address of " + host + " is " + ip)
            response = os.system("ping " + ip)

            #Program tells user the URL is up if the response is normal
            if response == 0:
                print("")
                print("")
                print("The server is up.")

            #Program tells user the URL is down if the response is not normal
            else:
                print("")
                print("")
                print("The server is down.")
            break

        #Program tells user if the URL cannot be resolved
        except socket.gaierror:
            print("")
            print("")
            print("Cannot resolve the host " + host)
            print("Please try again.")
            print("")

#host_ip will ping an IP address to check for a response.
def ping_IP():

    ip = input("Please enter the IP address - ")
    response = os.system("ping " + ip)

    #Program tells user the IP is up if the response is normal
    if response == 0:
        print("")
        print("")
        print("The server is up.")

    #Program tells user the IP is down if the response is not normal
    else:
        print("")
        print("")
        print("The server is down.")