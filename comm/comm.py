#CS300 Report Dispaying 
#Weekly Member Services Reports

import os #for making directories and files
from interface.forms import Forms #date function is in here

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

def newMemberReport():
    # Each member who has consulted a ChocAn provider during that week
    # receives a list of services provided to that member, sorted in order of service date.
    # The report, which is also sent as an e-mail attachment, includes:
    #   • Member name (25 characters).
    #   • Member number (9 digits).
    #   • Member street address (25 characters).
    #   • Member city (14 characters).
    #   • Member state (2 letters).
    #   • Member zip code (5 digits).
    #   • For each service provided, the following details are required:
    #       o Date of service (MM-DD-YYYY).
    #       o Provider name (25 characters).
    #       o Service name (20 characters).
    # make sure the main report folder exists
    path = 'reports'
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path)
    # create new subdirectories for the current report
    report_path = path + "/member_report_" + Forms.date().replace(":", "_")  # no ":" in windows filenames
    os.makedirs(report_path)

    memberInfo = db.get_members()
    x = 0
    print("\nList of all Members who were provided services this week:\n")
    total_fee = 0.00
    total_con = 0
    total_mem = 0
    while x < len(memberInfo):
        # Currently is printing ALL of providers names from provider database. Should we randomly generate everytime to simulate a "week"?
        # solution: I will go through all the providers but skip them if they don't appear in the billing database
        # print("\t" + providerInfo[x][1])

        member_file = report_path + "/" + str(memberInfo[x][0]) + ".txt"

        billing = db.get_member_billing(memberInfo[x][0])
        if billing is None:
            x += 1
            continue
        member_total_fee = 0.00  # Total fee of services provided.
        member_total_con = 0  # Total consultations provided to the Member
        total_mem += 1

        info = "\nMember Name: " + memberInfo[x][1] + \
               "\nMember ID Number: " + str(memberInfo[x][0]) + \
               "\nMember Street Address: " + memberInfo[x][2] + \
               "\nMember City: " + memberInfo[x][3] + \
               "\nMember State: " + memberInfo[x][4] + \
               "\nMember Zip Code: " + str(memberInfo[x][5]) + \
               "\n\nList of services provided to this Member: \n"

        print(info)  # print the info, same as before
        with open(member_file, "a") as f:
            f.write(info)

        for bill in billing:
            serviceInfo = db.get_service(bill[5])  # Used for displaying service name and fee.
            providerInfo = db.get_provider(bill[2])  # Used for displaying provider name.

            # skip if it is a bad entry (bad serviceid, bad providerid)
            if serviceInfo is None or providerInfo is None:
                continue

            info = "\n\tDate of Service: " + bill[3] + \
                   "\n\tDate & Time Data Received: " + bill[4] + \
                   "\n\tProvider Name: " + providerInfo[1] + \
                   "\n\tProvider ID: " + str(bill[2]) + \
                   "\n\tService Name: " + serviceInfo[1] + \
                   "\n\tService ID:" + str(bill[5]) + \
                   "\n\tFee to be paid: $" + "{:.2f}".format(serviceInfo[2])


            print(info)
            with open(member_file, "a") as f:
                f.write(info)

            fee = serviceInfo[2]
            member_total_fee += fee
            member_total_con += 1  # keep track of consultations provided.

        # case: provider had bills but all bills were invalid
        if member_total_con == 0:
            x += 1
            continue

        info = "\nTotal consults this Member had: " + str(member_total_con) + \
               "\nTotal fees: $" + "{:.2f}".format(member_total_fee)
        print(info)
        with open(member_file, "a") as f:
            f.write(info)

        total_fee += member_total_fee
        total_con += member_total_con
        x += 1

    # Total number of providers, should we just add all providers in the database?
    # Total number of consultations we can add all the services provided from member services database.
    # Overall fees will be ALL services across all members added up
    print("\nTotal number of Providers who provided services this week: ", total_mem,
          "\nTotal Number of Consultations: ", total_con,
          "\nOverall fees: $", "{:.2f}".format(total_fee))


