#CS300 Report Dispaying 

#Weekly Member Services Reports
from database.database import Database as db


def testMember():
    IDnum = 0
    print("Please enter the member's 9-digit ID: ")
    input(IDnum)
    memberReport(IDnum)

def memberReport(memberID):
    tempdb = db
    memberInfo = db.get_member(memberID)
    print(memberInfo)
    
"""
comm comments - all functions assume user is "logged in" already
make sure the "logged in" person meets requirements

member report function - prints report - manager only
    take member id
    displays information for that member
    displays services from this week for member
    if desired, display older services
provider report function - prints report - manager only
    same as above, but this time for providers
summary report function - prints report - manager only
    lists all members who have received services in past week
    lists all providers who have rendered services in past week
    lists (if desired) details on rendered services
    display total price of services rendered
weekly summary function - prints report - manager and provider access
    same as above, but only iterates once a week.
    note: if in middle of week, do not update
"""
