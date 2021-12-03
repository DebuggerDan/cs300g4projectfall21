# basic forms for user input
# once validation is added, input will return 0 if invalid

from datetime import datetime

from database.database import Database as DB
from security.sec import loginChecker, serviceChecker, nameChecker, rangeChecker, isValidSelection


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
        print(Forms.billingForm())

    ################################################################################################
    #
    # Basic input elements which include validation
    # These functions are fine to call on their own
    # Full forms (below) can also be built using these pieces
    #
    ################################################################################################

    # add forms
    @staticmethod
    def addMemberForm():
        name = input("Enter name: ")
        street = input("Enter street: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip = input("Enter Zip: ")
        # phone = input("Enter Phone: ")
        # fax = input("Enter Fax: ")
        # email = input("Enter Email: ")
        # service_id = input("Enter Service ID: ")
        active = 1

        good = 1
        if not nameChecker(name) == 3:
            print("Invalid name")
            good = 0
        if not rangeChecker(zip, 10000, 99999) == 3:
            print("Invalid zip")
            good = 0
        # if not isPhonenum(phone) == 3:
        #    print("Invalid Phone")
        #    good = 0
        # if not isPhonenum(fax) == 3:
        #    print("Invalid Fax")
        #    good = 0
        # if not serviceChecker(service_id) == 3:
        #    print("Invalid service ID")
        #    good = 0

        if good == 0:
            return 0
        # return name, street, city, state, zip, phone, fax, email, service_id
        return name, street, city, state, zip, active

    @staticmethod
    def addProviderForm():
        name = input("Enter name: ")
        street = input("Enter street: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip = input("Enter Zip: ")

        good = 1
        if not nameChecker(name) == 3:
            print("Invalid name")
            good = 0
        if not rangeChecker(zip, 10000, 99999) == 3:
            print("Invalid zip")
            good = 0

        if good == 0:
            return 0
        return name, street, city, state, zip

    @staticmethod
    def addServiceForm():
        name = input("Enter name: ")
        fee = input("Enter fee: ")

        good = 1
        if not nameChecker(name) == 3:
            print("Invalid name")
            good = 0
        if not rangeChecker(fee, 0, 999):
            print("Invalid fee")
            good = 0

        if good == 0:
            return 0
        return name, fee

    # id forms

    @staticmethod
    def providerIDForm():
        provider_id = input("Enter Provider ID: ")  # changed id to provider_id as id shadows a built-in function

        if not loginChecker(provider_id) == 3:
            print("Invalid ID")
            return 0
        return provider_id

    @staticmethod
    def memberIDForm():
        member_id = input("Enter Member ID: ")  # changed id to member_id as it shadows a built-in function

        if not loginChecker(member_id) == 3:
            print("Invalid ID")
            return 0
        return id

    @staticmethod
    def serviceIDForm():
        service_id = input("Enter Service ID: ")  # changed id to service_id as it shadows a built-in function

        if not serviceChecker(service_id) == 3:
            print("Invalid ID")
            return 0
        return id

    # name forms

    @staticmethod
    def providerNameForm():
        name = input("Enter Provider Name: ")

        if not nameChecker(name) == 3:
            print("Invalid Name")
            return 0
        return name

    @staticmethod
    def memberNameForm():
        name = input("Enter Member Name: ")

        if not nameChecker(name) == 3:
            print("Invalid Name")
            return 0
        return name

    @staticmethod
    def serviceNameForm():
        service_id = input("Enter Service Name: ")  # replaced id with service_id as it shadows a built-in function

        # nameChecker requires that there be a space
        # can't use here
        return service_id

    # menu form

    @staticmethod
    def menuSelectForm():
        num = input("Menu Selection: ")

        if not isValidSelection(num):
            print("Invalid Selection")
            return 0
        return num

    # member service form

    @staticmethod
    def dateForm():
        mm = input("Please enter the month (MM): ")
        dd = input("Please enter the day (DD): ")
        yyyy = input("Please enter the year (YYYY): ")

        good = 1
        if not rangeChecker(mm, 1, 12) == 3:
            print("Invalid Month")
            good = 0
        if not rangeChecker(dd, 1, 31) == 3:
            print("Invalid Day")
            good = 0
        if not rangeChecker(yyyy, 1900, 2100) == 3:
            print("Invalid Year")
            good = 0

        if good == 0:
            return 0
        # date = mm + "-" + dd + "-" + yyyy
        date = yyyy + "-" + mm + "-" + dd
        return date

    # (not "input" like the rest, but I had to put it somewhere)
    @staticmethod
    def date():
        # from datetime import datetime
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        return date

    @staticmethod
    def commentForm():
        comments = input("Please enter your comments: ")
        # technically should be a max of 100 characters
        # would need a validation function for that
        return comments

    @staticmethod
    def verificationForm():
        agree = input("Is this information valid? y/n: ")
        # no validation needed, just check for 'y' and consider anything else no
        return agree

    ################################################################################################
    #
    # FULL PROVIDER FORM FOR ENTERING A SERVICE PERFORMED
    # comments are copy/pasted from naya's doc
    #
    ################################################################################################

    # pass in the user object to access the ID of the logged in provider
    @staticmethod
    def billingForm(user):

        # (Provider enters member number)
        member_id = 0
        while member_id == 0:
            member_id = Forms.memberIDForm()

        # Provider enters the current date: MM-DD-YYYY (actually service date)
        service_date = 0
        while service_date == 0:
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

            # (make sure the id entered was actually valid)
            service = DB.get_service(service_id)
            if not service:
                print("Error: Invalid service code. Please search again.")
                continue

            # Display it back to the Provider and ask them to verify if it is the correct service.
            print("ID: " + service_id + "\nName: " + service_name + "\n")
            verify = Forms.verificationForm()

        # Provider enter additional comments as needed.
        comments = 0
        while comments == 0:
            comments = Forms.commentForm()

        # extra pieces
        current_date = Forms.date()
        # the provider is logged in so their id should be available somewhere
        provider_id = user[0]

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

        if verify == "n":
            return 0

        DB.add_billing(member_id, provider_id, service_date, current_date, service_id, comments)
        return member_id, provider_id, service_date, current_date, service_id, comments