def newProviderReport():
    # Each provider who has billed ChocAn during that week receives a report,
    # sent as an e-mail attachment, containing the list of services he or she provided to
    # ChocAn members. To simplify the task of verification, the report contains the same
    # information as that entered on the provider’s form, in the order that the data were
    # received by the computer. At the end of the report is a summary including the
    # number of consultations with members and the total fee for that week. That is, the
    # fields of the report include:
    #   • Provider name (25 characters).
    #   • Provider number (9 digits).
    #   • Provider street address (25 characters).
    #   • Provider city (14 characters).
    #   • Provider state (2 letters).
    #   • Provider zip code (5 digits).
    #   • For each service provided, the following details are required:
    #       o Date of service (MM-DD-YYYY).
    #       o Date and time data were received by the computer (MM-DD-YYYY
    #           HH:MM:SS).
    #       o Member name (25 characters).
    #       o Member number (9 digits).
    #       o Service code (6 digits).
    #       o Fee to be paid (up to $999.99).
    #   • Total number of consultations with members (3 digits).
    #   • Total fee for the week (up to $99,999.99).

    # make sure the main report folder exists
    path = 'reports'
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path)
    # create new subdirectories for the current report
    report_path = path + "/provider_report_" + Forms.date().replace(":", "_")  # no ":" in windows filenames
    os.makedirs(report_path)

    providerInfo = db.get_providers()
    x = 0
    print("\nList of all Providers to get paid this week:\n")
    total_fee = 0.00
    total_con = 0
    total_prov = 0
    while x < len(providerInfo):
        # Currently is printing ALL of providers names from provider database. Should we randomly generate everytime to simulate a "week"?
        # solution: I will go through all the providers but skip them if they don't appear in the billing database
        # print("\t" + providerInfo[x][1])

        provider_file = report_path + "/" + str(providerInfo[x][0]) + ".txt"

        billing = db.get_provider_billing(providerInfo[x][0])
        if billing is None:
            x += 1
            continue
        provider_total_fee = 0.00  # Total fee of services provided.
        provider_total_con = 0  # Total consultations provided by the Provider.
        total_prov += 1

        info = "\nProvider Name: " + providerInfo[x][1] + \
               "\nProvider ID Number: " + str(providerInfo[x][0]) + \
               "\nProvider Street Address: " + providerInfo[x][2] + \
               "\nProvider City: " + providerInfo[x][3] + \
               "\nProvider State: " + providerInfo[x][4] + \
               "\nProvider Zip Code: " + str(providerInfo[x][5]) + \
               "\n\nList of services provided by this Provider: \n"

        print(info)  # print the info, same as before
        with open(provider_file, "a") as f:
            f.write(info)

        for bill in billing:
            serviceInfo = db.get_service(bill[5])  # Used for displaying service name and fee.
            memberInfo = db.get_member(bill[1])  # Used for displaying member name.

            # skip if it is a bad entry (bad serviceid, bad memberid)
            if serviceInfo is None or memberInfo is None:
                continue

            info = "\n\tDate of Service: " + bill[3] + \
                   "\n\tDate & Time Data Recieved: " + bill[4] + \
                   "\n\tMember Name:" + memberInfo[1] + \
                   "\n\tMember ID: " + str(bill[1]) + \
                   "\n\tService Name: " + serviceInfo[1] + \
                   "\n\tService ID:" + str(bill[5]) + \
                   "\n\tFee to be paid: $" + "{:.2f}".format(serviceInfo[2])

            print(info)
            with open(provider_file, "a") as f:
                f.write(info)

            fee = serviceInfo[2]
            provider_total_fee += fee
            provider_total_con += 1  # keep track of consultations provided.

        # case: provider had bills but all bills were invalid
        if provider_total_con == 0:
            x += 1
            continue

        info = "\nTotal consults this Provider had: " + str(provider_total_con) + \
               "\nTotal fees: $" + "{:.2f}".format(provider_total_fee)
        print(info)
        with open(provider_file, "a") as f:
            f.write(info)

        total_fee += provider_total_fee
        total_con += provider_total_con
        x += 1

    # Total number of providers, should we just add all providers in the database?
    # Total number of consultations we can add all the services provided from member services database.
    # Overall fees will be ALL services across all members added up
    print("\nTotal number of Providers who provided services this week: ", total_prov,
          "\nTotal Number of Consultations: ", total_con,
          "\nOverall fees: $", "{:.2f}".format(total_fee))

