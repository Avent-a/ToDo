# ToDo List Application

This is a simple ToDo List application built using Python and Tkinter. It allows users to add and delete tasks from a list, with the tasks being saved to a file for persistence.

## Features

- **Add Task:** Add new tasks to your to-do list.
- **Delete Task:** Remove tasks from your to-do list.
- **Persistent Storage:** Tasks are saved to a file (`tasklist.txt`) and loaded automatically when the application starts.

## Installation

1. **Clone the repository** (if using a version control system):
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Python** (if not already installed):
    - Download and install Python from [python.org](https://www.python.org/).

3. **Install Tkinter** (if not already installed):
    - Tkinter usually comes pre-installed with Python. If it's not installed, you can install it using the following command:
      ```sh
      pip install tk
      ```

4. **Prepare the images**:
    - Place your images (`task.png`, `topbar.png`, `dock.png`, `delete.png`) in the specified directory as used in the code.

## Usage

1. **Run the application**:
    ```sh
    python todo.py
    ```

2. **Add a Task**:
    - Type a task in the input field and click the "add" button.

3. **Delete a Task**:
    - Select a task from the list and click the delete button.

## Code Overview

### Main Components

- **Root Window**:
    - Title: `todo`
    - Size: `400x650`
    - Non-resizable

- **Task Management**:
    - `addTask()`: Adds a task to the list and saves it to the file.
    - `deleteTask()`: Deletes a task from the list and updates the file.
    - `openTaskFile()`: Loads tasks from the file when the application starts.

### UI Elements

- **Images and Icons**:
    - `Image_icon`: Application icon.
    - `topImage`: Top bar image.
    - `dockImage`: Dock image.
    - `noteImage`: Note image.
    - `Delete_icon`: Delete button icon.

- **Labels**:
    - Heading: "ALL TASK"

- **Input Field**:
    - Entry for adding new tasks.

- **Buttons**:
    - Add Button: Adds a new task.
    - Delete Button: Deletes the selected task.

- **Listbox**:
    - Displays the list of tasks.
    - Configured with a scrollbar for easier navigation.

## File Structure

- **tasklist.txt**: File used for storing tasks.

---

Enjoy managing your tasks with this simple ToDo List application!
