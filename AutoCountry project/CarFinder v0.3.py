alv = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]
rep = True

def starup():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please enter the following number below from the following menu")
    print("")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicles")
    print("3. ADD Authorized Vechile")
    print("4. Exit")

def select(int):
    match response:
        case 1:
            printALV()
            return True
        case 2:
            searchALV()
            return True
        case 3:
            updateALV()
            return True
        case 4:
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            return False
        case _:
            print("Please enter one of the options above")
            return True

def printALV():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    i = 0
    while(i < len(alv)):
        print(alv[i])
        i+=1
    print("")
    print("")
    
def searchALV():
    print("Please Enter the full Vehicle name")
    vecSearch = str(input())
    i = 0
    while(i < len(alv)):
        if(alv[i] == vecSearch):
            print(str(alv[i]) + " is an authorized vehicle")
            return
        i+=1
    print(vecSearch + " is not an authorized vehicle, if you recived this error please check spelling and try again.")
    
def updateALV():
    print("PLease enter the full vechile name you would like to add:")
    addition = str(input())
    alv.append(addition)
    print("You have added '" + addition + "' as an authorized vechicle")

while(rep):
    starup()
    response = int(input())
    rep = select(response)





