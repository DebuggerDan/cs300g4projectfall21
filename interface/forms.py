#basic forms for user input
#once validation is added, input will return 0 if invalid

from datetime import datetime
from database.database import Database as DB
from security.sec import loginChecker, serviceChecker, nameChecker, rangeChecker, isValidSelection


class Forms:


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
        name = input("Enter Member Name: ")
        street = input("Enter Street: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip = input("Enter Zip: ")
        #phone = input("Enter Phone: ")
        #fax = input("Enter Fax: ")
        #email = input("Enter Email: ")
        #service_id = input("Enter Service ID: ")
        active = 1

        good = 1
        if not nameChecker(name) == 3:
            print("Invalid Member Name!")
            good = 0
        if not rangeChecker(zip, 10000, 99999) == 3:
            print("Invalid Zip!")
            good = 0
        #if not isPhonenum(phone) == 3:
            #print("Invalid Phone")
            #good = 0
        #if not isPhonenum(fax) == 3:
        #    print("Invalid Fax")
         #   good = 0
        #if not serviceChecker(service_id) == 3:
        #    print("Invalid service ID")
        #    good = 0

        if good == 0:
            return 0
        #return name, street, city, state, zip, phone, fax, email, service_id
        #return name, street, city, state, zip, active
        DB.add_member(name, street, city, state, zip, active)
        return 1

    @staticmethod
    def addProviderForm():
        name = input("Enter Provider Name: ")
        street = input("Enter Street: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip = input("Enter Zip: ")

        good = 1
        if not nameChecker(name) == 3:
            print("Invalid Provider Name!")
            good = 0
        if not rangeChecker(zip, 10000, 99999) == 3:
            print("Invalid Zip!")
            good = 0

        if good == 0:
            return 0
        #return name, street, city, state, zip
        DB.add_provider(name, street, city, state, zip)
        return 1

    @staticmethod
    def addServiceForm():
        name = input("Enter Service Name: ")
        fee = input("Enter Service Fee: ")

        good = 1
        if not nameChecker(name) == 3:
            print("Invalid Service Name!")
            good = 0
        if not rangeChecker(fee, 0, 999):
            print("Invalid Service Fee!")
            good = 0

        if good == 0:
            return 0
        #return name, fee
        DB.add_service(name, fee)
        return 1

    #id forms

    @staticmethod
    def providerIDForm():
        id = input("Enter Provider ID: ")

        if not loginChecker(id) == 3:
            print("Invalid Provider ID!")
            return 0
        return id

    @staticmethod
    def memberIDForm():
        id = input("Enter Member ID: ")

        if not loginChecker(id) == 3:
            print("Invalid Member ID!")
            return 0
        return id

    @staticmethod
    def serviceIDForm():
        id = input("Enter Service ID: ")

        if not serviceChecker(id) == 3:
            print("Invalid Service ID!")
            return 0
        return id

    #name forms

    @staticmethod
    def providerNameForm():
        name = input("Enter Provider Name: ")

        if not nameChecker(name) == 3:
            print("Invalid Provider Name!")
            return 0
        return name

    @staticmethod
    def memberNameForm():
        name = input("Enter Member Name: ")

        if not nameChecker(name) == 3:
            print("Invalid Member Name!")
            return 0
        return name

    @staticmethod
    def serviceNameForm():
        id = input("Enter Service Name: ")

        #nameChecker requires that there be a space
        #can't use here
        return id

    #menu form

    @staticmethod
    def menuSelectForm():
        num = input("Menu Selection: ")

        if not isValidSelection(num):
            print("Invalid Menu Selection!")
            return 0
        return num


    #member service form

    @staticmethod
    def dateForm():
        mm = input("Please enter the month (MM): ")
        dd = input("Please enter the day (DD): ")
        yyyy = input("Please enter the year (YYYY): ")

        good = 1
        if not rangeChecker(mm, 1, 12) == 3:
            print("Invalid Month!")
            good = 0
        if not rangeChecker(dd, 1, 31) == 3:
            print("Invalid Day!")
            good = 0
        if not rangeChecker(yyyy, 1900, 2100) == 3:
            print("Invalid Year!")
            good = 0

        if good == 0:
            return 0
        #date = mm + "-" + dd + "-" + yyyy
        date = yyyy + "-" + mm + "-" + dd
        return date

    #(not "input" like the rest, but I had to put it somewhere)
    @staticmethod
    def date():
        #from datetime import datetime
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        return date

    @staticmethod
    def commentForm():
        comments = input("Please enter your comments: ")
        #technically should be a max of 100 characters
        #would need a validation function for that
        return comments

    @staticmethod
    def verificationForm():
        agree = input("Is this information valid? Please enter y or n: ")
        #no validation needed, just check for 'y' and consider anything else no
        return agree



    ################################################################################################
    #
    # FULL PROVIDER FORM FOR ENTERING A SERVICE PERFORMED
    # comments are copy/pasted from naya's doc
    #
    ################################################################################################


    #pass in the user object to access the ID of the logged in provider
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
        service_id = 0

        verify = "n"
        while verify == "n":

            # (Provider looks up service)
            service_name = Forms.serviceNameForm()

            services = DB.get_services_by_name(service_name)
            if not services:
                print("No Services with Service Name of '" + service_name + "' was found\n")
                print("Hint: Try 'Punishment'")
                continue

            print("Search results for Service Name '" + service_name + "':\n")
            print(services)

            # Provider enters the 6-digit code for the chosen service.
            service_id = Forms.serviceIDForm()

            #(make sure the id entered was actually valid)
            service = DB.get_service(service_id)
            if not service:
                print("Error: Invalid Service Code. Please search again.")
                continue

            # Display it back to the Provider and ask them to verify if it is the correct service.
            print("Service ID: " + service_id + "\nService Name: " + service_name + "\n")
            verify = Forms.verificationForm()

        # Provider enter additional comments as needed.
        comments = 0
        while (comments == 0):
            comments = Forms.commentForm()

        #extra pieces
        current_date = Forms.date()
        #the provider is logged in so their id should be available somewhere
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
        print("\n\tCurrent Date and Time: " + current_date)
        print("\tService Date: " + service_date)
        print("\tMember Number: " + member_id)
        print("\tService Code: " + service_id)
        print("\tFee to be paid: " + str(fee))
        verify = Forms.verificationForm()

        if (verify == "n"):
            return 0

        DB.add_billing(member_id, provider_id, service_date, current_date, service_id, comments)
        return member_id, provider_id, service_date, current_date, service_id, comments

    @staticmethod
    def killMember():
        memID = input("ID of Member being deleted: ")
        valID = loginChecker(memID)
        if valID != 3:
            print("Invalid Member ID Format. Returning.")
            return -1
        userData = DB.get_member(memID)
        if userData == "None":
            print("Member already does not exist. Returning.")
            return -1
        print(userData)
        choice = input("Remove Member? y/n: ")
        if choice == "y":
            DB.delete_member(memID)
            print("Member deleted!")
            return 1
        else:
            return -1

    @staticmethod
    def killProvider():
        provID = input("ID of Provider being deleted: ")
        valID = loginChecker(provID)
        if valID != 3:
            print("Invalid Provider ID Format. Returning.")
            return -1
        userData = DB.get_member(provID)
        if userData == "None":
            print("Provider already does not exist. Returning.")
            return -1
        print(userData)
        choice = input("Remove Provider? y/n: ")
        if choice == "y":
            DB.delete_provider(provID)
            print("Provider deleted!")
            return 1
        else:
            return -1

    @staticmethod
    def killService():
        servID = input("ID of Service being deleted: ")
        valID = serviceChecker(servID)
        if valID != 3:
            print("Invalid Service ID Format. Returning.")
            return -1
        serviceData = DB.get_service(servID)
        if serviceData == "None":
            print("Service already does not exist. Returning.")
            return -1
        print(serviceData)
        choice = input("Remove Service? y/n: ")
        if choice == "y":
            DB.delete_service(servID)
            print("Service deleted! Poof!")
            return 1
        else:
            return -1

    @staticmethod
    def editMember():
        memID = input("ID of Member being edited: ")
        valID = loginChecker(memID)
        if valID != 3:
            print("Invalid Member ID Format. Returning.")
            return -1
        userData = DB.get_member(memID)
        if userData == "None":
            print("Member does not exist. Returning.")
            return -1
        print(userData)
        name = input("Enter Member Name: ")
        street = input("Enter Street: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip = input("Enter Zip: ")
        active = input("Enter Member Activity State, enter 0 or 1: ")
        if not nameChecker(name) == 3:
            print("Invalid Member Name. Keeping old Member Name.")
            name = userData[1]
        if not rangeChecker(zip, 10000, 99999) == 3:
            print("Invalid Zip. Keeping old Zip.")
            zip = userData[5]
        if active != 1 or 0:
            print("Invalid Member Activity State. Keeping old Activity State. (Make sure to enter a 1 or a 0).")
            active = userData[6]
        DB.update_member(memID, name, street, city, state, zip, active)
        return 1

    @staticmethod
    def editProvider():
        provID = input("ID of Provider being edited: ")
        valID = loginChecker(provID)
        if valID != 3:
            print("Invalid Provider ID Format. Returning.")
            return -1
        userData = DB.get_member(provID)
        if userData == "None":
            print("Provider does not exist. Returning.")
            return -1
        print(userData)
        name = input("Enter Provider Name: ")
        street = input("Enter Street: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip = input("Enter Zip: ")
        if not nameChecker(name) == 3:
            print("Invalid Provider Name. Keeping old Provider Name.")
            name = userData[1]
        if not rangeChecker(zip, 10000, 99999) == 3:
            print("Invalid Zip. Keeping old Zip.")
            zip = userData[5]
        DB.update_provider(provID, name, street, city, state, zip)
        return 1

    @staticmethod
    def editService():
        servID = input("ID of Service being edited: ")
        valID = serviceChecker(servID)
        if valID != 3:
            print("Invalid Service ID Format. Returning.")
            return -1
        serviceData = DB.get_service(servID)
        if serviceData == "None":
            print("Service does not exist. Returning.")
            return -1
        print(serviceData)
        name = input("Enter Service Name: ")
        fee = input("Enter Service Fee: ")
        if not nameChecker(name) == 3:
            print("Invalid Service Name. Keeping old Service Name.")
            name = serviceData[1]
        if not rangeChecker(fee, 0, 999):
            print("Invalid Service Fee. Keeping old Service Fee.")
            fee = serviceData[2]
        DB.update_service(servID, name, fee)
        return 1
