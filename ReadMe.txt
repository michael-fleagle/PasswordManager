Project: CS 112 Final Project: Password Manager

Author: Michael Fleagle
Date completed: 18-Nov-2020
Language: Python

Original Project Proposal: "I want to make a password manager that will encompass three main components: a mySQL database, 
				industry(ish) level encryption/hashing, and a simple GUI to improve user experience. The project 
				would utilize a username/password login to enable multiple users and protect each user’s passwords. 
				The goal would be to create an easy to use password manager that utilizes a database and as close to industry 
				level encryption/security as possible. I would utilize the Kivy or PyQT5 library to help handle the GUI, and 
				mySQL Connector to connect to the mySQL database. More libraries may be added as needed. If I find that I have 
				more time then expected for the project, additional features may be added. 
							
Actual Project Implementation: This project creates an easy to use/simplistic password manager featuring multiple
							possible users and a basic GUI. The passwords and logins are stored in a mySQL database. 
							Unfortunately, due to time constraints and complexity no password encryption 
							was able to be implemented. 
 
							I utilize the PyQT5 library to help handle the GUI, and mySQL 
							Connector to connect to the mySQL database.
							
Project Key Aspects: GUI (using PyQt5), Database (using mySQL)

Libraries implemented: PyQt5, mysql.connector

Application Guide/Walkthrough:
	
	Getting Started
	1) Run PasswordManager.py
	2) For first time use: Click "Create/Delete User" button to create a user login
	3) Enter a Username and Password to use for login
	4) Click the "Create User" button to create the user login account and add the username and password to the database table 'logins'
	
	To Add a New Saved Account
	1) To add an account to be saved, input the title, username, and passsword of the account into their respective type-boxes
	2) Click the "Add Account" Button

	To Delete a Saved Account
	1) Type the exact title, username, and password for the account you wish to delete into the title, username, and password type-boxes. You can use the displayed accounts on the side as reference.
	2) Click the "Delete Account" button

	To Change an Account Username
	1) Type the exact title, username (the current/old username displayed on the right), and password for the account you wish to change the username for into the title, username, and password type-boxes.
	2) Type the new username that you wish to change to into the "New Username/Password" typebox
	3) Click the "Change Account Username" button

	To Change the Account Password
	1) Type the exact title, username, and password (the current/old password displayed on the right) for the account you wish to change the password for into the title, username, and password type-boxes.
	2) Type the new password that you wish to change to into the "New Username/Password" typebox
	3) Click the "Change Account Password" button

	To Logout/Return to the Main Menu
	1) Click the "Logout" button

	To Login to an existing User Login Account
	1) From the main menu, click the "Login" button
	2) Enter the exact username and password used to create the user login account into the username and password typeboxes
	3) Click the "Login" button

	To Delete a User Login and User Data **WARNING-THIS WILL PERMENANTLY DELETE ALL SAVED USER ACCOUNTS AS WELL**
	1) From the main menu, click the "Create/Delete User" button
	2) Enter the username and password for the already existing user login account
	3) Click the "Delete User" button
	4) Confirm by clicking the "yes" button on the popup window