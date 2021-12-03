# testfile seems like a great file for tests

import unittest
import contextlib
import io

from database.database import Database as DB
from comm.comm import newMemberReport, newProviderReport, newEFTReport, newSummaryReport
from interface.Menus import displayMenu
from interface.forms import Forms
from security.sec import isValidSelection

# redirecting standard input to run functions with forced user input
class redirect_stdin(contextlib._RedirectStream):
    _stream = "stdin"

class TestChocAn(unittest.TestCase):


    # User Interface Test
    # 	The goal of the User Interface Test is to test the interface as a provider. The functionality that the provider
    # 	is
    # 	allowed consists of entering information of a new member or existing member, requesting services, etc.
    # 	This will be testing the integration of the interface and the database. The data entered by the provider should
    # 	be correct and stored in the correct database. The data requested by the provider should be the correct data
    # 	pulled by the  database
    #

    # 5.1.1 New Member Subtest
    # 	The New Member subtest will test the user creation process by using the user interface to create a new member.
    # 	The New Member test tries to create two new members:
    #       Invalid Member:
    #           An attempt is made to create a user with invalid information. This test passes if the user interface
    #           displays the correct error message identifying the invalid information.
    #       Valid Member:
    #           An attempt is made to create a user by providing valid user information. This test passes if the user
    #           interface displays the correct success message stating that the user has been added to the user
    #           directory.
    #
    def test_add_member_valid(self):
        member_info = "Unit Test\n000 Unit St\nUnit City\nOR\n90217\n0"

        with redirect_stdin(io.StringIO(member_info)):
            result = Forms.addMemberForm()

        if result != 0:
            member = DB.get_member_by_name("Unit Test")
            # clean up the member (this could fail, deletion test occurs later)
            if str(member) != "None":
                DB.delete_member(member[0])

        self.assertNotEqual(0, result, "Unable to add valid member")

    # this one will of course fail until somebody writes a validation function I can use
    # instead of using the database functions directly
    def test_add_member_invalid(self):
        member_info = "100\nstring\n100\nstring\n100\nstring"

        with redirect_stdin(io.StringIO(member_info)):
            result = Forms.addMemberForm()

        self.assertEqual(0, result, "Able to add Invalid Member")

    # 5.1.2 Member Lookup Subtest
    # 	The Member Lookup subtest will test the member lookup function of the member directory by using the user
    # 	interface to search for members. The Member Lookup subtest tries to look up two types of patients:
    #       Non-existing Patient:
    #           An attempt is made to look up a patient who does not exist in the member directory. This test passes
    #           if the user interface displays the correct error message stating that the patient was not found
    #       Existing Patient: An attempt is made to look up a patient who is known to exist in the member directory.
    #       This test passes if the user interface displays the correct patient information for the user.
    #
    def test_member_lookup_valid(self):
        valid_id = 400000001
        member = DB.get_member(valid_id)
        self.assertFalse(str(member) == "None", "Valid member not found")

    def test_member_lookup_invalid(self):
        invalid_id = 1111111111
        member = DB.get_member(invalid_id)
        print(member)
        self.assertTrue(str(member) == "None", "Invalid member found")

    # 5.1.3 Provider Lookup Subtest
    # 	The Provider Lookup subtest will test the provider lookup function of the provider directory by using the user
    # 	interface to search for providers. The Provider Lookup subtest tries to look up two types of providers:
    #       Non-existing Provider:
    #           An attempt is made to look up a user who does not exist in the provider directory.
    #           This test passes if the user interface displays the correct error message stating that the user was not
    #           found.
    #       Existing Provider:
    #           An attempt is made to look up a user who is known to exist in the provider directory.
    #           This test passes if the user interface displays the correct provider information for the user.
    #
    def test_provider_lookup_valid(self):
        valid_id = 200000002
        provider = DB.get_provider(valid_id)
        self.assertNotEqual(str(provider), "None", "Valid provider not found")

    def test_provider_lookup_invalid(self):
        invalid_id = 123456789
        provider = DB.get_provider(invalid_id)
        self.assertEqual(str(provider), "None", "Invalid provider found")

    # 5.1.4 Service Lookup Subtest
    # 	The Service Lookup subtest will test the service lookup function of the service directory by using the user
    # 	interface to lookup service codes. The Service Lookup subtest tries to look up two types of service:
    #       Non-existing Service:
    #           An attempt is made to look up a service code that does not exist in the service directory.
    #           This test passes if the user interface displays the correct error message stating that the service
    #           code was not found.
    #       Existing Service:
    #           An attempt is made to look up a service code that is known to exist in the service directory. This test
    #           passes if the user interface displays the correct service information for the service code which was
    #           provided.
    #
    def test_service_lookup_exist(self):
        valid_id = 100001
        service = DB.get_service(valid_id)
        self.assertNotEqual(str(service), "None", "Valid provider not found")

    def test_service_lookup_notexist(self):
        invalid_id = 666666
        service = DB.get_service(invalid_id)
        self.assertEqual(str(service), "None", "Invalid provider found")

    # Report Generation Test The purpose of the Report Generation test suite is to test the report generation for
    # third-party software. The report generation is requested weekly and contains specific information. This will be
    # testing the integration of the database with the code that will generate a report and save it to disk.
    #
    # 5.2.1 Member Report Subtest The Member Report subtest will test the report generation abilities of the software
    # by generating a member report. After issuing a request for the report to be generated, the subtest will then
    # inspect the report to determine its validity. This test passes if the following conditions are met: The report
    # file exists. The report file is not empty. The report file is formatted appropriately.
    #
    #
    def test_member_report(self):

        member_id = "400000004"
        member_name = "Latifah Neal"


        f = io.StringIO()
        with contextlib.redirect_stdout(f), redirect_stdin(io.StringIO(member_id)):
            newMemberReport()
        output = f.getvalue()
        #print(output)

        self.assertRegex(output, member_name, "Member Report: Member Not Found")

    # 5.2.2 Provider Report Subtest
    # 	The Provider Report subtest will test the report generation abilities of the software by generating a provider
    # 	report. After issuing a request for the report to be generated, the subtest will then inspect the report to
    # 	determine its validity. This test passes if the following conditions are met:
    #       The report file exists.
    #       The report file is not empty.
    #       The report file is formatted appropriately.
    #
    def test_provider_report(self):
        provider_id = "100000001"
        provider_name = "Manager Bob"


        f = io.StringIO()
        with contextlib.redirect_stdout(f), redirect_stdin(io.StringIO(provider_id)):
            newProviderReport()
        output = f.getvalue()
        #print(output)

        self.assertRegex(output, provider_name, "Provider Report: Provider Not Found")

    # 5.2.3 Electronic Funds Transfer (EFT) Report Subtest The Electronic Funds Transfer Report subtest will test the
    # report generation abilities of the software by generating an EFT report. After issuing a request for the report
    # to be generated, the subtest will then inspect the report to determine its validity. This test passes if the
    # following conditions are met: The report file exists. The report file is not empty. The report file is
    # formatted appropriately.
    #
    def test_eft_report(self):
        manager_id = "100000001"
        expected_output = "Provider Name: Dr. Sam"


        f = io.StringIO()
        with contextlib.redirect_stdout(f), redirect_stdin(io.StringIO(manager_id)):
            newEFTReport()
        output = f.getvalue()
        #print(output)


        self.assertRegex(output, expected_output, "EFT report did not match expected output.")

    # 5.2.4 Summary Report Subtest The Summary Report subtest will test the report generation abilities of the
    # software by generating a summary report. After issuing a request for the report to be generated, the subtest
    # will then inspect the report to determine its validity. This test passes if the following conditions are met:
    # The report file exists. The report file is not empty. The report file is formatted appropriately.
    #
    #
    def test_summary_report(self):
        manager_id = "100000001"
        expected_output = "Provider Name: Dr. Sam"


        f = io.StringIO()
        with contextlib.redirect_stdout(f), redirect_stdin(io.StringIO(manager_id)):
            newSummaryReport()
        output = f.getvalue()
        #print(output)



        self.assertRegex(output, expected_output, "Summary report did not match expected output.")

    # Manager Interface Test The goal of the Manager Interface Test is to test the interface as a manager trying to
    # access specific information from the database that may be protected. This specific data may be sensitive,
    # thus should be safely stored and not allow access to unauthorized users.
    #
    # The Manager Interface test will confirm that the privileged manager-level functions are only accessible by
    # authorized users who have been granted the appropriate permissions. The Manager Interface Test will perform two
    # separate checks: Unauthorized User: The test program will log in to the system using the credentials of a valid
    # user who has not been granted manager-level permissions. The program will then attempt to run manager-level
    # functions. This test passes if the attempted operations fail or are otherwise shown to be inaccessible to the
    # unauthorized user. Authorized User: The test program will log in to the system using the credentials of a valid
    # user who has been granted manager-level permissions. The program will then attempt to run manager-level
    # functions. This test passes if the attempted operations are available to the program and if the operations
    # succeed.
    #
    def test_manager_interface_valid(self):
        valid_id = ("100000001")
        expected_output = "7 - Generate Reports Menu"

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            displayMenu(valid_id)
        output = f.getvalue()
        print(output)

        self.assertRegex(output, expected_output, "Report generation unavailable for manager")

    def test_manager_interface_invalid(self):
        invalid_id = ("200000001")
        expected_output = "6 - Interactive Mode Menu \(IAM\)8 - Log Out"

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            displayMenu(invalid_id)
        output = f.getvalue()
        output = output.replace("\r", "").replace("\n\t", "")
        print(output)



        self.assertRegex(output, expected_output, "Report generation available for non-manager")

    # Menu Integration Test The purpose of the Menu Integration Test is to test the menu interface with the
    # integration of the database and weekly report generation. This will make sure that every choice in the main
    # menu does what it should and allows the user to have an easy menu interface that flows with what they request.
    # The menu interface should connect to the database for accessing data. The menu interface should connect with
    # the report generator that will generate and display a weekly report with the correct data requested in the
    # report generation component. The Menu Integration Test will be comprised of the following subtests:
    #
    # 5.4.1 Menu Selection Subtest
    #   The Menu Selection subtest will test each valid menu selection. The subtest will also test several invalid menu
    #   options. The subtest passes if each valid menu selection results in the correct menu being displayed to the user
    #   and if each invalid menu selection results in an appropriate error message confirming that the invalid input has
    #   been handled correctly.
    #
    def test_menu_selection_valid(self):
        select = isValidSelection("5")
        self.assertEqual(3, select, "Valid menu selection not allowed.")

    def test_menu_selection_invalid(self):
        select = isValidSelection("100")
        self.assertNotEqual(3, select, "Invalid menu selection allowed.")


    # 5.4.2 Form Manager Subtest The Form Manager subtest will test each form that is managed by the software. These
    # forms will connect with the database. This subtest will fill each form out with both valid and invalid data.
    # The subtest passes only if each form correctly accepts the valid data and displays an appropriate response.
    # Furthermore, the subtest passes only if each form correctly recognizes the invalid data and displays an error
    # message appropriately.
    #
    def test_form_validation_valid(self):
        input = "Unit Test\nStreet Address\nCity\nST\n30598\n"

        with redirect_stdin(io.StringIO(input)):
            result = Forms.addProviderForm()

        self.assertNotEqual(result, 0, "Valid Form Rejected")


    def test_form_validation_invalid(self):
        input = "UnitTest\nStreet Address\nCity\nST\n305989398\n"

        with redirect_stdin(io.StringIO(input)):
            result = Forms.addProviderForm()

        self.assertEqual(result, 0, "Invalid Form Accepted")

if __name__ == '__main__':
    unittest.main()
