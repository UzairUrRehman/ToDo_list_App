To-Do List Application – Python

A console-based task management application built in Python, featuring task creation, viewing, removal, status tracking, and a menu-driven interface.

Overview

This project implements a simple command-line To-Do List manager that allows users to organize and track their daily tasks.

Users interact with the application through a numeric menu system to add, view, delete, and mark tasks as completed. The program continuously runs until the user chooses to exit, making it convenient for managing multiple tasks in one session.

The task list is stored in memory using Python data structures, and each task maintains its own completion status.

Core Features

Menu-driven console interface
Add new tasks to the list
View all tasks with their status
Remove tasks by task number
Mark tasks as completed
Input validation for incorrect entries
Continuous program loop until user exits

Technology Stack

Language: Python
Standard Library: Built-in Python functions only
Execution Environment: Terminal / Command Prompt / VS Code Terminal
Programming Style: Procedural

Application Mechanics

Tasks are stored in a list of dictionaries
Each task contains:

Task Name

Status (pending / completed)

The main menu provides five options:

Add a New Task

View All Tasks

Remove a Task

Mark a Task as Completed

Exit the Application

User input determines which function is executed.
The program includes error handling for invalid numbers and out-of-range task selections.

Project Structure

todo_list_app/
│
├── ToDo_list_App.py → Main application code
├── ToDo_list_App.sln → Visual Studio solution file
├── ToDo_list_App.pyproj → Visual Studio Python project file
├── .gitignore → Git ignored files configuration
├── .gitattributes → Git attributes configuration
└── README.md → Project documentation
