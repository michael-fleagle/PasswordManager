# Michael Fleagle
# Date: 18-Nov-2020
# Final Project, Password Manager.py

"""
This project creates an easy to use/simplistic password manager featuring multiple
possible users and a basic GUI. The passwords and logins are stored in a mySQL database. 
Unfortunately, due to time constraints and complexity no password encryption 
was able to be implemented. 
 
I utilize the PyQT5 library to help handle the GUI, and mySQL 
Connector to connect to the mySQL database.

Run this file to execute the entire program

"""

# Import libraries needed: PyQt5
# Import Database.py and sys
import Database
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QLabel, QLineEdit, QGridLayout, QMessageBox,
                             QScrollArea, QFrame)
from PyQt5.QtCore import (Qt)      
    

# Class to create landing page post login
class LandingPage(QWidget):
    
    #init method
    def __init__(self, username):
        
        super().__init__()
        self.setWindowTitle("Password Manager")
        self.resize(1000, 500)
        self.username = username
        self.UiElem()
    
    #mehod to create all ui elements for LandingPage
    def UiElem(self):
        
        #create layout
        layout = QGridLayout()
        self.layout = layout
        
        user = self.username
        
        #create scrollarea layout
        scrollLayout = QGridLayout()
        
        #create scroll area
        scroll = QScrollArea()
        
        #Scroll Area Properties
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        
        #seting layout for scroll
        scroll.setLayout(scrollLayout)
        
        #create frame widget to add to the scroll area
        self.innerScroll = QFrame(scroll)
        self.innerLayout = QGridLayout()
        self.innerScroll.setLayout(self.innerLayout)
        
        #add titles header
        column1 = QLabel('<font size="15"> Titles </font>')
        self.innerLayout.addWidget(column1, 0, 0)
        
        #get titles from database
        userTitles = Database.getUserTitles(user)
        
        f = 1
        #put titles in as labels
        for titles in userTitles:
            title = QLabel(str(titles.split(",")))
            self.innerLayout.addWidget(title, f, 0)
            f+=1
            
        #add usernames header
        column2 = QLabel('<font size="15"> Usernames </font>')
        self.innerLayout.addWidget(column2, 0, 1)
        
        #get usernames from database
        userUsernames = Database.getUserUsernames(user)
        
        i = 1
        #put usernames in as labels
        for names in userUsernames:
            name = QLabel(str(names.split(",")))
            self.innerLayout.addWidget(name, i, 1)
            i+=1
        
        #add passwords header
        column3 = QLabel('<font size="15"> Passwords </font>')
        self.innerLayout.addWidget(column3, 0, 2)
        
        #put passwords in as labels
        userPasswords = Database.getUserPasswords(user)
        
        j = 1
        for passes in userPasswords:
            pas = QLabel(str(passes.split(",")))
            self.innerLayout.addWidget(pas, j, 2)
            j+=1
    
        self.dataShow()
        
        #add inerscroll to scroll
        scroll.setWidget(self.innerScroll)
        
        #add scroll to layout
        layout.addWidget(scroll, 0, 2, 15, 2)
        
        #create welcome banner
        banner = QLabel('<font size="15"> Welcome ' + user + '</font>')
        
        layout.addWidget(banner, 0, 0, 1, 2)
        
        #create title lable and input
        label1 = QLabel('<font size="8"> Title </font>')
        self.title_input = QLineEdit()
        layout.addWidget(label1, 2, 0)
        layout.addWidget(self.title_input, 2, 1)
        
        #create username label and input
        label2 = QLabel('<font size="8"> Username </font>')
        self.username_input = QLineEdit()
        layout.addWidget(label2, 3, 0)
        layout.addWidget(self.username_input, 3, 1)
        
        #create password label and input
        label3 = QLabel('<font size="8"> Password </font>')
        self.password_input = QLineEdit()
        layout.addWidget(label3, 4, 0)
        layout.addWidget(self.password_input, 4, 1)
        
        #create add account button
        button_addAcct = QPushButton('Add Account')
        layout.addWidget(button_addAcct, 5, 1, 2, 1)
        
        #insert add account button click here
        button_addAcct.clicked.connect(self.addAccount_ButtonClick)
        
        #create delete account button
        button_delAcct = QPushButton('Delete Account')
        layout.addWidget(button_delAcct, 6, 1, 3, 1)
        
        #insert delacct button click here
        button_delAcct.clicked.connect(self.deleteAccount_ButtonClick)
        
        #create label for new user or pass
        newLabel = QLabel('<font size="6"> New Username/Password </font>')
        self.newUserOrPass_input = QLineEdit()
        layout.addWidget(newLabel, 9, 0)
        layout.addWidget(self.newUserOrPass_input, 8, 1, 3, 1)
        
        #create change account username button
        button_changeUser = QPushButton('Change Account Username')
        layout.addWidget(button_changeUser, 9, 1, 4, 1)
        
        #insert changeUser button click here
        button_changeUser.clicked.connect(self.changeUsername_ButtonClick)
        
        #create change account password button
        button_changePass = QPushButton('Change Account Password')
        layout.addWidget(button_changePass, 10, 1, 5, 1)
        
        #insert changePass button click here
        button_changePass.clicked.connect(self.changePassword_ButtonClick)
        
        #create logout button
        button_logOut = QPushButton('Logout')
        layout.addWidget(button_logOut, 12, 1, 6, 1)
        
        #insert logout button click
        button_logOut.clicked.connect(self.logOut_ButtonClick)
        
        #set layout
        self.setLayout(layout)
    
    #method for button click to add account
    def addAccount_ButtonClick(self):
        
        #collect inputs
        inputTitle = self.title_input.text()
        inputUsername = self.username_input.text()
        inputPassword = self.password_input.text()
        
        #pass to add account
        Database.addAccount(self.username, inputTitle, inputUsername, inputPassword)
        
        #send back to previous page
        self.refresh()

    
    #method for button click to delete account
    def deleteAccount_ButtonClick(self):
        
        #collect inputs
        inputTitle = self.title_input.text()
        inputUsername = self.username_input.text()
        inputPassword = self.password_input.text()
        
        #check if account exists
        if self.checkAcctExist(inputTitle, inputUsername, inputPassword) == True:
            #pass to delete account
            Database.deleteAccount(self.username, inputTitle, inputUsername, inputPassword)
            
        else:
    
            self.noAccountFound()
        
        #refresh
        self.refresh()
        
    #method to check if deleted account exists
    def checkAcctExist(self, title, username, password):
        
        #get accounts matching input
        accts = Database.findAcct(self.username, title, username, password)
        
        #check for accounts to delete
        if len(accts) == 0:
           return False
        else:
            return True
        
    #method to create popup if no account found
    def noAccountFound(self):
        
            #create qmessagebox
            checkAccount = QMessageBox()
            checkAccount.setWindowTitle('Warning!')
            
            #set text
            checkAccount.setText("No account found!")
            
            #set icon and buttons
            checkAccount.setIcon(QMessageBox.Warning)
            checkAccount.setStandardButtons(QMessageBox.Ok)
            
            #set default button
            checkAccount.setDefaultButton(QMessageBox.Ok)
            checkAccount.setInformativeText("The account entered was not found")
            
            #execute
            checkAccount.exec()
        
    
    #method for button click to change username
    def changeUsername_ButtonClick(self):
        
        #collect inputs
        inputTitle = self.title_input.text()
        inputUsername = self.username_input.text()
        inputPassword = self.password_input.text()
        inputNew = self.newUserOrPass_input.text()
        
        #check if account exists
        if self.checkAcctExist(inputTitle, inputUsername, inputPassword) == True:
            #pass to update username
            Database.changeUsername(self.username, inputTitle, inputUsername, inputPassword, inputNew)
            
        else:
            
            self.noAccountFound()
            
        #refresh
        self.refresh()

    #method for button click to change password
    def changePassword_ButtonClick(self):
        
        #collect inputs
        inputTitle = self.title_input.text()
        inputUsername = self.username_input.text()
        inputPassword = self.password_input.text()
        inputNew = self.newUserOrPass_input.text()
        
        #check if account exists
        if self.checkAcctExist(inputTitle, inputUsername, inputPassword) == True:
        
            #pass to update username
            Database.changePassword(self.username, inputTitle, inputUsername, inputPassword, inputNew)
        
        else:
            
            self.noAccountFound()
            
        #refresh
        self.refresh()
        
    #method to return to openingPage
    def logOut_ButtonClick(self):
        
        #take back to openingpage window
        self.cams = openingPage()
        self.cams.show()
        self.close()
    
    #method to 'refresh' page (simple fix to update problem)
    def refresh(self):
        
        #reopen the same window, forcing an update
        self.cams = LandingPage(self.username)
        self.cams.show()
        self.close()
    
    #method for showing data from database
    def dataShow(self):
        
        #update widget
         #add titles header
        column1 = QLabel('<font size="15"> Titles </font>')
        self.innerLayout.addWidget(column1, 0, 0)
        
        #get titles from database
        userTitles = Database.getUserTitles(self.username)
        
        f = 1
        #put titles in as labels
        for titles in userTitles:
            title = QLabel(str(titles.split(",")))
            self.innerLayout.addWidget(title, f, 0)
            f+=1
            
        #add usernames header
        column2 = QLabel('<font size="15"> Usernames </font>')
        self.innerLayout.addWidget(column2, 0, 1)
        
        #get usernames from database
        userUsernames = Database.getUserUsernames(self.username)
        
        i = 1
        #put usernames in as labels
        for names in userUsernames:
            name = QLabel(str(names.split(",")))
            self.innerLayout.addWidget(name, i, 1)
            i+=1
        
        #add passwords header
        column3 = QLabel('<font size="15"> Passwords </font>')
        self.innerLayout.addWidget(column3, 0, 2)
        
        #put passwords in as labels
        userPasswords = Database.getUserPasswords(self.username)
        
        j = 1
        for passes in userPasswords:
            pas = QLabel(str(passes.split(",")))
            self.innerLayout.addWidget(pas, j, 2)
            j+=1
            