def newEFTReport():
    # A record consisting of electronic funds transfer (EFT) data is then written to
    # disk; banking computers will later ensure that each provider’s bank account is
    # credited with the appropriate amount.

    path = 'reports'
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path)
    # create new subdirectories for the current report
    report_path = path + "/EFT_report_" + Forms.date().replace(":", "_")  # no ":" in windows filenames
    os.makedirs(report_path)
    EFT_file = report_path + "/EFT_report.txt"

    providerInfo = db.get_providers()
    x = 0
    total_fee = 0.00
    total_con = 0
    total_prov = 0
    while x < len(providerInfo):
        # Currently is printing ALL of providers names from provider database. Should we randomly generate everytime to simulate a "week"?
        # solution: I will go through all the providers but skip them if they don't appear in the billing database
        # print("\t" + providerInfo[x][1])

        billing = db.get_provider_billing(providerInfo[x][0])
        if billing is None:
            x += 1
            continue
        provider_total_fee = 0.00  # Total fee of services provided.
        provider_total_con = 0  # Total consultations provided by the Provider.
        total_prov += 1

        info = "\nProvider Name: " + providerInfo[x][1] + \
               "\nProvider ID Number: " + str(providerInfo[x][0])

        print(info)  # print the info, same as before
        with open(EFT_file, "a") as f:
            f.write(info)

        for bill in billing:
            serviceInfo = db.get_service(bill[5])  # Used for displaying service name and fee.
            memberInfo = db.get_member(bill[1])  # Used for displaying member name.

            # skip if it is a bad entry (bad serviceid, bad memberid)
            if serviceInfo is None or memberInfo is None:
                continue

            fee = serviceInfo[2]
            provider_total_fee += fee
            provider_total_con += 1  # keep track of consultations provided.

        # case: provider had bills but all bills were invalid
        if provider_total_con == 0:
            info = "\n\tProvider had bills, but they were invalid." + \
                   "\n\tTotal fees: $ 0.00\n"
            print(info)
            with open(EFT_file, "a") as f:
                f.write(info)
            x += 1
            continue

        info = "\n\tTotal consults this Provider had: " + str(provider_total_con) + \
               "\n\tTotal fees: $" + "{:.2f}".format(provider_total_fee) + "\n"
        print(info)
        with open(EFT_file, "a") as f:
            f.write(info)

        total_fee += provider_total_fee
        total_con += provider_total_con
        x += 1

    # Total number of providers, should we just add all providers in the database?
    # Total number of consultations we can add all the services provided from member services database.
    # Overall fees will be ALL services across all members added up
    print("\nTotal number of Providers who provided services this week: ", total_prov,
          "\nTotal Number of Consultations: ", total_con,
          "\nOverall fees: $", "{:.2f}".format(total_fee))



