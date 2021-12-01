#basic forms for user input
#once validation is added, input will return 0 if invalid

from datetime import datetime
from database.database import Database as DB

class Forms:

    @staticmethod
    def testForms():
        # print("\nADD MEMBER FORM\n")
        # print(Forms.addMemberForm())
        # print("\nADD PROVIDER FORM\n")
        # print(Forms.addProviderForm())
        # print("\nADD SERVICE FORM\n")
        # print(Forms.addServiceForm())
        #
        # print("\nMEMBER ID FORM\n")
        # print(Forms.memberIDForm())
        # print("\nPROVIDER ID FORM\n")
        # print(Forms.providerIDForm())
        # print("\nSERVICE ID FORM\n")
        # print(Forms.serviceIDForm())
        #
        # print("\nMEMBER NAME FORM\n")
        # print(Forms.memberNameForm())
        # print("\nPROVIDER NAME FORM\n")
        # print(Forms.providerNameForm())
        # print("\nSERVICE NAME FORM\n")
        # print(Forms.providerNameForm())
        #
        # print("\nMENU SELECTION FORM\n")
        # print(Forms.menuSelectForm())
        #
        # print("\nDATE FORM\n")
        # print(Forms.dateForm())
        # print("\nDATE\n")
        # print(Forms.date())
        # print("\nMENU SELECTION FORM\n")
        # print(Forms.commentForm())

        print("\nFull Service Form\n")
        print(Forms.provideServiceForm())


    ################################################################################################
    #
    # Basic input elements which include validation
    # These functions are fine to call on their own
    # Full forms (below) can also be built using these pieces
    #
    ################################################################################################

    #add forms
    @staticmethod
    def addMemberForm():
        name = input("Enter name: ")
        street = input("Enter street: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip = input("Enter Zip: ")
        phone = input("Enter Phone: ")
        fax = input("Enter Fax: ")
        email = input("Enter Email: ")
        service_id = input("Enter Service ID: ")
        return name, street, city, state, zip, phone, fax, email, service_id

    @staticmethod
    def addProviderForm():
        return Forms.addMemberForm()

    @staticmethod
    def addServiceForm():
        name = input("Enter name: ")
        fee = input("Enter fee: ")
        return name, fee

    #id forms

    @staticmethod
    def providerIDForm():
        id = input("Enter Provider ID: ")
        return id

    @staticmethod
    def memberIDForm():
        id = input("Enter Member ID: ")
        return id

    @staticmethod
    def serviceIDForm():
        id = input("Enter Service ID: ")
        return id

    #name forms

    @staticmethod
    def providerNameForm():
        name = input("Enter Provider Name: ")
        return name

    @staticmethod
    def memberNameForm():
        name = input("Enter Member Name: ")
        return name

    @staticmethod
    def serviceNameForm():
        id = input("Enter Service Name: ")
        return id

    #menu form

    @staticmethod
    def menuSelectForm():
        num = input("Menu Selection: ")
        return num


    #member service form

    @staticmethod
    def dateForm():
        mm = input("Please enter the month (MM): ")
        dd = input("Please enter the day (DD): ")
        yyyy = input("Please enter the month (YYYY): ")
        date = mm + "-" + dd + "-" + yyyy
        return date

    #(not "input" like the rest, but I had to put it somewhere)
    @staticmethod
    def date():
        #from datetime import datetime
        now = datetime.now()
        date = now.strftime("%d-%m-%Y %H:%M:%S")
        return date

    @staticmethod
    def commentForm():
        comments = input("Please enter your comments: ")
        return comments

    @staticmethod
    def verificationForm():
        agree = input("Is this information valid? y/n: ")
        return agree



    ################################################################################################
    #
    # FULL PROVIDER FORM FOR ENTERING A SERVICE PERFORMED
    # comments are copy/pasted from naya's doc
    #
    ################################################################################################


    @staticmethod
    def provideServiceForm():

        # (Provider enters member number)
        member_id = Forms.memberIDForm()

        # Provider enters the current date: MM-DD-YYYY (actually service date)
        service_date = Forms.dateForm()

        verify = "n"
        while verify == "n":

            # (Provider looks up service)
            service_name = Forms.serviceNameForm()

            services = DB.get_services_by_name(service_name)
            if not services:
                print("No services with name '" + service_name + "' found\n")
                print("Hint: Try 'Punishment'")
                continue

            print("Search results for service name '" + service_name + "':\n")
            print(services)

            # Provider enters the 6-digit code for the chosen service.
            service_id = Forms.serviceIDForm()

            #(make sure the id entered was actually valid)
            service = DB.get_service(service_id)
            if not service:
                print("Error: Invalid service code. Please search again.")
                continue

            # Display it back to the Provider and ask them to verify if it is the correct service.
            print("ID: " + service_id + "\nName: " + service_name + "\n")
            verify = Forms.verificationForm()

        # Provider enter additional comments as needed.
        comments = Forms.commentForm()

        #extra pieces
        current_date = Forms.date()
        #the provider is logged in so their id should be available somewhere
        provider_id = 0

        # The following information is now stored about the member:
        # Current date and time (MM-DD-YYYY HH:MM:SS).
        # Date service was provided (MM-DD-YYYY).
        # Provider number (9 digits).
        # Member number (9 digits).
        # Service code (6 digits).
        # Comments (100 characters) (optional)

        # Software will look up the fee for the service and display it to the Provider.
        service = DB.get_service(service_id)
        fee = service[2]

        # The Provider will need to verify all the information by filling out a verification form with:
        # Current date and time.
        # Date of the service that was provided
        # Member name and number
        # Service code
        # Fee to be paid

        print("\nInformation Verification:")
        print("\n\tCurrent date and time: " + current_date)
        print("\tService Date: " + service_date)
        print("\tMember Number: " + member_id)
        print("\tService code: " + service_id)
        print("\tFee to be paid: " + str(fee))
        verify = Forms.verificationForm()

        if (verify == "n"):
            return 0

        return current_date, service_date, provider_id, member_id, service_id, comments, fee






