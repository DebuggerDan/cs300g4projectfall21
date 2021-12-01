#attempting to create basic forms for all possible user inputs
#these could all be modified to include data validation as well

class Forms:

    @staticmethod
    def testForms():
        print("\nADD MEMBER FORM\n")
        print(Forms.addMemberForm())
        print("\nADD PROVIDER FORM\n")
        print(Forms.addProviderForm())
        print("\nADD SERVICE FORM\n")
        print(Forms.addServiceForm())

        print("\nMEMBER ID FORM\n")
        print(Forms.memberIDForm())
        print("\nPROVIDER ID FORM\n")
        print(Forms.providerIDForm())
        print("\nSERVICE ID FORM\n")
        print(Forms.serviceIDForm())

        print("\nMEMBER NAME FORM\n")
        print(Forms.memberIDForm())
        print("\nPROVIDER NAME FORM\n")
        print(Forms.providerIDForm())

        print("\nMENU SELECTION FORM\n")
        print(Forms.menuSelectForm())


    #add

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
        id = input("Enter Service Name: ")
        return id

    #name forms

    @staticmethod
    def providerNameForm():
        name = input("Enter Provider Name: ")
        return name

    @staticmethod
    def memberIDForm():
        name = input("Enter Member Name: ")
        return name

    #menu form

    @staticmethod
    def menuSelectForm():
        num = input("Menu Selection: ")
        return num