def newSummaryReport():
    path = 'reports'
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path)
    # create new subdirectories for the current report
    report_path = path + "/summary_report_" + Forms.date().replace(":", "_")  # no ":" in windows filenames
    os.makedirs(report_path)
    summary_file = report_path + "/summary_report.txt"

    providerInfo = db.get_providers()
    x = 0
    print("\nList of all Providers to get paid this week:\n")
    total_fee = 0.00
    total_con = 0
    total_prov = 0
    while x < len(providerInfo):
        # Currently is printing ALL of providers names from provider database. Should we randomly generate everytime to simulate a "week"?
        # solution: I will go through all the providers but skip them if they don't appear in the billing database
        # print("\t" + providerInfo[x][1])

        billing = db.get_provider_billing(providerInfo[x][0])
        if billing is None:
            x += 1
            continue
        provider_total_fee = 0.00  # Total fee of services provided.
        provider_total_con = 0  # Total consultations provided by the Provider.
        total_prov += 1

        info = "\nProvider Name: " + providerInfo[x][1] + \
               "\nProvider ID Number: " + str(providerInfo[x][0]) + \
               "\nProvider Street Address: " + providerInfo[x][2] + \
               "\nProvider City: " + providerInfo[x][3] + \
               "\nProvider State: " + providerInfo[x][4] + \
               "\nProvider Zip Code: " + str(providerInfo[x][5]) + \
               "\n\nList of services provided by this Provider: \n"

        print(info)  # print the info, same as before
        with open(summary_file, "a") as f:
            f.write(info)

        for bill in billing:
            serviceInfo = db.get_service(bill[5])  # Used for displaying service name and fee.
            memberInfo = db.get_member(bill[1])  # Used for displaying member name.

            # skip if it is a bad entry (bad serviceid, bad memberid)
            if serviceInfo is None or memberInfo is None:
                continue

            info = "\n\tDate of Service: " + bill[3] + \
                   "\n\tDate & Time Data Recieved: " + bill[4] + \
                   "\n\tMember Name:" + memberInfo[1] + \
                   "\n\tMember ID: " + str(bill[1]) + \
                   "\n\tService Name: " + serviceInfo[1] + \
                   "\n\tService ID:" + str(bill[5]) + \
                   "\n\tFee to be paid: $" + "{:.2f}".format(serviceInfo[2])

            print(info)
            with open(summary_file, "a") as f:
                f.write(info)

            fee = serviceInfo[2]
            provider_total_fee += fee
            provider_total_con += 1  # keep track of consultations provided.

        # case: provider had bills but all bills were invalid
        if provider_total_con == 0:
            x += 1
            continue

        info = "\n\nTotal consults this Provider had: " + str(provider_total_con) + \
               "\nTotal fees: $" + "{:.2f}".format(provider_total_fee) + "\n\n"
        print(info)
        with open(summary_file, "a") as f:
            f.write(info)

        total_fee += provider_total_fee
        total_con += provider_total_con
        x += 1

    # Total number of providers, should we just add all providers in the database?
    # Total number of consultations we can add all the services provided from member services database.
    # Overall fees will be ALL services across all members added up
    info = "\nTotal number of Providers who provided services this week: " + str(total_prov) +\
           "\nTotal Number of Consultations: " + str(total_con) +\
           "\nOverall fees: $" + "{:.2f}".format(total_fee)

    print(info)
    with open(summary_file, "a") as f:
        f.write(info)

def newMAPReport():
    print("\nRunning Main Accounting Procedure...")
    newMemberReport()
    newProviderReport()
    newEFTReport()
    newSummaryReport()


def providerDirectory():
    # At any time, a provider can request the software product for a Provider Directory, an alphabetically
    # ordered list of service names and corresponding service codes and fees. The Provider Directory is sent
    # to the provider as an e-mail attachment.
    print("\nGenerating Provider Directory...")

    path = 'reports'
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path)
    # create new subdirectories for the current report
    provider_directory_file = path + "/provider_directory_" + Forms.date().replace(":", "_") + ".txt"

    serviceInfo = db.get_services()

    x = 0
    while x < len(serviceInfo):
        info = "\nService Name: " + serviceInfo[x][1] + \
               "\n\tService ID: " + str(serviceInfo[x][0]) + \
               "\n\tService Fee: " + str(serviceInfo[x][2]) + "\n"
        with open(provider_directory_file, "a") as f:
            f.write(info)
        x += 1

    print("Provider Directory Email Sent! (File created in reports folder)")