# Class to create Login page
class LoginPage(QWidget):
    
    def __init__(self):
        
        #create intake text for username and password
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(1000,500)
        self.UiElements()
        self.Username = "" 
        
    def UiElements(self):
        
        layout = QGridLayout()
        label1 = QLabel('<font size="8"> Username </font>')
        self.user_obj = QLineEdit()
        layout.addWidget(label1, 1, 0)
        layout.addWidget(self.user_obj, 1, 1)
        label2 = QLabel('<font size="8"> Password </font>')
        
        
        #make password unreadable
        self.user_pwd = QLineEdit()
        self.user_pwd.setEchoMode(QLineEdit.Password)
        
        #generate layout for login
        layout.addWidget(label2, 2, 0)
        layout.addWidget(self.user_pwd, 2, 1)
        
        #login button
        button_login = QPushButton('Login')
        layout.addWidget(button_login, 2, 0, 3, 2)

        #login button click
        button_login.clicked.connect(self.loginButtonClick)
        
        #go back button
        button_return = QPushButton('Go Back')
        layout.addWidget(button_return, 2, 0, 4, 2)
        self.setLayout(layout)
    
        button_return.clicked.connect(self.goBackButtonClick)
    
    #make button click action for return
    def goBackButtonClick(self):
        
        self.cams = openingPage()
        self.cams.show()
        self.close()
    
    #method for login button click
    def loginButtonClick(self):
        
        #get text from user upon click
        inputUsername = self.user_obj.text()
        inputPassword = self.user_pwd.text()
        
        
        if self.checkPassword(inputUsername, inputPassword) == True:
            
            self.Username = self.user_obj.text()
            
            self.cams = LandingPage(self.Username)
            self.cams.show()
            self.close()
            
        else:
    
            self.incorrectLoginPopUp()
            
    #check if the username/password combo matches the input
    def checkPassword(self, username, password):
        
        #get saved user from database
        savedPassword = Database.getPassword(username)
        
        #format input from user for comparison against saved
        inputLogin = [(username, password)]
        
        #check input against saved user
        if savedPassword == inputLogin:
            return True
        else:
            return False
    
    #create popup to alert of incorrect login
    def incorrectLoginPopUp(self):
        #create popup due to incorrect username or password
            #create qmessagebox
            wrongUserOrPass = QMessageBox()
            wrongUserOrPass.setWindowTitle('Warning!')
            
            #set text
            wrongUserOrPass.setText("Incorrect Username or Password")
            
            #set icon and buttons
            wrongUserOrPass.setIcon(QMessageBox.Warning)
            wrongUserOrPass.setStandardButtons(QMessageBox.Ok)
            
            #set default button
            wrongUserOrPass.setDefaultButton(QMessageBox.Ok)
            wrongUserOrPass.setInformativeText("The username or password attempted was incorrect")
            
            #execute
            wrongUserOrPass.exec()
    
    #method to get username from input (and save it)
    def getUsername(self):
        
        #get and return the inputed username
        username = self.Username
        return username
        


