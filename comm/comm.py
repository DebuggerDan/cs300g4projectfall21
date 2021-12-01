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


provider report function - prints report - manager only
    same as above, but this time for providers


summary report function - prints report - manager only
    lists all members who have received services in past week
    lists all providers who have rendered services in past week
    lists (if desired) details on rendered services
    display total price of services rendered

    
weekly summary function - prints report - manager and provider access
    same as above, but only iterates once a week.
    note: if in middle of week, do not update
"""



from database.database import Database as db

#Helper function to get the user input and sends it to the memberReport function. 
#Did it seperately just incase this input functionality will be implemented in the menu or leave it here.
def testMember():
    print("\nThis report will display the information of a specific member and a list of the services they utilized for the entire week.\n")
    IDnum = input("To search for a member, please enter the member's 9-digit ID: ")
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
        serviceID = memberInfo[9]

        #provider can only take in provider number, not service ID number. must fix database.
        #Maybe in the database with list of services will also keep track of each provider who provided the service.
        #providerInfo = db.get_provider(serviceID)

        #Get service info from the service database using the service ID.
        #Will change once we incorporate multiple services per member.
        serviceInfo = db.get_service(serviceID)

        #Display the entire report using member info from specific column(element).
        print("\nMember Name: ", memberInfo[1],
        "\nMember ID Number: ", memberInfo[0],
        "\nMember Street Address: ", memberInfo[2],
        "\nMember City: ", memberInfo[3],
        "\nMember State: ", memberInfo[4],
        "\nMember Zip Code: ", memberInfo[5],
        "\n\nList of weekly services utilized by this member: \n\t Service ID:", memberInfo[9])
    

        #Put a loop here that will loop through the list of services and print out individually
        print("\tDate of Service: 00/00/0000",
        "\n\tProvider Name: null", 
        #providerInfo[2],
        "\n\tService Name: ", serviceInfo[1])

        #Will need a database that will have a list of services used by specific members
        #with: date of service, name of provider who gave service, and service name.




