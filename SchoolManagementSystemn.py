# importing mysql.connector to use MySQL for storing data of students, teachers, etc.
import mysql.connector as a

# establishing connection with MySQL local server
con = a.connect(host="localhost", user="root", database="school")

# importing OS module for clear screen function
import os

"""
Creating a MySQL Database

 1. Download and install MySQL **/
 2. Using the MySQL Command Line Client execute the following commands(line 8 to 15):
# create database school;
# use school;
# create table student (name varchar(50), class varchar(20), roll varchar(10),
  address varchar(50), phone varchar(10));
# create table teacher (name varchar(50), post varchar(20), salary varchar(10),
  address varchar(50), phone varchar(10), acno varchar(10));
# create table cattendance (date varchar(20), class varchar(10), absent varchar(1000));
# create table tattendance (date varchar(20), absent varchar(1000));
# create table fees (name varchar(50), class varchar(20), roll varchar(10),
  month_year varchar(20), fees_rs varchar(20), date varchar(20));
# create table salary (name varchar(50), month varchar(20), paid varchar(20));

"""

# ~~~~~~~~~Function to Display ending options to the User~~~~~~~~~

def op():
    print()
    choice = input(">>> Press <enter> to exit or Press 'm' to go back to the Main Menu: ")
    if choice == "M" or "m":
        main()
    else:
        exit()

# ~~~~~~~~~Function to clear screen after every message display~~~~~~~~~

def wash():
    os.system('clear')


# ~~~~~~~~~Function to Add a Student~~~~~~~~~

def ast():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    n = input("Student Name: ")
    c = input("Class Name: ")
    r = input("Roll No: ")
    ad = input("Address: ")
    p = input("Phone: ")
    data = (n, c, r, ad, p)
    sql = 'insert into student values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Entered Successfully")
    print(">----------------------------------------------------------------------------------------------------<")
    op()

# ~~~~~~~~~Function to Remove a Student~~~~~~~~~

def rst():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    c = input("Class Name: ")
    r = input("Roll No: ")
    data = (c, r)
    sql = 'delete from student where CLASS = %s and ROLL = %s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Function to Add a Teacher~~~~~~~~~

def addt():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    n = input("Teacher Name: ")
    p = input("Post: ")
    s = input("Salary: ")
    ad = input("Address: ")
    ph = input("Phone: ")
    ac = input("Account: ")
    data = (n, p, s, ad, ph, ac)
    sql = 'insert into teacher values(%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Entered Successfully")
    print(">----------------------------------------------------------------------------------------------------<")
    op()

# ~~~~~~~~~Function  to Remove a Teacher~~~~~~~~~

def remt():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    n = input("Teacher Name: ")
    ac = input("Account: ")
    data = (n, ac)
    sql = 'delete from teacher where name = %s and acno = %s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Function to List Absent Students from different classes~~~~~~~~~

def abclass():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    d = input("Date: ")
    cl = input("Class: ")
    ab = input("Names of Absent Students: ")
    data = (d, cl, ab)
    sql = 'insert into cattendance values(%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Function to List Absent Teachers~~~~~~~~~

def abteacher():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    d = input("Date: ")
    ab = input("Names of Absent Teachers: ")
    data = (d, ab)
    sql = 'insert into tattendance values(%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Function for Submitting Fees~~~~~~~~~

def submitf():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    n = input("Student Name: ")
    c = input("Class Name: ")
    r = input("Roll No: ")
    m = input("Month and Year: ")
    f = input("Fees: ")
    d = input("Date: ")
    data = (n, c, r, m, f, d)
    sql = 'insert into fees values(%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Fees Submitted")
    print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Function to Pay Teacher's Salary~~~~~~~~~

def pays():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    n = input("Teacher Name: ")
    m = input("Month: ")
    p = input("Yes/No? ")
    data = (n, m, p)
    sql = 'insert into salary values(%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Entered Successfully")
    print(">----------------------------------------------------------------------------------------------------<")
    op()

# ~~~~~~~~~Function to Display the profile all the Students of a particular Class~~~~~~~~~

def dclass():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    cl = input("Class: ")
    data = (cl,)
    sql = "select * from student where class = %s"
    c = con.cursor()
    c.execute(sql, data)
    d = c.fetchall()
    for i in d:
        print(">-----------------------<")
        print("Name: ", i[0])
        print("Class: ", i[1])
        print("Roll No.: ", i[2])
        print("Address: ", i[3])
        print("Phone: ", i[4])
        print(">-----------------------<")
    print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Function to Display the profile of all the Teachers~~~~~~~~~

