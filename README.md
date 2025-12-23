		

 Tours & Travels Management System
This is a Python-based terminal application designed to manage travel bookings for a tour company. It allows users to select travel destinations, calculate total costs based on food and activities, and store customer information in a MySQL database.

Features
Customer Features
	•	Booking Management: Users can enter personal details, select destinations (Manali, Rishikesh, or Goa), and choose specific seasonal packages.
	•	Cost Calculation: The system automatically calculates the total bill based on:
	•	The number of adults and children.
	•	Food preferences (Jain or Regular).
	•	Optional activities like camping, skiing, or river crossing.
	•	Update Information: Customers can update their registered mobile numbers.
	•	Search and Cancel: Users can search for their booking details or delete their booking using their mobile number.
Admin Features
	•	Secure Login: A protected admin area accessible only via specific credentials.
	•	View All Bookings: Admins can see a complete list of all customer records stored in the database.
	•	Delete Records: Admins have the authority to remove any booking from the system.

Technical Details
Prerequisites
	•	Python 3.x: The core programming language used.
	•	MySQL Server: Used to store and manage customer data.
	•	PyMySQL Library: The connector used to link Python with the MySQL database.
Database Structure
The system automatically creates a database named tat and a table named cust with the following fields:
	•	ID (Primary Key, Auto-increment)
	•	First Name and Last Name
	•	Mobile Number
	•	Age
	•	Number of Persons
	•	Total Bill Amount

How to Run
	1	Install Requirements: Ensure you have PyMySQL installed by running pip install pymysql.
	2	Configure Database: Update the db connection line in the code with your local MySQL password.
	3	Run the Script: Execute the file using python travel.py.
	4	Navigation: Use the numeric menus to navigate through the Admin or Customer sections.

Project Structure
	•	travel.py: Contains the main logic, including database connection, menu systems, and billing calculations.
