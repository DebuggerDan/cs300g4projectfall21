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
from security.sec import loginChecker, serviceChecker

#Member Report helper function to take in a Member ID.
def testMember():
    good = 0    #flag for proper ID number.
    print("\nThis report will display the information of a specific Member and a list of the services they utilized for the entire week.\n")
    #while loop to allow proper input of a Member's ID.
    while good != 3:   
        IDnum = input("To search for a Member, please enter the Member's 9-digit ID: ")
        good = loginChecker(IDnum)  #update flag with loginChecker function.
        if(good != 3):
            print("Error: ID Invalid.\n\n")
        else:
            memberReport(IDnum)

#Function to pull the data of a specific member with their ID number.
def memberReport(memberID):
    #Pull the member info from the chocan.sqlite database utilizing functions from database.py
    memberInfo = db.get_member(memberID)

    #Check if the member exists, give error if not and exit. 
    if(memberInfo == None):
        print("\nMember does not exist.\n\n")
    else:
        billing = db.get_member_billing(memberInfo[0])  #Get Member's weekly serives.
        total = 0.00

        #Display the entire report using member info from specific column(element).
        print("\nMember Name: ", memberInfo[1],
        "\nMember ID Number: ", memberInfo[0],
        "\nMember Street Address: ", memberInfo[2],
        "\nMember City: ", memberInfo[3],
        "\nMember State: ", memberInfo[4],
        "\nMember Zip Code: ", memberInfo[5],
        "\n\nList of weekly services utilized by this member: \n")
    
        #loop through all the services this specific member utilized for the week in billing table.
        for bill in billing:

            serviceInfo = db.get_service(bill[5]);  #Needed for displaying service name.
            providerInfo = db.get_provider(bill[2]);    #Needed for displaying Provider name.

            print("\n\tDate of Service: ", bill[3],
            "\n\tProvider Name: ", providerInfo[1], 
            "\n\tService Name: ", serviceInfo[1])


            #Pearstopher stuffz:
            """
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
            
            print("Total Fees: $" + "{:.2f}".format(total))
            """





#Helper function for provider report. Same process as Member report helper function.
def testProvider():
    good = 0
    print("\nThis report will display the information of a specific Provider and a list of the services they provided for Members for the entire week.\n")
    while good != 3:   
        IDnum = input("To search for a Provider, please enter the Provider's 9-digit ID: ")
        good = loginChecker(IDnum)
        if(good != 3):
            print("Error: ID Invalid.\n\n")
        else:
            providerReport(IDnum)


#The Provider weekly report with their info and weekly services given to each Member.
def providerReport(providerID):
    providerInfo = db.get_provider(providerID)

    if(providerInfo == None):
        print("\nProvider does not exist.")
    else:
        billing = db.get_provider_billing(providerInfo[0])
        total_fee = 0.00    #Total fee of services provided.
        total_con = 0       #Total consultations provided by the Provider.

        #Display the entire report using provider info from specific column(element).
        print("\nProvider Name: ", providerInfo[1],
        "\nProvider ID Number: ", providerInfo[0],
        "\nProvider Street Address: ", providerInfo[2],
        "\nProvider City: ", providerInfo[3],
        "\nProvider State: ", providerInfo[4],
        "\nProvider Zip Code: ", providerInfo[5],
        "\n\nList of services provided by this Provider: \n")
    
        for bill in billing:
            serviceInfo = db.get_service(bill[5]);  #Used for displaying service name and fee.
            memberInfo = db.get_member(bill[1]);    #Used for displaying member name.
            
            print("\n\tDate of Service: ", bill[3],
            "\n\tDate & Time Data Recieved: ", bill[4],
            "\n\tMember Name:", memberInfo[1],
            "\n\tMember ID: ", bill[1],
            "\n\tService Name: ", serviceInfo[1],
            "\n\tService ID:", bill[5],
            "\n\tFee to be paid: $", serviceInfo[2])

            fee = serviceInfo[2]
            total_fee += fee;
            total_con += 1  #keep track of consultations provided.

        print("\nTotal number of consultations: ", total_con)
        print("\nTotal service fees for the week: $", total_fee)
        print()





def testManager():
    good = 0
    print("\nThis report will display a summary of specific information for Managers.")
    print("The manager will utilize this report for accounts payable for Providers.")
    print("The report will also display a total number of providers who provided services, total consultations, and overall fee total from services.\n\n")
    
    while good != 3:   
        IDnum = input("To access this weeks Summary Report, please enter your 9-digit Manager ID: ")
        good = loginChecker(IDnum)
        if(good != 3):
            print("Error: ID Invalid.\n\n")
        else:
            managerReport(IDnum)

#STILL NEEDS WORK
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



#Takes a member ID and sees if they are valid or suspended. Uses some verification because of user input.
def querMemInfo():
    memID = input("Please enter the desired member ID: ")
    valID = loginChecker(memID)
    if valID != 3:
        print("Invalid ID entry! Returning to menu.")
        return -1
    member = db.get_member(memID)
    if str(member) == "None":
        print("Member does not exist! Returning to menu.")
        return -1
    #print(member[6])
    if int(member[6]) == 1:
        print("Member is active!")
        print("Member name: ", member[1])
        print("ZIP: ", member[5])
        return 1
    else:
        print("Member is not active!")
        print("Further details withheld due to inactivity.")
        return 2

#Same as above, but for providers. Doesn't check for activity, just prints.
def querProvInfo():
    provID = input("Please enter the desired provider ID: ")
    valID = loginChecker(provID)
    if valID != 3:
        print("Invalid ID entry! Returning to menu.")
        return -1
    provid = db.get_provider(provID)
    if str(provid) == "None":
        print("Provider does not exist! Returning to menu.")
        return -1
    print("Provider name: ", provid[1])
    print("Provider ZIP: ", provid[5])
    return 1

#Same as above again except for a service.
def querServInfo():
    servID = input("Please enter the desired service ID: ")
    valID = serviceChecker(servID)
    if valID != 3:
        print("Invalid ID entry! Returning to menu.")
        return -1
    servid = db.get_service(servID)
    if str(servid) == "None":
        print("Service does not exist! Returning to menu.")
        return -1
    print("Service name: ", servid[1])
    print("Service cost: ", servid[2])
    return 1