def dteacher():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    sql = "select * from teacher"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(">-----------------------<")
        print("Name: ", i[0])
        print("Post: ", i[1])
        print("Salary: ", i[2])
        print("Address: ", i[3])
        print("Phone: ", i[4])
        print("Account Number: ", i[5])
        print(">-----------------------<")
        print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Function to Check Student Fees Report~~~~~~~~~

def feesreport():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    cl = input("Class: ")
    data = (cl,)
    sql = "select * from fees where class = %s"
    c = con.cursor()
    c.execute(sql, data)
    d = c.fetchall()
    for i in d:
        print(">-----------------------<")
        print("Name: ", i[0])
        print("Class: ", i[1])
        print("Roll No.: ", i[2])
        print("Month & Year: ", i[3])
        print("Fees: ", i[4])
        print("Date: ", i[5])
        print(">-----------------------<")
    print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Function to Check if a Teacher's Salary is paid or not~~~~~~~~~

def checkteachsal():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    name = input("Teacher's Name: ")
    data = (name,)
    sql = "select * from salary where name = %s"
    c = con.cursor()
    c.execute(sql, data)
    d = c.fetchall()
    for i in d:
        print(">-----------------------<")
        print("Teacher's Name: ", i[0])
        print("Month: ", i[1])
        print("Transaction Completed? ", i[2])
        print(">-----------------------<")
    print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Function to Display all the absent students on a particular date~~~~~~~~~

def dabstud():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    date = input("Date: ")
    data = (date,)
    sql = "select * from cattendance where date = %s"
    c = con.cursor()
    c.execute(sql, data)
    d = c.fetchall()
    for i in d:
        print(">-----------------------<")
        print("Class: ", i[1])
        print("Name of Absent Students: ", i[2])
        print(">-----------------------<")
    print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Function to Display all the absent teachers on a particular date~~~~~~~~~

def dabteach():
    wash()
    print(">----------------------------------------------------------------------------------------------------<")
    date = input("Date: ")
    data = (date,)
    sql = "select * from tattendance where date = %s"
    c = con.cursor()
    c.execute(sql, data)
    d = c.fetchall()
    for i in d:
        print(">-----------------------<")
        print("Name of Absent Teachers: ", i[1])
        print(">-----------------------<")
    print(">----------------------------------------------------------------------------------------------------<")
    op()


# ~~~~~~~~~Main Function~~~~~~~~~

def main():
    wash()
    # ~~~~~~~~~~~~~~~~~~~~~~~~School Banner~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print("""
  ###        ###        ###                ###           ##############
  ###     ###            ###              ###         ###
  ###    ###              ###            ###         ###
  ###  ###                 ###          ###           ###
  #######                   ###        ###              #############
  ###  ###                   ###      ###                           ###
  ###    ###                  ###    ###                             ###
  ###      ###      ###        ###  ###      ###                   ###
  ###        ###    ###          ####        ###      ##############
    """)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print("""
+-----------------------SCHOOL MANAGEMENT SOFTWARE----------------------+
|---------------------------------Menu----------------------------------|
|                                   |                                   |
| >[1]  Add Student                 | >[2]  Remove Student              |
| >[3]  Add Teacher                 | >[4]  Remove Teacher              |
| >[5]  Class Attendance            | >[6]  Teacher Attendance          |
| >[7]  Submit Fees                 | >[8]  Pay Teacher's Salary        |
| >[9]  Display Profiles of all the | >[10] Display Teachers' Profiles  |
|       Students in a Particular    |                                   |
|       Class                       |                                   |
| >[11] Check Fee Submission        | >[12] Check if a Teacher's Salary |
|                                   |       is paid or not              |
| >[13] Display Absent Students     | >[14] Display Absent Teachers     |
| >[15] Exit                        |                                   |
+-----------------------------------------------------------------------+

                   """)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~~~~~~~~Taking the response from the user~~~~~~~~~
    choice = int(input("  >>> What would you like to do? "))
    if choice == 1:
        ast()
    elif choice == 2:
        rst()
    elif choice == 3:
        addt()
    elif choice == 4:
        remt()
    elif choice == 5:
        abclass()
    elif choice == 6:
        abteacher()
    elif choice == 7:
        submitf()
    elif choice == 8:
        pays()
    elif choice == 9:
        dclass()
    elif choice == 10:
        dteacher()
    elif choice == 11:
        feesreport()
    elif choice == 12:
        checkteachsal()
    elif choice == 13:
        dabstud()
    elif choice == 14:
        dabteach()
    elif choice == 15:
        exit()
    else:
        print("Wrong choice!")
    main()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~Executing the main function~~~~~~~~~
main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
