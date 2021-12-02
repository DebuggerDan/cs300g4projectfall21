from unittest import TestCase
from database import Database


class TestDatabase(TestCase):
    # Removing the database creation test so we can populate with data
    #def test_createdb(self):
    #    Database.createdb()

    def test_add_billing(self):
        Database.add_billing("A", "B", "C", "D", "E", "F")

    def test_get_billing(self):
        Database.get_provider_billing("200000001")

    def test_add_provider(self):
        Database.add_provider("1", "B", "C", "D", "E")
        Database.add_provider("2", "BB", "CC", "DD", "EE")

    def test_add_member(self):
        Database.add_member("1", "K", "L", "M", "N", 0)
        Database.add_member("2", "KK", "LL", "MM", "NN", 1)

    def test_add_service(self):
        Database.add_service("1", "T")
        Database.add_service("2", "TT")

    def test_get_provider(self):
        Database.get_provider("1")

    def test_get_member(self):
        Database.get_member("1")

    def test_get_provider_by_name(self):
        Database.get_provider_by_name("A")

    def test_get_member_by_name(self):
        Database.get_member_by_name("J")

    def test_get_service(self):
        Database.get_service("1")

    def test_get_providers(self):
        Database.get_providers()

    def test_get_members(self):
        Database.get_members()

    def test_get_services(self):
        Database.get_services()

    def test_get_service_by_name(self):
        Database.get_service_by_name("S")

    def test_delete_member(self):
        Database.delete_member("1")

    def test_delete_provider(self):
        Database.delete_provider("1")

    def test_delete_service(self):
        Database.delete_service("1")

    def test_update_member(self):
        Database.update_member("2", "JJJ", "KKK", "LLL", "MMM", "NNN", 0)

    def test_update_provider(self):
        Database.update_provider("2", "AAA", "BBB", "CCC", "DDD", "EEE")

    def test_update_service(self):
        Database.update_service("2", "SSS", "TTT")
