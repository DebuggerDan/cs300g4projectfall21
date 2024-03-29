# CS 300 - Group (#4) Project: ChocAn [Section: Menu Displays and Functions] - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang

from security.auth import is_manager
from comm.comm import querProvInfo, querMemInfo, querServInfo
from comm.comm import newProviderReport, newMemberReport, newEFTReport, \
    newSummaryReport, newMAPReport, providerDirectory
from interface.forms import Forms



def displayMenu(user): #displays main menu items
    print("\nChocAn Main Menu:")
    print("\t1 - Enter Member Service Entry.")
    print("\t2 - Request Member Info.")
    print("\t3 - Request Provider Info.")
    print("\t4 - Request Service Code Info.")
    print("\t5 - Request Provider Directory.")
    print("\t6 - Interactive Mode Menu (IAM)")
    #waiting for how manager is flagged from login function
    if (is_manager(user)): #checks if manager
        print("\t7 - Generate Reports Menu")
    print("\t8 - Log Out.")

def mainMenu(user): #main menu loop function
    menu_code = 0 #menu input
    while menu_code != 8: #while user does not want to log out
        displayMenu(user) #displays menu items
        menu_code = input("Please enter the Main Menu Item number: ") #asks for user input
        if menu_code.isdigit():
            menu_code = int(menu_code)
        else:
            menu_code = 0
        if (menu_code > 8 or menu_code < 1):
            print("\nInvalid Main Menu Item: Please select a number from the provided menu.")
            menu_code = 0
        else:
            if (menu_code == 0):
                print("\nPlease enter a Main Menu Item number (whole numbers from 1 to 8).")
                menu_code = 0
            elif (menu_code == 1):
                #Enter Service Entry function
                Forms.billingForm(user)

            elif (menu_code == 2):
                #Query Member Info
                #print("Query Member Info function goes here")
                querMemInfo()
            elif (menu_code == 3):
                #Query Provider Info
                #print("Query Provider Info function goes here")
                querProvInfo()
            elif (menu_code == 4):
                #Query Service Code Info
                #print("Query Service Code Info function goes here")
                querServInfo()
            elif (menu_code == 5):
                #provider directory (written to file)
                providerDirectory()
            elif (menu_code == 6):
                #IAM menu loop
                iamMenu(user)
            elif (menu_code == 7):
                #check if manager logged in
                if (is_manager(user)):
                    # if manager logged in, then execute report menu loop
                    reportMenu(user)
                #else display error message and set menu_code = 0
                else:
                    print("Permission Denied.")
                    menu_code = 0
            elif (menu_code == 8):
                #print log out message and exit to authentication login screen
                #logout(user)
                print("\n\nThank you for using the ChocAn Healthcare Suite!\nLogging out...\n")
            else:
                print("\nPlease enter a valid Main Menu Item number.\n")

def displayIAM():
    print("\nInteractive Mode Menu:")
    print("\t1 - Add Member.")
    print("\t2 - Delete Member.")
    print("\t3 - Modify Member.")
    print("\t4 - Add Provider.")
    print("\t5 - Delete Provider.")
    print("\t6 - Modify Provider.")
    print("\t7 - Add Service.")
    print("\t8 - Delete Service.")
    print("\t9 - Modify Service.")
    print("\t10- Exit IAM Menu.")
                
def iamMenu(user):
    menu_code = 0
    while (menu_code != 10):
        displayIAM()
        menu_code = input("\nPlease enter the IAM Menu Item number: ")
        if menu_code.isdigit():
            menu_code = int(menu_code)
        else:
            menu_code = 0
    #while menu_code != 8: #after input = impossible to change menu selection
        if (menu_code > 10 or menu_code < 1):
            print("\n\nInvalid IAM Menu Item: Please select a number from the provided menu.\n")
            menu_code = 0
        else:
            if (menu_code == 1):
                #Add member input and function
                #print("Add member function goes here")
                Forms.addMemberForm()
            elif (menu_code == 2):
                #Delete member input and function
                #print("Delete member function goes here")
                Forms.killMember()
            elif (menu_code == 3):
                #Modify member input and function
                #print("Modify member function goes here")
                Forms.editMember()
            elif (menu_code == 4):
                #Add provider input and function
                #print("Add provider function goes here")
                Forms.addProviderForm()
            elif (menu_code == 5):
                #Delete provider input and function
                #print("Delete provider function goes here")
                Forms.killProvider()
            elif (menu_code == 6):
                #Modify provider input and function
                #print("Modify provider function goes here")
                Forms.editProvider()
            elif (menu_code == 7):
                Forms.addServiceForm()
            elif (menu_code == 8):
                Forms.killService()
            elif (menu_code == 9):
                Forms.editService()
            elif (menu_code == 10):
                #print log out message from IAM menu and exits to main menu
                print("Returning to the ChocAn Main Menu...")
                #mainMenu(user) #returning, not calling a new one :)
            else:
                print("\nPlease enter a valid IAM Menu Item number.")
                

