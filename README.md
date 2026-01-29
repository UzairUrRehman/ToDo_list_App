# To-Do List Application – Python

A **console-based task management application** implemented in **Python**, featuring task creation, viewing, removal, status tracking, and a menu-driven interface.

---

## Overview
This project implements a simple **command-line To-Do List manager** for organizing and tracking daily tasks.  
Users interact with the application through a numeric menu system to add, view, delete, and mark tasks as completed.  
The program runs continuously until the user chooses to exit, allowing multiple tasks to be managed in a single session.

---

## Core Features
- Menu-driven console interface  
- Add new tasks  
- View all tasks with their status  
- Remove tasks by task number  
- Mark tasks as completed  
- Input validation for invalid entries  
- Continuous program loop until exit  

---

## Technology Stack
- **Language:** Python  
- **Standard Library:** Built-in Python functions  
- **Execution Environment:** Terminal / Command Prompt / VS Code Terminal  
- **Programming Style:** Procedural  

---

## Application Mechanics
- Tasks are stored in a **list of dictionaries**  
- Each task contains:
  - **Task Name**  
  - **Status** (`pending` or `completed`)  
- The main menu provides the following options:
  - Add a New Task  
  - View All Tasks  
  - Remove a Task  
  - Mark a Task as Completed  
  - Exit the Application  
- User input determines which function is executed  
- Input validation ensures correct task selection and prevents errors  

---

## Project Structure

- **todo_list_app/**  
  - `ToDo_list_App.py` → Main application code  
  - `ToDo_list_App.sln` → Visual Studio solution file  
  - `ToDo_list_App.pyproj` → Visual Studio Python project file  
