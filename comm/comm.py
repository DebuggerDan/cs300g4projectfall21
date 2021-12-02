#CS300 Report Dispaying 
#Weekly Member Services Reports

"""
comm comments - all functions assume user is "logged in" already
make sure the "logged in" person meets requirements

memberReport(memberID): 
    member report function - prints report - manager only
    take member id
    displays information for that member
    displays services from this week for member
    if desired, display older services


providerReport(providerID):
    provider report function - prints report - manager only
    same as above, but this time for providers

managerReport(managerID):
summary report function - prints report - manager only
    lists all members who have received services in past week
    lists all providers who have rendered services in past week
    lists (if desired) details on rendered services
    display total price of services rendered

NOT SURE ABOUT THIS YET:
weekly summary function - prints report - manager and provider access
    same as above, but only iterates once a week.
    note: if in middle of week, do not update
"""



from database.database import Database as db

#Helper function to get the user input and sends it to the memberReport function. 
#Did it seperately just incase this input functionality will be implemented in the menu or leave it here.
def testMember():
    print("\nThis report will display the information of a specific Member and a list of the services they utilized for the entire week.\n")
    IDnum = input("To search for a Member, please enter the Member's 9-digit ID: ")
    memberReport(IDnum)

#Function to pull the data of a specific member with their ID number.
def memberReport(memberID):
    #Pull the member info from the chocan.sqlite database utilizing functions from database.py
    memberInfo = db.get_member(memberID)

    #Check if the member exists, give error if not. 
    #(Should we allow them to keep trying?)
    if(memberInfo == None):
        print("\nMember does not exist.")
    else:
        #The service ID of a member is stored in column 9. 
        #Will change for when it is a list of members and will access that different database.
        #serviceID = memberInfo[9]
        billing = db.get_member_billing(memberInfo[0])
        total = 0.00

        #provider can only take in provider number, not service ID number. must fix database.
        #Maybe in the database with list of services will also keep track of each provider who provided the service.
        #providerInfo = db.get_provider(serviceID)

        #Get service info from the service database using the service ID.
        #Will change once we incorporate multiple services per member.
        #serviceInfo = db.get_service(serviceID)

        #Display the entire report using member info from specific column(element).
        print("\nMember Name: ", memberInfo[1],
        "\nMember ID Number: ", memberInfo[0],
        "\nMember Street Address: ", memberInfo[2],
        "\nMember City: ", memberInfo[3],
        "\nMember State: ", memberInfo[4],
        "\nMember Zip Code: ", memberInfo[5],
        #"\n\nList of weekly services utilized by this member: \n\tService ID:", memberInfo[9])
        "\n\nList of weekly services utilized by this member: \n")
    
        for bill in billing:
            #Put a loop here that will loop through the list of services and print out individually
            #print("\tDate of Service: 00/00/0000",
            #"\n\tProvider Name: null",
            #providerInfo[2],
            #"\n\tService Name: ", serviceInfo[1])
            print("\tMember ID: " + str(bill[1]))
            print("\tProvider ID: " + str(bill[2]))
            print("\tService Date: " + bill[3])
            print("\tBilling Date: " + bill[4])
            print("\tService ID: " + str(bill[5]))

            serviceInfo = db.get_service(bill[5])
            fee = serviceInfo[2]
            print("\tService Fee: $" + "{:.2f}".format(fee))
            total += fee
            print()

        #Will need a database that will have a list of services used by specific members
        #with: date of service, name of provider who gave service, and service name.
        print("Total Fees: $" + "{:.2f}".format(total))





#The Provider weekly report with their info and weekly services given to each Member.

def testProvider():
    print("\nThis report will display the information of a specific Provider and a list of the services they provided for Members for the entire week.\n")
    IDnum = input("To search for a Provider, please enter the Provider's 9-digit ID: ")
    providerReport(IDnum)

def providerReport(providerID):
    providerInfo = db.get_provider(providerID)

    if(providerInfo == None):
        print("\nProvider does not exist.")
    else:
        #The service ID of a member is stored in column 9. 
        #Will change for when it is a list of members and will access that different database.
        serviceID = providerInfo[9]

        #provider can only take in provider number, not service ID number. must fix database.
        #Maybe in the database with list of services will also keep track of each provider who provided the service.
        #providerInfo = db.get_provider(serviceID)

        #Get service info from the service database using the service ID.
        #Will change once we incorporate multiple services per member.
        serviceInfo = db.get_service(serviceID)

        #Display the entire report using provider info from specific column(element).
        print("\nProvider Name: ", providerInfo[1],
        "\nProvider ID Number: ", providerInfo[0],
        "\nProvider Street Address: ", providerInfo[2],
        "\nProvider City: ", providerInfo[3],
        "\nProvider State: ", providerInfo[4],
        "\nProvider Zip Code: ", providerInfo[5],
        "\n\nList of services provided by this Provider: \n")
    
        #Need to also add to the database of list of services member name + ID per service.
        #How will we go about doing the time and data accessed from computer? ..leave it out?
        print("\tDate of Service: 00/00/0000",
        "\n\tDate & Time Data Recieved: 00/00/0000 HH:MM:SS",
        "\n\tMember Name: null",
        "\n\tMember ID: null",
        "\n\tService Name: ", serviceInfo[1],
        "\n\tService ID:", serviceID,
        "\n\tFee to be paid: $", serviceInfo[2])
        #using the service ID currently in provider database but will change

        #Trying to add total of all current services.
        #Won't work because the dollar sign in database makes it a string.
        #Don't know how to, will wait for actual database of weekly services.
        '''
        allFee = db.get_services()
        x = 0
        currFee = 0
        while x < len(allFee):
            print("Test1: ", allFee[x][2])
            currFee = allFee[x][2]
            x = x+1
        
        print("TEST: ", currFee)
        '''    

        #Print out the total consults that the Provider gave for the week.
        #Print out the total fees from added up services given by Provider.
        print("\nTotal number of consultations: 000")
        print("\nTotal service fees for the week: $99,999.99")

        #Should we just do the total calculation in the database?
        #Or use a loop to add the total in this funcion?



def testManager():
    print("\nThis report will display a summary of specific information for Managers.")
    print("The manager will utilize this report for accounts payable for Providers.")
    print("The report will also display a total number of providers who provided services, total consultations, and overall fee total from services.\n\n")

    #We can use this to only allow Managers access this report.
    IDnum = input("To access this weeks Summary Report, please enter your 9-digit Manager ID: ")
    #Put a conditional statement here to check is it is a manager ID or not. Give error and exit if not.
    managerReport(IDnum)

def managerReport(managerID):
    providerInfo = db.get_providers()
    x = 0
    print("\nList of all Providers to get paid this week:\n")
    while x < len(providerInfo):
        #Currently is printing ALL of providers names from provider database. Should we randomly generate everytime to simulate a "week"?
        print("\n\t",providerInfo[x][1])
        print("\n\tTotal consults this Provider had: 0")
        print("\n\tTotal fees: $99,999.99")
        x += 1
    
    #Total number of providers, should we just add all providers in the database?
    #Total number of consultations we can add all the services provided from member services database.
    #Overall fees will be ALL services across all members added up
    print("\n\nTotal number of Providers who provided services this week: 000",
          "\nTotal Number of Consultations: 000",
          "\nOverall fees: $99,999.99")


    