def displayReport():
    print("\nGenerate Reports Menu:")
    print("\t1 - Generate a Member Report.")
    print("\t2 - Generate a Provider Report.")
    print("\t3 - Generate a EFT Report.")
    print("\t4 - Generate a Summary Report.")
    print("\t5 - Perform the Main Accounting Procedure (Runs All Reports).")
    print("\t6 - Exit Report Menu.")

def reportMenu(user):
    menu_code = 0
    while menu_code != 6:
        displayReport()
        menu_code = input("Please enter the Reports Menu Item number: ")
        if menu_code.isdigit():
            menu_code = int(menu_code)
        else:
            menu_code = 0
    #while menu_code != 4: #this is after the input again, oops
        if (menu_code > 6 or menu_code < 1):
            print("\nInvalid Reports Menu Item: Please select a number from the provided menu.")
            menu_code = 0
        else:
            if (menu_code == 0):
                print("\nPlease enter a Reports Menu Item number (whole numbers from 1 to 6).")
                menu_code = 0
            elif (menu_code == 1):
                #Print member summary report by member id
                newMemberReport()
            elif (menu_code == 2):
                #Print provider summary report by provider id
                newProviderReport()
            elif (menu_code == 3):
                # Print EFT Report
                newEFTReport()
            elif (menu_code == 4):
                # Print manager accounts payable report
                newSummaryReport()
            elif (menu_code == 5):
                # initializes main accounting procedure (runs all 4 reports above)
                newMAPReport()
            elif (menu_code != 6):
                print("\nPlease enter a valid Reports Menu Item number.\n")


