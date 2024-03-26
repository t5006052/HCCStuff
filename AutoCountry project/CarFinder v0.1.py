alv = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]
rep = True

def starup():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please enter the following number below from the following menu")
    print("")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

def select(int):
    match response:
        case 1:
            printALV()
            return True
        case 2:
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

while(rep):
    starup()
    response = int(input())
    rep = select(response)





