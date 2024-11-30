Skill Circle Library System - README
Overview - The Skill Circle Library System is a simple Python program designed to simulate a basic library information system.
Users can interact with the system to viewdetails about specific books by selecting options from a menu.

PROGRAM FLOW 
1. Display Welcome Message: The program begins by displaying the library system name and book selection menu.
2. User Input for Book Selection: The user selects a book by entering a number corresponding to the options displayed.
3. Display Book Details: The details of the selected book are displayed on the screen.
4. Continuation or Exit: The user is prompted to either continue browsing or exit the system:
-Enter 0 to return to the main menu.
-Enter 9 to exit the system.
5. Handle Invalid Inputs: If an invalid option is entered, the program gracefully informs the user and exits.

BOOK MENU OPTIONS
The menu includes the following options:

1. Press 1: Information about Data Analytics using Python
2. Press 2: Information about Time Machine
3. Press 3: Information about Treasure Island
4. Press 4: Information about Romeo and Juliet
5. Press 5: Information about The Tempest

CODE COMPONENTS
Variables
-Book Information: Each book's details (e.g., title, author, price, language, rating) are stored in individual variables such as book101, book102, etc.

Functions
1. start():
-Displays the book menu.
-Calls the main() function to handle the user's selection.
2. main():
-Captures user input for book selection.
-Displays the corresponding book details.
-Provides options to continue or exit.
-Handles invalid inputs.

USER INSTRUCTIONS
Running the Program
1. Execute the script in a Python 3.x environment.
2. Follow the on-screen instructions to navigate through the system.

Input Commands
1. Enter a number between 1 and 5 to view book information.
2. Enter 0 to return to the main menu.
3. Enter 9 to exit the system.

EXAMPLE INTERACTION

Step 1: Menu Display
Skill Circle Library System
press 1 for 101 book information
press 2 for 102 book information
press 3 for 103 book information
press 4 for 104 book information
press 5 for 105 book information

Step 2: User Input
Enter the number of book information: 3

Step 3: Book Details
Title=Treasure Island
Author=R.L. Stevenson
Price=670
Language=English
Rating=4.5

Step 4: Continuation Prompt
Do you want to continue 
if yes press 0 
if exit press 9

ERROR HANDLING
1. Invalid Book Selection:
If a number outside the range 1-5 is entered, the program will display:
invalid input. Thanks for visiting.
2. Invalid Continuation Command:
If an option other than 0 or 9 is entered, the program will display:
Invalid input

ADVANTAGES OF THIS SYSTEM
1. Simple and intuitive user interface.
2. Clear instructions for every step of interaction.
3. Graceful handling of unexpected inputs.

SYSTEM REQUIREMENTS -
Python 3.x

KEY LEARNING POINTS -
-String Handling: Organizing and displaying book details.
-Control Flow: Using conditional statements to guide program behavior.
-User Input: Capturing and validating input from users.

This library system provides a basic yet functional demonstration of Python programming concepts while serving as a stepping stone for building more complex applications.
























 
