import ccmenu

class regUsers:
    def __init__(self, usernameInput, passwordInput):
        self.username = usernameInput
        self.password = passwordInput

#create and initialise constants, with values for username and passwd
USERNAME = "Adocherty"
PASSWORD = "PNAccess"

user1 = regUsers(USERNAME, PASSWORD)

#attempts used
loginAttempts = 0 
loggedIn = False

print("")
print("Welcome to the Packaged Networks Script Program!")
print("")

#creating a loop. the user is allowed to try logging in 3 times
while loginAttempts < 3:
    usernameInput = input("Enter your username - ")
    passwordInput = input("Enter your password - ")

    #if the user enters the correct username and password, they are granted access
    if usernameInput == user1.username and passwordInput == user1.password:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("You have logged in as " + USERNAME + ".")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        loggedIn = True
        break
    
    #if the user enters the username or password incorrectly, the amount of login attempts is increased
    else:
        print("")
        print("The username or password was incorrect. Please try again")
        print("")
        loginAttempts += 1
        loggedIn = False
    
    #the program exits if the user fails the login 3 times
    if loginAttempts == 3:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Too many login attempts. Please contact your system administrator.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        loggedIn = False
        break

if loggedIn == True:
    ccmenu.menu()