# Class to create create user page
class CreateUser(QWidget):
    
    #init method
    def __init__(self):
        
        #create user creation page
        super().__init__()
        
        #set window title
        self.setWindowTitle("Create/Delete User")
        
        #set window size
        self.resize(1000, 500)
        
        self.UiGui()
    
    #method for UI
    def UiGui(self):
        #create grid layout
        layout = QGridLayout()
        
        #create label
        label1 = QLabel('<font size="8"> Username </font>')
        
        #create input line
        self.user_obj = QLineEdit()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.user_obj, 0, 1)
        
        #label for password
        label2 = QLabel('<font size="8"> Password </font>')
        
        #create input line for password
        self.obj_pass = QLineEdit()
        
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.obj_pass, 1, 1)
        
        #create create account button
        button_create_acct = QPushButton('Create User')
        layout.addWidget(button_create_acct, 2, 0, 1, 2)
        
        #button click
        button_create_acct.clicked.connect(self.createUserButtonClick)
        
        #create delete account button
        button_delete_acct = QPushButton('Delete User')
        layout.addWidget(button_delete_acct, 3, 0, 1, 2)
        
        #delete button click
        button_delete_acct.clicked.connect(self.deleteUserButtonClick)
        
        #create go back button
        button_return = QPushButton('Go Back')
        layout.addWidget(button_return, 4, 0, 1, 2)
        self.setLayout(layout)
        
        button_return.clicked.connect(self.returnButtonClick)
        
    #return to previous window
    def returnButtonClick (self):
        
        #show openingPage and close current window
        self.cams = openingPage()
        self.cams.show()
        self.close()
    
    #method for create user button click
    def createUserButtonClick(self):
        
        inputUsername = self.user_obj.text()
        inputPassword = self.obj_pass.text()
        
        if self.checkIfUserExists(inputUsername, inputPassword) == True:
            
            self.userExistPopup()
            
        else:
            
            #set the username to the input
            self.Username = self.user_obj.text()
            
            #add user in database
            Database.addUser(inputUsername, inputPassword)
            
            self.cams = LandingPage(self.Username)
            self.cams.show()
            self.close()
    
    #method for delete user button click
    def deleteUserButtonClick(self):
        
        inputUsername = self.user_obj.text()
        inputPassword = self.obj_pass.text()
        
        if self.checkIfUserExists(inputUsername, inputPassword) == True:
            
            #create popup to confirm that the user wants to delete the user
            self.confirmDelete(inputUsername, inputPassword)
            
        else:
            
            #create popup to inform that no user exists
            self.noUserFound()
    
    #method to check if the user exists
    def checkIfUserExists(self, username, password):
        
        #get saved user from database
        savedPassword = Database.getPassword(username)
        
        #format input from user for comparison against saved
        inputCreate = [(username, password)]
        
        #check input against saved user
        if savedPassword == inputCreate:
            return True
        else:
            return False
    
    #method to popup if user exists
    def userExistPopup(self):
        #create popup due to user existing
            #create qmessagebox
            userExist = QMessageBox()
            userExist.setWindowTitle('Warning!')
            
            #set text
            userExist.setText("User Already Exists")
            
            #set icon and buttons
            userExist.setIcon(QMessageBox.Warning)
            userExist.setStandardButtons(QMessageBox.Ok)
            
            #set default button
            userExist.setDefaultButton(QMessageBox.Ok)
            userExist.setInformativeText("The user login that you are attempting to create already exists")
            
            #execute
            userExist.exec()
    
    #popup to confirm deletion of user
    def confirmDelete(self, username, password):
        #create popup to confirm delete
        confirmDelete = QMessageBox()
        confirmDelete.setWindowTitle('Confirm Delete')
        
        #set text
        confirmDelete.setText("Are you sure you want to delete this user?")
        
        #set icon and buttons
        confirmDelete.setIcon(QMessageBox.Warning) 
        confirmDelete.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel)
        
        #set default
        confirmDelete.setDefaultButton(QMessageBox.Cancel)
        confirmDelete.setInformativeText("The user and all saved accounts will be deleted perminantly.")
    
        result = confirmDelete.exec()
        
        if result == QMessageBox.Yes:
            # do yes-action
            Database.deleteUser(username, password)
            
            #switch to main screen
            self.cams = openingPage()
            self.cams.show()
            self.close()
        else:
            # do no-action
            pass
    
    #create popup if no user found to delete       
    def noUserFound(self):
        
        #create popup to inform no user found
        noUser = QMessageBox()
        noUser.setWindowTitle('No User Found')
        
        #set Text
        noUser.setText ("No User Found")
        
        #set icon and buttons
        noUser.setIcon(QMessageBox.Warning)
        noUser.setStandardButtons(QMessageBox.Ok)
        
        #set defaults
        noUser.setDefaultButton(QMessageBox.Ok)
        noUser.setInformativeText("No user with the username and password entered was found")
        
        noUser.exec()



