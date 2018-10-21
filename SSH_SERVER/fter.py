import ProfileClass
import json
import imgToAsciiArt2


def switchFun(argument, switcher):
    func = switcher.get(argument, lambda: "Invalid number")
    func()


def MainMenu():
    global userID
    #userID = Connect to server(userID)
    userID = "Pedrito"
    global profile
    profile = ProfileClass.Profile()
    image_file_path = "IriaSlack.jpg"
    global imageAscii
    imageAscii = imgToAsciiArt2.handle_image_conversion(image_file_path)
    print "Welcome to TerMeet "
    f = open('termita.txt', 'r')
    mensaje = f.read()
    print(mensaje)
    f.close()
    print
    print "What are you seeking for?:"
    print "1. Couple"
    print "2. HackBuddy"
    print "3. Job"
    menuOption = input()
    print
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
    print "Choose an option:"
    print "1. Profile"
    print "2. Inbox Matchings"
    print "3. Termeeting"
    print "4. Exit"
    menuOption = input()
    print
    switcher = {
        1: ProfileMenu,
        2: InboxMenu,
        3: TermeetingMenu,
        4: MainMenu #Exit
    }
    switchFun(menuOption, switcher)





def ProfileMenu():
    #profile = CAPAMEDIA.getProfile(userID,subMenuSelected)
    print "What do you wanna do?:"
    print "1. View my Profile"
    print "2. Add Interest"
    print "3. Edit Description"
    print "4. Edit Age"
    print "5. Edit gender"
    print "6. Edit searching"
    print "7. Edit Work"
    print "8. Edit Study"
    print "9. Edit Mail"
    print "10. Exit"
    menuOption = input()
    print
    switcher = {
        1: ViewProfile,
        2: AddInterest,
        3: EditDescription,
        4: EditAge,
        5: EditGender,
        6: EditSearching,
        7: EditWork,
        8: EditStudy,
        9: EditCorreo,
        10: ExitProfileMenu
    }
    switchFun(menuOption, switcher)

def ExitProfileMenu():
    printMenuTools(SubMenuSelected)

def EditCorreo():
    print "Give me your mail babe. Press Intro when you finish"
    profile.correo = str(raw_input())
    #CAPAMEDIA.editMail(profile.correo,userID)
    print
    ProfileMenu()

def EditWork():
    print "Tell us about how you manage the work ;). Press Intro when you finish"
    profile.work = str(raw_input())
    #CAPAMEDIA.editWork(profile.work,userID)
    print
    ProfileMenu()

def EditStudy():
    print "Tell us about your studies stuff. Press Intro when you finish"
    profile.description =str(raw_input())
    #CAPAMEDIA.editStudy(profile.study,userID)
    ProfileMenu()

def EditSearching():
    print "1. Other, 2. Male, 3. Male & Other, 4. Female, 5.Female & Other, 6. Male & Female, 7. Everything is fine to me"
    profile.searching = int(raw_input())
    print
    ProfileMenu()

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
    print
    ProfileMenu()


def EditDescription():
    print "Try to be funny at the same time smart. Press Intro when you finish"
    profile.description = raw_input()
    #CAPAMEDIA.editDescription(profile.description,userID)
    print
    ProfileMenu()


def EditAge():
    print "Age is only a number."

    age = int(input())
    if age>18 and age <100:
        # CAPAMEDIA.editAge(age,userID)
        profile.age = age

    else:
        if age<18:
            print "Try again, lie this time"

        else:
            print "WTF? Why you still alive?"
    print
    ProfileMenu()


def ViewProfil(profile):
    print imageAscii
    print "Nick: " + profile.nick
    print "Full Name: " + profile.fullName
    print "Mail: " + profile.correo
    print "Interests: " + profile.interests
    print "Description: " + profile.description
    print "Age: " + str(profile.age)
    print "Gender: " + profile.gender
    searching = ["None", "Others", "Boys", "Boys & Others", "Girls", "Girls & Others", "Girls & Boys",
                 "I love people not their genitals"]
    if profile.searching == 7:
        print "Searching: I love people not their genitals"
    else:
        print "Searching: " + searching[profile.searching]
    print "Work: " + profile.work
    print "Study: " + profile.study
    print


def ViewProfile():
    ViewProfil(profile)
    ProfileMenu()

def AddInterest():
    #intereses[] = CAPAMEDIA.getAllInterestsTable()
    print "Choose all the tags you identify with : "
    intereses = ["#Fuertes", "#Tontos", "#C++", "#PatinajeArtistico"]
    i =0
    print "To go back to menu press 0."
    for interes in intereses:
        i = i + 1
        print (str(i) + ". " + interes),
    print

    entrada = int(input())
    if entrada < len(intereses):
        nuevosIntereses = profile.interests.split("/")
        nuevosIntereses2 = []
        nuevosIntereses.append("/")

        while entrada != 0:
            nuevosIntereses.append(intereses[int(entrada)-1])
            profile.interests = profile.interests  + intereses[int(entrada)-1] + "/"
            nuevosIntereses2.append(int(entrada))
            nuevosIntereses.append("/")
            for ni in nuevosIntereses:
                print ni,
            print
            entrada = input()

        #CAPAMEDIA.addTags(userID, nuevosIntereses2)
    else: print "There's no number " + entrada
    print
    ProfileMenu()


def InboxMenu():
    #print SubMenuTitle + "/Inbox"
    # matches[] = CAPAMEDIA.getMatches(userID)
    match = ProfileClass.Profile()
    match2 = ProfileClass.Profile()
    match3 = ProfileClass.Profile()
    match.nick = "ABBy"
    match2.nick = "JeNNy"
    match3.nick = "ANNa"
    matches = [match, match2, match3]
    print "Matches:"
    for m in matches:
        print m.nick + ", " + m.fullName + ", " + m.correo

    # superlikes[] = CAPAMEDIA.getSuperlikes(userID)
    print
    print "If you want to see more about a match, press 1.\nIf you want to come back to menu, press 2."
    aux=input()
    if aux == 1:
        print "Write your posible love name: "
        nickLove = str(raw_input())
        b = False;
        for m in matches:
            if m.nick == nickLove:

                ViewProfil(m)
                b = True
        if not b:
            print "There's no person called " + nickLove
    print
    ExitProfileMenu()


def TermeetingMenu():
    #print SubMenuTitle + "/Termeeting"
    # candidatos[] = CAPAMEDIA.getCandidatos(userID)
    match = ProfileClass.Profile()
    match2 = ProfileClass.Profile()
    match3 = ProfileClass.Profile()
    match.nick = "ABBy"
    match2.nick = "JeNNy"
    match3.nick = "ANNa"
    candidatos = [match, match2, match3]
    for c in candidatos:
        print "Do you like what you see?"
        print imageAscii
        print "Nick: " + c.nick
        print "Name: " + c.fullName
        print
        print "Use S To accept, A to Refuse, W To SuperMeet, Z to see more about "
        arrow = raw_input()
        while arrow == 'Z' or arrow == 'z':
            ViewProfil(c)
            print "Use S To accept, A to Refuse, W To SuperMeet"
            arrow = raw_input()

        if arrow =='S' or arrow == 's':
            #accept = CAPAMEDIA.likeFromTo(userID, c.userID)
            accept = True
            if accept ==True:
                print "MATCH!"
                print
    print "Oh! There are not more people for you!"



MainMenu()
