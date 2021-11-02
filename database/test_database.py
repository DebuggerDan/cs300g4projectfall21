from unittest import TestCase
from database import Database


class TestDatabase(TestCase):
    def test_createdb(self):
        Database.createdb()

    def test_add_provider(self):
        Database.add_provider("A", "B", "C", "D", "E", "F", "G", "H", "I")
        Database.add_provider("AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II")

    def test_add_member(self):
        Database.add_member("J", "K", "L", "M", "N", "O", "P", "Q", "R")
        Database.add_member("JJ", "KK", "LL", "MM", "NN", "OO", "PP", "QQ", "RR")

    def test_add_service(self):
        Database.add_service("S", "T")
        Database.add_service("SS", "TT")

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
        Database.update_member("2", "JJJ", "KKK", "LLL", "MMM", "NNN", "OOO", "PPP", "QQQ", "RRR")

    def test_update_provider(self):
        Database.update_provider("2", "AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III")

    def test_update_service(self):
        Database.update_service("2", "SSS", "TTT")
