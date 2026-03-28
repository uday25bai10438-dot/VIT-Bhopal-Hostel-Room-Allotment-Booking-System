# VIT-Bhopal-Hostel-Room-Allotment-Booking-System
A straightforward and effective desktop program for managing student reservations and hostel room assignments.  Constructed with SQLite for the database and Python Tkinter for the graphical user interface, this system offers all the CRUD (Create, Read, Update, Delete) features needed for efficient hostel management.
Project Definition: Hostel Room Allotment System
System for Allocating Hostel Rooms

 ● Title of Project

 Booking and Allocation of Hostel Rooms (Tkinter/SQLite)

 An overview of the project

 The goal of this project is to manage student room reservations and allotments in a hostel setting using a straightforward, stand-alone desktop application.  Using the standard tkinter library for Python, it offers a Graphical User Interface (GUI) that enables users to carry out common CRUD (Create, Read, Update, Delete) operations on booking records.

 Booking data is preserved even after the application is closed thanks to the application's use of an embedded SQLite database (hostel.db) for lightweight and persistent storage.  For minor administrative duties in a dorm or college, it is perfect.
 Features

 The following essential features are offered by the application:

 Add Booking: Update the database with new student records (Name, Roll No., Room No., Department).

 View All Bookings: In a clear, scrollable table (Treeview), show all current records.

 Choose Record: The input fields are filled in for simple editing when you click on a row in the table.

 Update Record: Make changes to a chosen booking record's details and store them in the database.

 Delete Record: Take a particular booking record out of the system permanently.

 Clear Fields: Reset every field in the input form.

 Data Persistence: Every record is kept locally in a SQLite database.
 How to install and operate the project

 Installation is simple because this project only makes use of standard Python libraries.


 Requirements

 Python 3 needs to be installed on your computer.

 Installation and Implementation

 Keep the code safe:  The supplied Python code should be saved in a file called hostel_allotment.py.

 Execute the script:  Go to the directory where you saved the file in your terminal or command prompt, then type the following command:

 Hostel_allotment.py in Python
 
 Guidelines for testing

 To test all of the application's main features, follow these steps:


 Test Add Reservation:

 Fill in the input fields with your name, department, roll number, and room number.

 Press the "Add Booking" button.

 Anticipated Outcome: The fields should clear, a success message should show up, and the new record should show up in the table below.

 To test for errors, click "Add Booking" without providing a name, roll number, or room number.  A "Input Error" alert ought to show up.

 Test View and Select:

 In the table that is displayed, click on any row.

 Expected Outcome: The Name, Roll No., Room No., and Department input fields should instantly be filled in with the information from the chosen row.


 Update for Testing:

 Choose a record that already exists in the table (see step 2).

 Modify one or more fields, such as the Room No.

 Press the "Update" button.

 Anticipated Outcome: The table should instantly reflect the modification and a "Updated" success message should show up.

 Test Removal:

 Choose the record you want to delete from the table.

 Press the "Delete" button.

 Anticipated Outcome: The record should disappear from the table and a "Deleted" success message should show up.

 Clear the test:

 Click "Clear" if there is data in the input fields.

 Anticipated Outcome: All four input fields ought to be empty.

 ● Screenshots (recommended but optional)
