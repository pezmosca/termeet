import ProfileClass
import json


def switchFun(argument, switcher):
    func = switcher.get(argument, lambda: "Invalid number")
    func()


def MainMenu():
    global userID
    #userID = Connect to server(userID)
    userID = "Pedrito"
    global profile
    profile = ProfileClass.Profile()
    f = open('termita.txt', 'r')
    mensaje = f.read()
    print(mensaje)
    f.close()
    print "Welcome to TerMeet \nWhat are you seeking for?:\n"
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
    print "Choose an option:\n"
    print "1. Profile"
    print "2. Inbox Matchings"
    print "3. Termeeting"
    print "4. Exit"
    menuOption = input()
    switcher = {
        1: ProfileMenu,
        2: InboxMenu,
        3: TermeetingMenu,
        4: Exit
    }
    switchFun(menuOption, switcher)





def ProfileMenu():
    #profile = CAPAMEDIA.getProfile(userID,subMenuSelected)
    print "What do you wanna do?:\n"
    print "1. View Profile"
    print "2. Add Interest"
    print "3. Edit Description"
    print "4. Edit Age"
    print "5. Edit gender"
    print "6. Edit searching"
    print "7. Edit Work"
    print "8. Edit Study"
    menuOption = input()
    switcher = {
        1: ViewProfile,
        2: AddInterest,
        3: EditDescription,
        4: EditAge,
        5: EditGender,
        6: EditSearching,
        7: EditWork,
        8: EditStudy
    }
    switchFun(menuOption, switcher)

def EditWork():
    print "Try to be funny at the same time smart. Press Intro when you finish"
    profile.work = str(input())
    #CAPAMEDIA.editWork(profile.work,userID)

def EditStudy():
    print "Try to be funny at the same time smart. Press Intro when you finish"
    profile.description =str( input())
    #CAPAMEDIA.editStudy(profile.study,userID)

def EditSearching():
    print "1. Other, 2. Male, 3. Male & Other, 4. Female, 5.Female & Other, 6. Male & Female, 7. Everything is fine for me"
    profile.searching = int(input());

def EditGender():
    print "1. Female, 2. Male or 3.Other?"
    genderNum = input()
    gender = ""
    if genderNum == 1: gender = "Female"
    elif genderNum == 2: gender = "Male"
    elif genderNum == 3: gender = "Other"
    else:
        print "That's not an option"
        gender = "None"

    if gender != "None":
        profile.gender = gender
        #CAPAMEDIA.editGender(gender,userID)
        b=0


def EditDescription():
    print "Try to be funny at the same time smart. Press Intro when you finish"
    profile.description = input()
    #CAPAMEDIA.editDescription(profile.description,userID)

    print profile.description


def EditAge():
    print "Age is only a number."
    profile.age = int(input())
    age = profile.age
    if age>18 and age <100:
        # CAPAMEDIA.editAge(age,userID)
        print str(age)
    else:
        if age>18:
            print "Try again, lie this time"
        else: print "WTF? Why you still alive?"


def ViewProfile():
    print "Image"
    print "Nick: "+ profile.nick
    print "Full Name: "+ profile.fullName
    print "Age: " + str(profile.age)
    print "Gender: "+ profile.gender
    searching = ["None", "Others", "Boys", "Boys & Others", "Girls", "Girls & Others", "Girls & Boys", "I love people not their genitals"]
    if profile.searching == 7:
        print "Searching: I love people not their genitals"
    else: print "Searching: "+ searching[profile.searching]
    print "Work: " + profile.work
    print "Study: " + profile.study

def AddInterest():
    #intereses[] = CAPAMEDIA.getAllInterestsTable()
    print "Choose all the tags you identify with : "
    intereses = ["None", "#Fuertes", "#Tontos", "#C++", "#PatinajeArtistico"]
    i =0
    print "0. Exit"
    for interes in intereses:
        i = i + 1
        print (str(i) + ". " + interes),
    print

    entrada = input()
    nuevosIntereses = []
    nuevosIntereses2 = []
    nuevosIntereses.append("/")

    while entrada != 0:
        nuevosIntereses.append(intereses[int(entrada)])
        nuevosIntereses2.append(int(entrada))
        nuevosIntereses.append("/")
        for ni in nuevosIntereses:
            print ni,
        print
        entrada = input()

    #CAPAMEDIA.addTags(userID, nuevosIntereses2)


def InboxMenu():
    print SubMenuTitle + "/Inbox"


def TermeetingMenu():
    print SubMenuTitle + "/Termeeting"


def Exit():
    MainMenu()


MainMenu()
