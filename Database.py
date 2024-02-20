# Michael Fleagle
# Date: 18-Nov-2020
# Final Project, Database.py

'''
This file handles the sql connector and databse actions.
'''

# Import mysql.connector
import mysql.connector



#add user to logins, create user acct table
def addUser(username, password):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
        
    #sql formula to instert
    sqlForm = "INSERT INTO logins (username, password) VALUES (%s, %s)"
        
    #create tuple for user and pass
    log = (username, password)
        
    #execute
    myCursor.execute(sqlForm, log)
    
    #sql formula to create accts table for user
    sqlForm2 = "CREATE TABLE " + username + "accts (title VARCHAR(255), username VARCHAR(255), password VARCHAR(255))"
    
    myCursor.execute(sqlForm2)
    
    #commit to database
    myDB.commit()
      
    
#delete user from logins, delete user accts table
def deleteUser(user, passwd):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    #sql form to delete
    sqlForm = "DELETE FROM logins WHERE password =%s"
    
    password = (passwd,)
    
    #execute
    myCursor.execute(sqlForm, password)
    
    #commit to database
    myDB.commit()
    
    #sql form to delete user accts table
    sqlForm2 = "DROP TABLE IF EXISTS " + user + "accts"
    
    #execute sql2
    myCursor.execute(sqlForm2)
    
    #commit to database
    myDB.commit()


#get password from login table
def getPassword(username):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    #sql form to get username from login table
    sqlForm = "SELECT * FROM logins WHERE username = %s"
    
    user = (username,)
    
    #execute
    myCursor.execute(sqlForm, user)
    
    loginPass = myCursor.fetchall()
    
    #commit to database
    myDB.commit()
    
    return loginPass
    

#add title, username, and password to user table
def addAccount(user, title, username, password):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    #sql form to insert
    sqlForm = "INSERT INTO "+ user + "accts (title, username, password) VALUES (%s, %s, %s)"
    
    acct = (title, username, password)
    
    #execute
    myCursor.execute(sqlForm, acct)
    
    #commit to database
    myDB.commit()
    
    
#delete title, username, and password from user table
def deleteAccount(user, title, username, password):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    # accts = findTitle(user, title)  
    
    #combine inputs
    # delete_accts = "(" + title + ", " + username + ", " + password + ")"

    #sql form to delete
    sqlForm2 = "DELETE FROM " + user + "accts WHERE (title, username, password) IN ((%s, %s, %s))"
    
    acct = (title, username, password)
    
    #execute
    myCursor.execute(sqlForm2, acct)
           
    #commit to database
    myDB.commit()
    
    
#change username in user table
def changeUsername(user, title, username, password, newUsername):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    #sql form to change username in user table
    sqlForm = "UPDATE " + user + "accts SET username =%s WHERE (title, username, password) IN ((%s, %s, %s))"
    
    name = (newUsername, title, username, password)
    
    #execute
    myCursor.execute(sqlForm, name)
    
    #commit to database
    myDB.commit()
    
    
#change password
def changePassword(user, title, username, password, newPassword):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    #sql form to change password in user table
    sqlForm = "UPDATE " + user + "accts SET password =%s WHERE (title, username, password) IN ((%s, %s, %s))"
    
    newInfo = (newPassword, title, username, password)
    
    #execute
    myCursor.execute(sqlForm, newInfo)
    
    #commit to database
    myDB.commit()
    
    
#get user table
def getUserTable(username):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    #sql form to get full user table
    sqlForm = "SELECT * FROM " + username + "accts"
    
    #execute
    myCursor.execute(sqlForm)
    
    #get the table inputs
    userAccounts = myCursor.fetchall()
    
    #return userAccounts
    return userAccounts


#get user table titles
def getUserTitles(username):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    #sql form to get titles column
    sqlForm = "SELECT title FROM " + username + "accts"
    
    #execute
    myCursor.execute(sqlForm)
    
    #get the inputs
    titlesAccts = myCursor.fetchall()
    
    title = []
    
    for titles in titlesAccts:
        title += titles
                
    #return title column
    return title


#get user table usernames
def getUserUsernames(username):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    #sql form to get usernames column
    sqlForm = "SELECT username FROM " + username + "accts"
    
    #execute
    myCursor.execute(sqlForm)
    
    #get usernames
    userAcctNames = myCursor.fetchall()
    
    userNames = []
    
    for names in userAcctNames:
        userNames += names
        
    #return username column
    return userNames


#get user table passwords 
def getUserPasswords(username):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    #sql form to get passwords column
    sqlForm = "SELECT password FROM " + username + "accts"
    
    #execute
    myCursor.execute(sqlForm)
    
    #get passwords
    userPasswds = myCursor.fetchall()
    
    userPasses = []
    
    for passes in userPasswds:
        userPasses += passes
    
    #return passwords column
    return userPasses
    

#search in table based on title
def findAcct(user, title, username, password):
    
    myDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "CS112FinalProject!",
        database = "passwordmanager"
    )
    
    #create cursor to navigate sql
    myCursor = myDB.cursor()
    
    #sql form to find based on title
    sqlForm = "SELECT * FROM michaelaccts WHERE (title, username, password) IN ((%s, %s, %s))"
    
    name = (title, username, password)
    
    #execute
    myCursor.execute(sqlForm, name)
    
    #fetch from title  
    accts = myCursor.fetchall()
    
    return accts
    

    


