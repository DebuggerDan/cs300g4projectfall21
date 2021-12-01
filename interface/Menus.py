"""
This is a basic outline of the menu and functions that will be called for each menu item.
There is more to elborate of course, including error cases and exception handling.
I tried to include the normal flow of information, and I can elaborate more on each case and such,
this is just a rough outline of how I am currently envisioning the menu functionality and database/menu
interactions.
These also give some testing capabilities for some of the "background" processes and allow us to manually trigger them.

Feel free to break it down even more or add further case handling scenarios or specific function calls.

Some prototypes I will make:
displayMenu(int menu_code); //displays the associated menu (1 - main menu, 2 - IAM menu, 3 - report menu)
displayError(int error_code); //displays asociated error message
displayWelcome(int display_code); //displays message based on given code number

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
