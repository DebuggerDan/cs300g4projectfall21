# CS 300 - Group (#4) Project: ChocAn [Section: Database] - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang

# Connect to database that is stored in path. This will be used to read/write our data.

import os
import random
import sqlite3
from datetime import datetime

path = os.path.dirname(os.path.realpath(__file__)) + "/chocan.sqlite"


class Database:

    @staticmethod
    def createdb():
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Provider")

        cur.execute("DROP TABLE IF EXISTS Member")

        cur.execute("DROP TABLE IF EXISTS Service")

        cur.execute("DROP TABLE IF EXISTS Billing")

        cur.execute("CREATE TABLE Service (Service_ID INTEGER PRIMARY KEY, Name VARCHAR(25), Fee DECIMAL(3,2))")

        cur.execute("CREATE TABLE Provider (Provider_ID INTEGER PRIMARY KEY, Name VARCHAR(25), "
                    "Street VARCHAR(25), City TEXT, State VARCHAR(2), Zip INTEGER)")

        cur.execute("CREATE TABLE Member (Member_ID INTEGER PRIMARY KEY, Name VARCHAR(25), Street VARCHAR(25), "
                    "City TEXT, State VARCHAR(2), Zip INTEGER, Is_Active INTEGER)")

        cur.execute("CREATE TABLE Billing (Member_ID INTEGER PRIMARY KEY, Provider INTEGER, Service_Date DATE, "
                    "Billing_Date DATETIME, Service INTEGER, Comments VARCHAR(100))")

        con.commit()
        con.close()

    @staticmethod
    def fixBilling():
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS Billing")
        cur.execute("CREATE TABLE Billing (Key INTEGER PRIMARY KEY, Member_ID INTEGER, Provider INTEGER, "
                    "Service_Date DATE, Billing_Date DATETIME, Service INTEGER, Comments VARCHAR(100))")

        con.commit()
        con.close()

    @staticmethod
    def fixService():
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS Service")
        cur.execute("CREATE TABLE Service (Service_ID INTEGER PRIMARY KEY, Name VARCHAR(25), Fee DECIMAL(3,2))")

        con.commit()
        con.close()

    @staticmethod
    def add_billing(member_id, provider_id, service_date, billing_date, service_id, comments):
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("INSERT INTO billing (Member_ID, Provider, Service_date, Billing_Date, Service, comments) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    (member_id, provider_id, service_date, billing_date, service_id, comments))
        con.commit()
        con.close()

    # shove some bills in the database
    @staticmethod
    def generate_billing():
        now = datetime.now()
        service_date = now.strftime("%Y-%m-%d")
        billing_date = now.strftime("%Y-%m-%d %H:%M:%S")

        for x in range(12):  # currently there are 12 members
            member_id = 400000001 + x
            for y in range(4):  # give each member four bills
                provider_id = 200000001 + random.randrange(17)  # currently there are 17 providers
                service_id = 100001 + random.randrange(10)  # currently there are 10 named services
                Database.add_billing(member_id, provider_id, service_date, billing_date, service_id, "comments")

    @staticmethod
    def get_provider_billing(provider_id):
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("SELECT * FROM billing WHERE provider = ?", (provider_id,))

        billing = cur.fetchall()
        con.close()

        return billing

    @staticmethod
    def get_member_billing(member_id):
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("SELECT * FROM billing WHERE Member_ID = ?", (member_id,))

        billing = cur.fetchall()
        con.close()

        return billing

    @staticmethod
    def add_provider(name, street, city, state, zip):
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("INSERT INTO provider (name, street, city, state, zip) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (name, street, city, state, zip))

        con.commit()
        con.close()

    @staticmethod
    def add_member(name, street, city, state, zip, is_active):
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("INSERT INTO member (name, street, city, state, zip, is_active) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    (name, street, city, state, zip, is_active))

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

        cur.execute("SELECT * FROM service ORDER BY name ASC") #required to be alphabetical

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
    def update_member(member_id, name, street, city, state, zip, is_active):
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("UPDATE member SET name = ?, street = ?, city = ?, state = ?, "
                    "zip = ? , is_active = ? WHERE member_id = ?",
                    (name, street, city, state, zip, is_active, member_id))

        con.commit()
        con.close()

    @staticmethod
    def update_provider(provider_id, name, street, city, state, zip):
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("UPDATE provider SET name = ?, street = ?, city = ?, state = ?, zip = ? WHERE provider_id = ?",
                    (name, street, city, state, zip, provider_id))

        con.commit()
        con.close()

    @staticmethod
    def update_service(service_id, name, fee):
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("UPDATE service SET name = ?, fee = ? WHERE service_id = ?", (name, fee, service_id))

        con.commit()
        con.close()
