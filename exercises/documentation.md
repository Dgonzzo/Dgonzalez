# Documentation

This is the documentation for the python program made by Daniel González.  

# Execution
The code is uploaded on classroom. You have to install the file.py on your computer and execute it on the terminal by using the python interpreter or with vscode once having installed the python's extension.

# File management

The file extension used by the program is the xml. The file can be already created before the execution of the program. However, if it does not exists, it will create a new file with the name: **inventory.xml**.

> **Note**: The program will only use the file which name matches with the one stored at the variable "file_name". You can change the value as you wish. 

# OS
To better user experience, change manually the variable `user_os` depending on the operative system you are using on your device.
- **Unix-based systems**: `user_os = 'Unix'`
- **Windows**: `user_os = 'Windows'`

> **Note**: Linux, MacOS and BSD systems are Unix-based.

# Stored data

All the data will be stored at the file.xml with the following properties:
- Author
- Released date:
    - Day
    - Month
    - Year
- Genre
- Age clasification
- Language
- ISBN
- Price

# Dependencies

This programs use different modules for its execution. 
In order to avoid errors of execution, the following modules should be installed on your device:
- `xml` **Note**: This extension is mandatory for the correct execution of the program
- `colorama`

# Main menu

When starting the program, the user will be asked for an input.
- For each number from 1 to 5, matches for a main function.

> **Note** Do not press spacebar before pressing enter.
- 'q' for exiting the program.
> **Note** Pressing 'Q' will also close the program. However, as well as for the main functions, do not press spacebar before pressing enter.

## Add

This option makes a new objecct at the root path, its tag is the book's title.
Then, follows the hierarchy mentioned previosly.

> **Note** You must enter an item before doing anything else.
> **Note** It is mandatory to insert a book title, otherwise the whole program will crash.

> **Note** When inserting released_date, insert numerical values separated by a comma with the following order `day month year`, for example `01 01 2000`, please do not press enter. 
Otherwise, it may crash the program when trying to calculate how old is the book.

> **Note** When adding the price, insert a float value, do not press enter, for example `0.00`. 
Otherwise, it may crash the program when trying to calculte the revenue.

## Update

With this function you can change the properties or values of an object that has been previouly created.

> **Note**: You can't change all the values of an object at the same prompt 

## Delete

The function's name is self explanatory, it eliminates an object at the file.

To use it correctly, only the name of the object (the book's title) has to be introduced.  

## Consult

Prints the desire information on the terminal. 
You can choose from printing all the books at the inventory or just one book's property.  


## Calculate

With this function you can check and calculate some information from the your inventory's item.
