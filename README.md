# TaskFlow 📝

A simple command-line task management application built using **Python**.

TaskFlow helps users manage their daily tasks directly from the terminal. Users can create, view, complete, and delete tasks while keeping their data saved using JSON file storage.

## Features ✨

- ✅ Add new tasks
- 📋 View all tasks
- ✔️ Mark tasks as completed
- 🗑️ Delete tasks
- 💾 Persistent storage using JSON
- ⚠️ Handles invalid inputs

## Technologies Used 🛠️

- Python 3
- JSON File Handling

## Project Structure 📂

```
TaskFlow/
│
├── main.py          # Main application logic
├── tasks.json       # Task storage file
└── README.md        # Project documentation
```

## How to Run 🚀

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/TaskFlow.git
```

### 2. Navigate to the project folder

```bash
cd TaskFlow
```

### 3. Run the application

```bash
python main.py
```

## Usage Example 💻

```
====== TaskFlow ======

1. View Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Exit

Choose option: 2

Enter task: Learn Python

Task added!
```

## Task Storage Example 📄

Tasks are saved inside `tasks.json`:

```json
[
    {
        "title": "Learn Python",
        "completed": false
    },
    {
        "title": "Create GitHub Repository",
        "completed": true
    }
]
```

## Testing ✅

The application was tested with:

- Adding multiple tasks
- Viewing saved tasks
- Completing tasks
- Deleting tasks
- Restarting the application to verify data persistence
- Handling invalid inputs

## Future Improvements 🚀

- Add task deadlines
- Add task priorities
- Add search functionality
- Add a graphical user interface (GUI)
- Replace JSON storage with a database

## Author 👨‍💻

Created by AD