# Class for first opening
class openingPage(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.logWindow = LoginPage()
        
        self.makeUser = CreateUser()
        
        self.setWindowTitle("Password Manager")
        
        self.resize(1000,500)
        
        layout = QGridLayout()
        
        #create welcome label
        welcome_label = QLabel('<font size="15"> Welcome to Password Manager! </font>')
        layout.addWidget(welcome_label, 0, 1, 3, 1)
        
        #create button for create user
        button_create = QPushButton('Create/ Delete User')
        layout.addWidget(button_create, 2, 1, 5, 1)
        
        #create button for login
        button_log = QPushButton('Login')
        layout.addWidget(button_log, 2, 2, 5, 1)
        
        #click for log_button
        button_log.clicked.connect(self.logButtonClick)
        
        #click for button_create
        button_create.clicked.connect(self.createButtonClick)
        
        #create layout
        self.setLayout(layout)
        
    #switch to createUser on button click
    def createButtonClick (self):
        
        self.cams = CreateUser()
        self.cams.show()
        self.close()
        
    #switch to login on button click
    def logButtonClick(self):
        
        self.cams = LoginPage()
        self.cams.show()
        self.close()
   
        
     
#create app instance
app = QApplication((sys.argv))

form = openingPage()

#run and show app
form.show()
app.exec_()