"""
Process of interactions:

Login screen:
    Asks for provider number - Authenticate(int user_id)
        checks if provider number is valid in data base - checkProviderID(int user_id)
            if (user_id == -1)
                displayError(int error_code); //displays Successful log out screen and ends program
            if not valid number 
                returns error message and denies access - displayError(int error_code); return false;
            if valid number
                checks if manager flag - isManager(int user_id)
                    if number is manager
                        returns welcome message, grants access, moves to main menu (manager view) - displayWelcome(int display_code);
                    if number not a manager
                        returns welcome message and grants access and moves to main menu (provider view) - displayWelcome(int display_code);

//hold provider_id in "global" variable = logged_in

Main Menu Screen:
    Display menu:
        1 - Enter Member Service Entry (must go through process of checking member number validity, 
                                        then enter service code, creates provider and member entry, returns to main menu)
            addServiceEntry(int member_id, int logged_in, int service_id, String date_provided); //provider enters in member service provided
            displayServiceEntry(); //displays newly entered service provided entry
            
        2 - Request Member Info (queries member database by name or number, 
                                  then displays info, then returns to main menu)
            displayMember(int member_id); //displays member account based on member id
            displayMember(String name); //displays member account based on name
            
        3 - Request Provider Info (queries provider database by name or number, 
                                    then displays info, then returns to main menu)
            displayProvider(int provider_id); //displays provider info based on provider id (if manager, will display that they are manager)
            displayProvider(String name); //displays provider info based on name
            
        4 - Request Service Code (queries service code directory by name or number, 
                                  then displays info, then returns to main menu)
            displayServiceCodes(); //lists all active service codes
            displayServiceCode(int service_id); //displays service based on id
            displayServiceCode(String name); //displays service based on name
            
        5 - Interactive Mode (IAM) (add/delete/modify databases, goes to IAM menu, 
                                    exits back to main menu when user exits)
            Loop:
            displayMenu(int menu_code == 2); //displays IAM menu - see IAM menu for prototypes
            
        6 - Generate Reports (Manager Only) (only accessible if user has manager credentials, 
                                              generate all reports from report menu, 
                                              exits back to main menu when user exits)
            Loop:
            displayMenu(int menu_code == 3); //displays report menu - see report menu for prototypes
            
        7 - Exit
            //ends loop check case - logs out to authentication screen
            
    Interactive Mode Menu (IAM Menu):
        1 - Add Member (adds new member to database, takes member name and address, 
                         and randomly generates number that isn't assigned in the database)
            addMember(String name, String address); //will assign member ID number to account
            displayMember(int member_id); //diplays member information and provides newly created member id number to user
            
        2 - Delete Member (Deletes member by name or number, requires confirmation, removes member from database entirely)
            removeMember(int member_id); //removes member by id
            removeMember(String name); //removes member by name
            
        3 - Modify Member Info (modifies existing member's name and address, cannot modify member number)
            modifyMember(int member_id); //searches for member entry to modify
                displayMember(int member_id); //displays member matching member id
                displayMenu(int menu_code); //asks user what they want to modify
                editMember(String name); //edits name
                editMember(String address); //edits address
                //I would be down to add more methods that modified the services provided entries for each member but it's not "required"
                
        4 - Add Provider (adds new provider to database, takes provider name and address,
                           randomly generates provider numebr that isn't assigned in the database)
            addProvider(String name, String address); //creates provider and generates unassigned provider id
            displayProvider(int provider_id); //displays provider information and shows newly created provider id number
            
        5 - Delete Provider (deletes provider by name or number, cannot delete provider that is logged in,
                              cannot delete manager unless are logged in as manager, 
                              cannot delete supervisor 000000000 provider number)
            removeProvider(int provider_id); //deletes provider based on id number
            removeProvider(String name); //deletes provider based on name
                ^^^ will not delete if provider_id == 000000000 OR provider_id == logged_in OR checkManager(provider_id) == True
            
        6 - Modify Provider (modifies existing provider's name and address, cannot modify provider number)
        modifyProvider(int provider_id); //searches for provider entry to modify
                displayProvider(int provider_id); //displays provider matching member id
                displayMenu(int menu_code); //asks user what they want to modify
                editProvider(String name); //edits name
                editProvider(String address); //edits address
                //I would be down to add more methods that modified the services provided entries for each provider but it's not "required"
                
        7 - Update Member Statuses (checks member accounts for fees and compare to amounts paid, if not zero, 
                                    then the member status is set to 'SUSPENDED', this process will be automated,
                                    but for testing purposes I have included it in the IAM menu)
            setStatus(int member_id, int new_status); //changes member to given status 1 - Active, 2 - Suspended, 3 - Inactive
            setStatus(); //goes through all members, checks (fees) - (paid), if result == 0, then status = 1, else status = 2
            
        8 - Exit (returns to main menu)
            //exits loop, returns user to main menu
    
    Generate Reports Menu (Manager Only):
        1 - Member Summary Report (lists member's name, number, address, 
                                    and each service provided to the member, 
                                    including date, service name, and provider)
            displayMemberReport(int member_id); //displays member name and address, all services received (service name, code, date received, fee amount per line), and total services received and total fee to be paid for the week
            
        2 - Provider Summary Report (lists provider's name, number, address, 
                                      and each service they provided, 
                                      date service was provided, 
                                      the date and time the service was entered, 
                                      the member's name and number, the service name and code, 
                                      and the fee to be paid, and totals up the number of 
                                      services provided and the total fees to be paid for the week)
            displayProviderReport(int provider_id); //displays provider's name and address, all services provided (service name, code, date provided, and fee per line), and total services provided and total fee to receive for the week
        
        3 - Accounts Payable/Manager Summary Report (lists every provider to be paid for the week,
                                                      how many consultations each provider had, 
                                                      and their total fee for the week, then summarizes
                                                      the total number of providers who had consultations this week,
                                                      the total number of all consultations for the week,
                                                      and the total fee amount to be paid, this report has all the info
                                                      for an EFT file)
        displayManagerReport(); //displays per line, each provider, their provider id number, the total number of services provided, the total fee amount, and at the bottom it totals all services provided and all fees to be paid out
        
        4 - Exit (returns to main menu)
            //exits loop, returns user to main menu
"""
