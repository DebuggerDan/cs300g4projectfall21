"""
This is a basic outline of the menu and functions that will be called for each menu item.
There is more to elborate of course, including error cases and exception handling.
I tried to include the normal flow of information, and I can elaborate more on each case and such,
this is just a rough outline of how I am currently envisioning the menu functionality and database/menu
interactions.
These also give some testing capabilities for some of the "background" processes and allow us to manually trigger them.

Feel free to break it down even more or add further case handling scenarios or specific function calls.


Process of interactions:

Login screen:
    Asks for provider number
        checks if provider number is valid in data base
            if not valid number
                returns error message and denies access
            if valid number
                checks if manager flag
                    if number is manager
                        returns welcome message, grants access, moves to main menu (manager view)
                    if number not a manager
                        returns welcome message and grants access and moves to main menu (provider view)

Main Menu Screen:
    Display menu:
        1 - Enter Member Service Entry (must go through process of checking member number validity, 
                                        then enter service code, creates provider and member entry, 
                                        returns to main menu)
        2 - Request Member Info (queries member database by name or number, 
                                  then displays info, then returns to main menu)
        3 - Request Provider Info (queries provider database by name or number, 
                                    then displays info, then returns to main menu)
        4 - Request Service Code (queries service code directory by name or number, 
                                  then displays info, then returns to main menu)
        5 - Interactive Mode (IAM) (add/delete/modify databases, goes to IAM menu, 
                                    exits back to main menu when user exits)
        6 - Generate Reports (Manager Only) (only accessible if user has manager credentials, 
                                              generate all reports from report menu, 
                                              exits back to main menu when user exits)
        7 - Exit
        
    Interactive Mode Menu (IAM Menu):
        1 - Add Member (adds new member to database, takes member name and address, 
                         and randomly generates number that isn't assigned in the database)
        2 - Delete Member (Deletes member by name or number, requires confirmation, removes member from database entirely)
        3 - Modify Member Info (modifies existing member's name and address, cannot modify member number)
        4 - Add Provider (adds new provider to database, takes provider name and address,
                           randomly generates provider numebr that isn't assigned in the database)
        5 - Delete Provider (deletes provider by name or number, cannot delete provider that is logged in,
                              cannot delete manager unless are logged in as manager, 
                              cannot delete supervisor 000000000 provider number)
        6 - Modify Provider (modifies existing provider's name and address, cannot modify provider number)
        7 - Update Member Statuses (checks member accounts for fees and compare to amounts paid, if not zero, 
                                    then the member status is set to 'SUSPENDED', this process will be automated,
                                    but for testing purposes I have included it in the IAM menu)
        8 - Exit (returns to main menu)
    
    Generate Reports Menu (Manager Only):
        1 - Member Summary Report (lists member's name, number, address, 
                                    and each service provided to the member, 
                                    including date, service name, and provider)
        2 - Provider Summary Report (lists provider's name, number, address, 
                                      and each service they provided, 
                                      date service was provided, 
                                      the date and time the service was entered, 
                                      the member's name and number, the service name and code, 
                                      and the fee to be paid, and totals up the number of 
                                      services provided and the total fees to be paid for the week)
        3 - Accounts Payable/Manager Summary Report (lists every provider to be paid for the week,
                                                      how many consultations each provider had, 
                                                      and their total fee for the week, then summarizes
                                                      the total number of providers who had consultations this week,
                                                      the total number of all consultations for the week,
                                                      and the total fee amount to be paid, this report has all the info
                                                      for an EFT file)
        4 - Exit (returns to main menu)
"""
