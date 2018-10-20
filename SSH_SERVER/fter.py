import ProfileClass
import json


def switchFun(argument, switcher):
    func = switcher.get(argument, lambda: "Invalid number")
    func()


def MainMenu():
    #Connect to server(userID)
    global userID
    userID = "Pedrito"
    global profile
    profile = ProfileClass.Profile()
    print "Welcome to Termeet \nPlease select what are you seeking:\n"
    print "1. Couple"
    print "2. HackBuddy"
    print "3. Job"
    menuOption = input()
    switcher = {1: CoupleMenu,
                2: HackBuddyMenu,
                3: JobMenu
                }
    switchFun(menuOption, switcher)


def CoupleMenu():
    global SubMenuTitle
    global SubMenuSelected
    SubMenuSelected = 1
    SubMenuTitle = "Termeet/Couple"
    print SubMenuTitle
    printMenuTools(SubMenuSelected)


def HackBuddyMenu():
    global SubMenuTitle
    global SubMenuSelected
    SubMenuSelected = 2
    SubMenuTitle = "Termeet/HackBuddy"
    print SubMenuTitle
    printMenuTools(SubMenuSelected)


def JobMenu():
    global SubMenuTitle
    global SubMenuSelected
    SubMenuSelected = 3
    SubMenuTitle = "Termeet/Job"
    print SubMenuTitle
    printMenuTools(SubMenuSelected)


def printMenuTools(SubMenu):
    print "1. Profile"
    print "2. Inbox"
    print "3. Match list"
    print "4. Termeeting"
    print "5. Exit"
    menuOption = input()
    switcher = {
        1: ProfileMenu,
        2: InboxMenu,
        3: MatchListMenu,
        4: TermeetingMenu,
        5: Exit
    }
    switchFun(menuOption, switcher)





def ProfileMenu():
    #profile = CAPAMEDIA.damePerfil(userID)
    print "1. View Profile"
    print "2. Add Interest"
    print "3. New Description"
    print "4. Edit Age"
    print "5. Edit gender"
    print "6. Add searching"
    print "7. Edit Work"
    print "8. Edit Study"
    menuOption = input()
    switcher = {
        1: ViewProfile,
        2: AddInterests,
        #3: NewDescription,
        #4: EditAge,
        #5: EditGender,
        #6: AddSearching,
        #7: EditWork,
        #8: EditStudy
    }
    switchFun(menuOption, switcher)

def ViewProfile():
    print "Image"
    print "Nick: "+ profile.nick
    print "Full Name: "+ profile.fullName
    print "Age: " + profile.age
    #...

def AddInterests():
    #intereses[] = CAPAMEDIA.dameTodosTagsDeIntereses()
    print "Choose all the tags you identify with: "
    intereses = ["#Fuertes", "#Tontos", "#C++", "#PatinajeArtistico"]

    for interes in intereses:
        print


def InboxMenu():
    print SubMenuTitle + "/Inbox"


def MatchListMenu():
    print SubMenuTitle + "/Match list"


def TermeetingMenu():
    print SubMenuTitle + "/Termeeting"


def Exit():
    MainMenu()


MainMenu()
