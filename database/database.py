# CS 300 - Group (#4) Project: ChocAn [Section: Database] - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang

# Connect to database that is stored in path. This will be used to read/write our data.

import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__)) + "/chocan.sqlite";

class Database:

    @staticmethod
    def createdb():
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Provider")
        cur.execute("DROP TABLE IF EXISTS Member")
        cur.execute("DROP TABLE IF EXISTS Service")
        cur.execute("CREATE TABLE Service (Service_ID INTEGER PRIMARY KEY, Name TEXT, Fee INTEGER)")
        cur.execute("CREATE TABLE Provider (Provider_ID INTEGER PRIMARY KEY, Name TEXT, Street TEXT, City TEXT, "
                    "State TEXT, Zip INTEGER, Phone INTEGER, Fax INTEGER, Email TEXT, "
                    "Service_ID INTEGER, FOREIGN KEY(Service_ID) REFERENCES Service(Service_ID))")
        cur.execute(
            "CREATE TABLE Member (Member_ID INTEGER PRIMARY KEY, Name TEXT, Street TEXT, City TEXT, State TEXT, "
            "Zip INTEGER, Phone INTEGER, Fax INTEGER, Email TEXT, Service_ID INTEGER, "
            "FOREIGN KEY(Service_ID) REFERENCES Service(Service_ID))")
        con.commit()
        con.close()

    @staticmethod
    def add_provider(name, street, city, state, zip, phone, fax, email, service_id):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("INSERT INTO provider (name, street, city, state, zip, phone, fax, email, service_id) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (name, street, city, state, zip, phone, fax, email, service_id))
        con.commit()
        con.close()

    @staticmethod
    def add_member(name, street, city, state, zip, phone, fax, email, service_id):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("INSERT INTO member (name, street, city, state, zip, phone, fax, email, service_id) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (name, street, city, state, zip, phone, fax, email, service_id))
        con.commit()
        con.close()

    @staticmethod
    def add_service(name, fee):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("INSERT INTO service (name, fee) VALUES (?, ?)", (name, fee))
        con.commit()
        con.close()

    @staticmethod
    def get_provider(provider_id):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM provider WHERE provider_id = ?", (provider_id,))
        provider = cur.fetchone()
        con.close()
        return provider

    @staticmethod
    def get_member(member_id):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM member WHERE member_id = ?", (member_id,))
        member = cur.fetchone()
        con.close()
        return member

    @staticmethod
    def get_provider_by_name(name):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM provider WHERE name = ?", (name,))
        provider = cur.fetchone()
        con.close()
        return provider

    @staticmethod
    def get_member_by_name(name):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM member WHERE name = ?", (name,))
        member = cur.fetchone()
        con.close()
        return member

    @staticmethod
    def get_service(service_id):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM service WHERE service_id = ?", (service_id,))
        service = cur.fetchone()
        con.close()
        return service

    @staticmethod
    def get_providers():
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM provider")
        providers = cur.fetchall()
        con.close()
        return providers

    @staticmethod
    def get_members():
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM member")
        members = cur.fetchall()
        con.close()
        return members

    @staticmethod
    def get_services():
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM service")
        services = cur.fetchall()
        con.close()
        return services

    @staticmethod
    def get_service_by_name(name):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM service WHERE name = ?", (name,))
        service = cur.fetchone()
        con.close()
        return service

    @staticmethod
    def get_services_by_name(name):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM service WHERE name = ?", (name,))
        service = cur.fetchall()
        con.close()
        return service

    @staticmethod
    def delete_member(member_id):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("DELETE FROM member WHERE member_id = ?", (member_id,))
        con.commit()
        con.close()

    @staticmethod
    def delete_provider(provider_id):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("DELETE FROM provider WHERE provider_id = ?", (provider_id,))
        con.commit()
        con.close()

    @staticmethod
    def delete_service(service_id):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("DELETE FROM service WHERE service_id = ?", (service_id,))
        con.commit()
        con.close()

    @staticmethod
    def update_member(member_id, name, street, city, state, zip, phone, fax, email, service_id):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("UPDATE member SET name = ?, street = ?, city = ?, state = ?, zip = ?, phone = ?, fax = ?, "
                    "email = ?, service_id = ? WHERE member_id = ?",
                    (name, street, city, state, zip, phone, fax, email, service_id, member_id))
        con.commit()
        con.close()

    @staticmethod
    def update_provider(provider_id, name, street, city, state, zip, phone, fax, email, service_id):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("UPDATE provider SET name = ?, street = ?, city = ?, state = ?, zip = ?, phone = ?, fax = ?, "
                    "email = ?, service_id = ? WHERE provider_id = ?",
                    (name, street, city, state, zip, phone, fax, email, service_id, provider_id))
        con.commit()
        con.close()

    @staticmethod
    def update_service(service_id, name, fee):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("UPDATE service SET name = ?, fee = ? WHERE service_id = ?", (name, fee, service_id))
        con.commit()
        con.close()
