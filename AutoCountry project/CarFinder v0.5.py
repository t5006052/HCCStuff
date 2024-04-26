#READ THIS FIRST
#it is crucial tht AVLv0.5.txt is in the SAME FOLDER as this file or else it will throw a cannot find file error
#thank you!
import os
avl = []
rep = True

def retriveAVL():
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    avlDoc = open("AVLv0.5.txt", mode = "r")
    i = 0
    l = len(avlDoc.readlines())
    avlDoc.seek(0)
    while i < l:
        avl.append(avlDoc.readline().strip())
        i += 1
        avlDoc.__next__
    avlDoc.close()
    

def starup():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")
    print("Please enter the following number below from the following menu")
    print("")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicles")
    print("3. ADD Authorized Vechile")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

def select(int):
    match response:
        case 1:
            printAVL()
            return True
        case 2:
            searchAVL()
            return True
        case 3:
            updateAVL()
            return True
        case 4: 
            removeAVL()
            return True
        case 5:
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            closeAVL()
            return False
        case _:
            print("Please enter one of the options above")
            return True

def printAVL():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    i = 0
    while(i < len(avl)):
        print(avl[i])
        i+=1
    print("")
    print("")
    
def searchAVL():
    print("Please Enter the full Vehicle name")
    vecSearch = str(input())
    i = 0
    while(i < len(avl)):
        if(avl[i] == vecSearch):
            print(str(avl[i]) + " is an authorized vehicle")
            return
        i+=1
    print(vecSearch + " is not an authorized vehicle, if you recived this error please check spelling and try again.")
    
def updateAVL():
    print("Please enter the full vechile name you would like to add:")
    addition = str(input())
    avl.append(addition)
    print("You have added '" + addition + "' as an authorized vechicle")
    

def removeAVL():
    print("Please enter the full Vehicle name you would like to REMOVE:")
    subtraction = str(input())
    try:
        print("Are you sure you want to remove '" + subtraction + "' from the Authorized Vehicle list?")
        yn = str(input())
        if(yn == "yes"):avl.remove(subtraction)
    except:
        print("That Vehicle is not on the Authorized Vehicle List")
        
def closeAVL():
    avlDoc = open("AVLv5.txt", mode = "w")
    i = 0
    update = ""
    while i < len(avl):
        update += avl[i] + "\n"
        i += 1
    avlDoc.write(update)
    avlDoc.close()

retriveAVL()
while(rep):
    starup()
    response = int(input())
    rep = select(response)
  





