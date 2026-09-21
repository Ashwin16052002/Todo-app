# 📝 Todo App

A simple Python-based **To-Do application** that allows users to create, view, edit, and complete tasks.

The project provides **three different ways to manage your tasks**:

* 💻 Command-Line Interface (CLI)
* 🖥️ Desktop GUI using PySimpleGUI
* 🌐 Web interface using Streamlit

All three interfaces share the same task-management functions and store the tasks in a simple `todos.txt` file.

## ✨ Features

* ➕ Add new tasks
* 📋 View existing tasks
* ✏️ Edit tasks
* ✅ Complete/remove tasks
* 💾 Persistent task storage using a text file
* 💻 Command-line interface
* 🖥️ Desktop graphical interface
* 🌐 Streamlit web application
* 🕒 Displays the current date and time
* 🔄 All interfaces use the same underlying task data

## 🛠️ Technologies Used

* **Python** – Core programming language
* **PySimpleGUI** – Desktop graphical user interface
* **Streamlit** – Web-based interface
* **File Handling** – Persistent storage using `todos.txt`
* **Time** – Displays the current date and time

## 📂 Project Structure

```text
Todo-app/
│
├── cli.py
├── gui.py
├── web.py
├── functions.py
├── todos.txt
└── .gitignore
```

### `functions.py`

Contains the common task-management functions used by the application.

It provides:

* `get_todo()` – Reads tasks from `todos.txt`
* `write_todos()` – Writes the updated task list back to `todos.txt`

This allows the CLI, GUI, and web application to use the same underlying storage mechanism.

### `cli.py`

Provides a command-line interface for managing tasks.

Supported commands include:

```text
add
show
edit
complete
exit
```

The CLI reads and modifies tasks through `functions.py`.

### `gui.py`

Provides a desktop graphical interface using **PySimpleGUI**.

The GUI includes:

* Task input field
* Add button
* Task list
* Edit button
* Complete button
* Exit button
* Live date/time display

### `web.py`

Provides a browser-based interface using **Streamlit**.

The web application allows users to:

* Add new tasks
* View tasks
* Mark tasks as completed
* Remove completed tasks
* Store tasks in `todos.txt`

### `todos.txt`

This file acts as the application's simple persistent storage.

Each task is stored as a separate line.

Example:

```text
Complete Python project
Study for interview
Read a book
Go for a walk
```

## ⚙️ Application Architecture

```text
                 ┌───────────────┐
                 │   User Tasks  │
                 └───────┬───────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
     ┌─────────┐   ┌───────────┐   ┌─────────┐
     │  CLI    │   │    GUI    │   │   Web   │
     │ cli.py  │   │  gui.py   │   │ web.py  │
     └────┬────┘   └─────┬─────┘   └────┬────┘
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                  ┌─────────────┐
                  │ functions.py│
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │  todos.txt  │
                  └─────────────┘
```

## 🔄 How It Works

### 1. Add a Task

A task can be added through any of the available interfaces.

The application reads the existing tasks, adds the new task, and writes the updated list back to `todos.txt`.

```python
todos = functions.get_todo()
todos.append(todo + '\n')
functions.write_todos(todos)
```

### 2. View Tasks

The application reads the contents of `todos.txt` and displays each task.

The CLI displays tasks with a numbered format:

```text
1-Complete Python project
2-Study for interview
3-Read documentation
```

### 3. Edit a Task

The user selects a task and provides the replacement text.

The selected task is then updated in `todos.txt`.

### 4. Complete a Task

Completing a task removes it from the active task list.

The updated list is written back to `todos.txt`.

## 💻 Command-Line Interface

Run:

```bash
python cli.py
```

The application displays:

```text
Enter add, show, edit, complete or exit:
```

### Add

```text
add Learn Python
```

### Show

```text
show
```

Example output:

```text
1-Learn Python
2-Complete project
3-Study Flask
```

### Edit

```text
edit 1
```

The application then asks:

```text
Enter a new To-do:
```

### Complete

```text
complete 1
```

The selected task is removed from the list.

### Exit

```text
exit
```

## 🖥️ Desktop GUI

Run:

```bash
python gui.py
```

The desktop application provides a graphical interface with:

```text
┌─────────────────────────────────────┐
│             To-Do App               │
│                                     │
│  Type in a To-do                    │
│  ┌──────────────────┐  [ Add ]      │
│  │                  │               │
│  └──────────────────┘               │
│                                     │
│  ┌───────────────────────────────┐  │
│  │ Task 1                        │  │
│  │ Task 2                        │  │
│  │ Task 3                        │  │
│  └───────────────────────────────┘  │
│                                     │
│  [Edit] [Complete]     [Exit]       │
└─────────────────────────────────────┘
```

The GUI uses PySimpleGUI and shares the same `todos.txt` storage used by the other interfaces.

## 🌐 Web Application

Run:

```bash
streamlit run web.py
```

The application opens a browser-based Todo interface.

The web application:

1. Loads existing tasks.
2. Displays them as checkboxes.
3. Allows users to add new tasks.
4. Removes a task when its checkbox is selected.
5. Saves changes back to `todos.txt`.

## 🚀 Installation

### Prerequisites

Make sure Python 3.x is installed.

Check your Python version:

```bash
python --version
```

### Clone the Repository

```bash
git clone https://github.com/Ashwin16052002/Todo-app.git
```

Navigate into the project:

```bash
cd Todo-app
```

### Install Dependencies

Install the required libraries:

```bash
pip install PySimpleGUI streamlit
```

## ▶️ Running the Project

### CLI Version

```bash
python cli.py
```

### Desktop GUI Version

```bash
python gui.py
```

### Web Version

```bash
streamlit run web.py
```

You can choose whichever interface is most convenient.

## 💾 Data Storage

This project uses a simple text-file-based storage system rather than a database.

```text
Application
     │
     ▼
functions.py
     │
     ▼
todos.txt
```

The `get_todo()` function reads the file, while `write_todos()` updates it.

This makes the project simple to understand and suitable for learning Python file handling.

## 🎯 Project Objectives

The project demonstrates several fundamental Python concepts:

* Functions
* File handling
* Lists
* Loops
* Conditional statements
* Exception handling
* User input
* GUI programming
* Web application development
* Code reuse through shared functions

## 📚 Learning Outcomes

By working with this project, you can learn:

* How to build a CLI application
* How to create a desktop GUI using PySimpleGUI
* How to create a web application using Streamlit
* How to read and write files using Python
* How multiple interfaces can share the same backend logic
* How to persist application data without using a database

## 🚀 Future Improvements

Possible improvements for future versions:

* [ ] Add task due dates
* [ ] Add task priorities
* [ ] Add task categories
* [ ] Add search functionality
* [ ] Add task completion status instead of deleting completed tasks
* [ ] Add database support using SQLite
* [ ] Add user accounts
* [ ] Add authentication
* [ ] Add cloud synchronization
* [ ] Add task reminders
* [ ] Improve GUI design
* [ ] Add responsive web styling
* [ ] Add automated tests
* [ ] Add requirements.txt
* [ ] Add deployment configuration

## 👨‍💻 Author

**Ashwin V**

GitHub:
https://github.com/Ashwin16052002

LinkedIn:
https://www.linkedin.com/in/ashwin-v-5124992a9/

## 📜 License

This project is intended for educational and personal use.

---