########################################################
# old reports below
########################################################


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

            serviceInfo = db.get_service(bill[5])  #Needed for displaying service name.
            providerInfo = db.get_provider(bill[2])    #Needed for displaying Provider name.

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
            serviceInfo = db.get_service(bill[5])  #Used for displaying service name and fee.
            memberInfo = db.get_member(bill[1])    #Used for displaying member name.

            # skip if it is a bad entry (bad serviceid, bad memberid)
            if serviceInfo is None or memberInfo is None:
                continue
            
            print("\n\tDate of Service: ", bill[3],
            "\n\tDate & Time Data Recieved: ", bill[4],
            "\n\tMember Name:", memberInfo[1],
            "\n\tMember ID: ", bill[1],
            "\n\tService Name: ", serviceInfo[1],
            "\n\tService ID:", bill[5],
            "\n\tFee to be paid: $", "{:.2f}".format(serviceInfo[2]))

            fee = serviceInfo[2]
            total_fee += fee
            total_con += 1  #keep track of consultations provided.

        print("\nTotal number of consultations: ", total_con)
        print("\nTotal service fees for the week: $", "{:.2f}".format(total_fee))
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
    #make sure the main report folder exists
    path = 'reports'
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path)
    #create new subdirectories for the current report
    report_path = path + "/manager_report_" + Forms.date().replace(":", "_") #no ":" in windows filenames
    os.makedirs(report_path)
    provider_path = report_path + "/providers"
    os.makedirs(provider_path)
    member_path = report_path + "/members"
    os.makedirs(member_path)

    providerInfo = db.get_providers()
    x = 0
    print("\nList of all Providers to get paid this week:\n")
    total_fee = 0.00
    total_con = 0
    total_prov = 0
    while x < len(providerInfo):
        #Currently is printing ALL of providers names from provider database. Should we randomly generate everytime to simulate a "week"?
        # solution: I will go through all the providers but skip them if they don't appear in the billing database
        #print("\t" + providerInfo[x][1])

        provider_file = provider_path + "/" + str(providerInfo[x][0]) + ".txt"

        billing = db.get_provider_billing(providerInfo[x][0])
        if billing is None:
            x += 1
            continue
        provider_total_fee = 0.00  # Total fee of services provided.
        provider_total_con = 0  # Total consultations provided by the Provider.
        total_prov += 1

        info = "\nProvider Name: " + providerInfo[x][1] +\
            "\nProvider ID Number: " + str(providerInfo[x][0]) +\
            "\nProvider Street Address: " + providerInfo[x][2] +\
            "\nProvider City: " + providerInfo[x][3] +\
            "\nProvider State: " + providerInfo[x][4] +\
            "\nProvider Zip Code: " + str(providerInfo[x][5]) +\
            "\n\nList of services provided by this Provider: \n"

        print(info) #print the info, same as before
        with open(provider_file, "a") as f:
            f.write(info)

        for bill in billing:
            serviceInfo = db.get_service(bill[5])  # Used for displaying service name and fee.
            memberInfo = db.get_member(bill[1])  # Used for displaying member name.

            # skip if it is a bad entry (bad serviceid, bad memberid)
            if serviceInfo is None or memberInfo is None:
                continue

            member_file = member_path + "/" + str(bill[1]) + ".txt"

            info = "\n\tDate of Service: " + bill[3] +\
                    "\n\tDate & Time Data Recieved: " + bill[4] +\
                    "\n\tMember Name:" + memberInfo[1] +\
                    "\n\tMember ID: " + str(bill[1]) +\
                    "\n\tService Name: " + serviceInfo[1] +\
                    "\n\tService ID:" + str(bill[5]) +\
                    "\n\tFee to be paid: $" + "{:.2f}".format(serviceInfo[2])

            print(info)
            with open(provider_file, "a") as f:
                f.write(info)
            with open(member_file, "a") as f:
                f.write(info)

            fee = serviceInfo[2]
            provider_total_fee += fee
            provider_total_con += 1  # keep track of consultations provided.

        #case: provider had bills but all bills were invalid
        if provider_total_con == 0:
            x += 1
            continue

        info = "\nTotal consults this Provider had: " + str(provider_total_con) +\
                "\nTotal fees: $" + "{:.2f}".format(provider_total_fee)
        print(info)
        with open(provider_file, "a") as f:
            f.write(info)

        total_fee += provider_total_fee
        total_con += provider_total_con
        x += 1
    
    #Total number of providers, should we just add all providers in the database?
    #Total number of consultations we can add all the services provided from member services database.
    #Overall fees will be ALL services across all members added up
    print("\nTotal number of Providers who provided services this week: ", total_prov,
          "\nTotal Number of Consultations: ", total_con,
          "\nOverall fees: $", "{:.2f}".format(total_fee))



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