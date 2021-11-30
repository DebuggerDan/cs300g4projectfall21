#testfile seems like a great file for tests

import unittest
from database.database import Database as DB

class TestSum(unittest.TestCase):

    # User Interface Test
    # 	The goal of the User Interface Test is to test the interface as a provider. The functionality that the provider is
    # 	allowed consists of entering information of a new member or existing member, requesting services, etc. This will be
    # 	testing the integration of the interface and the database. The data entered by the provider should be correct and
    # 	stored in the correct database. The data requested by the provider should be the correct data pulled by the database
    #


    # 5.1.1 New Member Subtest
    # 	The New Member subtest will test the user creation process by using the user interface to create a new member. The
    # 	New Member test tries to create two new members:
    #       Invalid Member:
    #           An attempt is made to create a user with invalid information. This test passes if the user interface
    #           displays the correct error message identifying the invalid information.
    #       Valid Member:
    #           An attempt is made to create a user by providing valid user information. This test passes if the user
    #           interface displays the correct success message stating that the user has been added to the user directory.
    #
    def test_add_member_valid(self):



    # 5.1.2 Member Lookup Subtest
    # 	The Member Lookup subtest will test the member lookup function of the member directory by using the user interface
    # 	to search for members. The Member Lookup subtest tries to look up two types of patients:
    #       Non-existing Patient:
    #           An attempt is made to look up a patient who does not exist in the member directory. This test passes if the
    #           user interface displays the correct error message stating that the patient was not found
    #       Existing Patient: An attempt is made to look up a patient who is known to exist in the member directory. This
    #           test passes if the user interface displays the correct patient information for the user.
    #
    def test_member_lookup_valid(self):
        valid_id = 93
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
    #           An attempt is made to look up a user who does not exist in the provider directory. This test passes if the
    #           user interface displays the correct error message stating that the user was not found.
    #       Existing Provider: An attempt is made to look up a user who is known to exist in the provider directory. This
    #           test passes if the user interface displays the correct provider information for the user.
    #
    def test_provider_lookup_valid(self):
        valid_id = 300000012
        provider = DB.get_provider(valid_id)
        self.assertNotEqual(str(provider), "None", "Valid provider not found")

    def test_provider_lookup_invalid(self):
        invalid_id = 123456789;
        provider = DB.get_provider(invalid_id);
        self.assertEqual(str(provider), "None", "Invalid provider found")

    # 5.1.4 Service Lookup Subtest
    # 	The Service Lookup subtest will test the service lookup function of the service directory by using the user
    # 	interface to lookup service codes. The Service Lookup subtest tries to look up two types of service:
    #       Non-existing Service:
    #           An attempt is made to look up a service code that does not exist in the service directory. This test passes
    #           if the user interface displays the correct error message stating that the service code was not found.
    #       Existing Service:
    #           An attempt is made to look up a service code that is known to exist in the service directory. This test
    #           passes if the user interface displays the correct service information for the service code which was
    #           provided.
    #
    def test_service_lookup_exist(self):
        valid_id = 148
        service = DB.get_service(valid_id);
        self.assertNotEqual(str(service), "None", "Valid provider not found")

    def test_service_lookup_notexist(self):
        invalid_id = 666666;
        service = DB.get_service(invalid_id);
        self.assertEqual(str(service), "None", "Invalid provider found")

    # Report Generation Test
    # 	The purpose of the Report Generation test suite is to test the report generation for third-party software. The
    # 	report generation is requested weekly and contains specific information. This will be testing the integration of the
    # 	database with the code that will generate a report and save it to disk.
    #
    # 5.2.1 Member Report Subtest
    # 	The Member Report subtest will test the report generation abilities of the software by generating a member report.
    # 	After issuing a request for the report to be generated, the subtest will then inspect the report to determine its
    # 	validity. This test passes if the following conditions are met:
    #       The report file exists.
    #       The report file is not empty.
    #       The report file is formatted appropriately.
    #
    #
    # 5.2.2 Provider Report Subtest
    # 	The Provider Report subtest will test the report generation abilities of the software by generating a provider
    # 	report. After issuing a request for the report to be generated, the subtest will then inspect the report to
    # 	determine its validity. This test passes if the following conditions are met:
    #       The report file exists.
    #       The report file is not empty.
    #       The report file is formatted appropriately.
    #
    # 5.2.3 Electronic Funds Transfer (EFT) Report Subtest
    # 	The Electronic Funds Transfer Report subtest will test the report generation abilities of the software by generating
    # 	an EFT report. After issuing a request for the report to be generated, the subtest will then inspect the report to
    # 	determine its validity. This test passes if the following conditions are met:
    #       The report file exists.
    #       The report file is not empty.
    #       The report file is formatted appropriately.
    #
    # 5.2.4 Summary Report Subtest
    # 	The Summary Report subtest will test the report generation abilities of the software by generating a summary report.
    # 	After issuing a request for the report to be generated, the subtest will then inspect the report to determine its
    # 	validity. This test passes if the following conditions are met:
    #       The report file exists.
    #       The report file is not empty.
    #       The report file is formatted appropriately.
    #
    #
    # Manager Interface Test
    # 	The goal of the Manager Interface Test is to test the interface as a manager trying to access specific information
    # 	from the database that may be protected. This specific data may be sensitive, thus should be safely stored and not
    # 	allow access to unauthorized users.
    #
    # The Manager Interface test will confirm that the privileged manager-level functions are only accessible by authorized
    # users who have been granted the appropriate permissions. The Manager Interface Test will perform two separate checks:
    #   Unauthorized User:
    #       The test program will log in to the system using the credentials of a valid user who has not been granted
    #       manager-level permissions. The program will then attempt to run manager-level functions. This test passes if the
    #       attempted operations fail or are otherwise shown to be inaccessible to the unauthorized user.
    #   Authorized User:
    #       The test program will log in to the system using the credentials of a valid user who has been granted
    #       manager-level permissions. The program will then attempt to run manager-level functions. This test passes if the
    #       attempted operations are available to the program and if the operations succeed.
    #
    # Menu Integration Test
    #   The purpose of the Menu Integration Test is to test the menu interface with the integration of the database and
    #   weekly report generation. This will make sure that every choice in the main menu does what it should and allows the
    #   user to have an easy menu interface that flows with what they request. The menu interface should connect to the
    #   database for accessing data. The menu interface should connect with the report generator that will generate and
    #   display a weekly report with the correct data requested in the report generation component. The Menu Integration
    #   Test will be comprised of the following subtests:
    #
    # 5.4.1 Menu Selection Subtest
    #   The Menu Selection subtest will test each valid menu selection. The subtest will also test several invalid menu
    #   options. The subtest passes if each valid menu selection results in the correct menu being displayed to the user
    #   and if each invalid menu selection results in an appropriate error message confirming that the invalid input has
    #   been handled correctly.
    #
    # 5.4.2 Form Manager Subtest
    #   The Form Manager subtest will test each form that is managed by the software. These forms will connect with the
    #   database. This subtest will fill each form out with both valid and invalid data. The subtest passes only if each
    #   form correctly accepts the valid data and displays an appropriate response. Furthermore, the subtest passes only if
    #   each form correctly recognizes the invalid data and displays an error message appropriately.
    #
    # 5.5	Database Functionality Tests
    # 	The purpose of the Database Functionality Tests is to ensure that the proper database structure has been created,
    # 	that the helper functions are able to read/retrieve/edit/delete data within the database, and that any extra values
    # 	passed to the functions are either truncated or return an error message.
    #
    # 5.5.1 Database Creation Subtest
    # 	The Database Creation Subtest will test if the database currently exists if the database has data stored already,
    # 	and if no database exists, the creation of a new database with required tables added. The tests will only pass if a
    # 	database exists with the proper tables (with or without existing data in the tables), or if no database exists and
    # 	the software can create/connect to a new database and ensure proper tables and structures are created.
    #
    # 5.5.2 Database Read/Write Subtest
    # 	The Database Read/Write Subtest will test the ability to read data that is stored in the database and pass only if
    # 	valid data is found. The written test will create a new test entry, and verify that the data exists in the database
    # 	during the reading subtest. It will fail if the data cannot be found, and will pass if the data is present in the
    # 	database that matches the query. This test relies on the Database Creation Subtest to return a pass, otherwise, it
    # 	will fail if no database is found, or the tables are not present in the database.
    #
    # 5.5.3 Database Update/Delete Subtest
    # 	The Database Update/Delete Subtest will test the ability to retrieve a value from the database, alter the data,
    # 	write it back to the database, then attempt to locate and read the newly edited data. It will pass if the new data
    # 	is found, and fail if it cannot find the data within the database. The delete subtest will then search for the data
    # 	that was just edited and verified to be in the database, and remove/drop the information from the database, then
    # 	perform a search for the data within the database. It will pass if the data is not found, and will fail if the data
    # 	is found.
    #
    # 5.5.4 Database Helper Function Subtest
    # 	The Database Helper Function Subtest will test the database helper functions’ ability to take arguments passed from
    # 	the frontend/menu interface and match the values to valid entries in the database. The test will pass if all passed
    # 	values match a valid entry in the database. If the arguments are incorrect, or if there are too many arguments, the
    # 	test will fail. These tests will cover all tables in the database and their corresponding functions. If no database
    #   is found, or no matching tables found, the test will fail.



    #def test_stuff(self):
    #    self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    #def test_new_member_invalid(self):
    #    self.assertRegex("stuff_string1_stuff", "string1", "Should be 'string1'")

if __name__ == '__main__':
    unittest.main()