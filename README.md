A simple desktop To-Do List application built with Tkinter, Python’s standard GUI library. This app allows users to add, delete, and toggle the completion status of tasks in a straightforward graphical interface. Tasks are stored in memory and do not persist after the app closes.<br />

**Features**<br />
Add Tasks: Enter a task and add it to your list.<br />
Delete Tasks: Remove selected tasks.<br />
Toggle Completion: Mark tasks as complete or incomplete with a checkbox-like indicator.<br />
Simple Interface: Easy-to-use window with a listbox and buttons.<br />
Error Handling: Warnings for invalid actions (e.g., no task selected).<br />

**Requirements**<br />
Python 3.x (Tkinter is included by default, no additional installation needed)<br />

**Setup Instructions**<br />
Follow these steps to run the project on your machine.<br />

1. Clone or Download<br />
If using Git, clone the project:<br />
git clone https://github.com/sujal7746/Tkinter-To-Do-List-App<br />
cd todo_tkinter<br />
Or download the todo_tkinter.py file and place it in a directory.<br />
2. Verify Python<br />
Ensure Python 3.x is installed:<br />
python --version<br />
Output should be something like Python 3.12.0. Tkinter comes pre-installed with Python.<br />
3. Run the Application<br />
Navigate to the directory containing todo_tkinter.py:<br />

cd path/to/todo_tkinter<br />
Run the script:<br />
A window titled "To-Do List" (400x400 pixels) will appear.<br />


**Usage**<br />
Add a Task:<br />
Type a task in the text box and click "Add Task".<br />
The task appears in the list as "[ ] Task Name".<br />
Toggle Completion:<br />
Select a task in the list and click "Toggle Complete".<br />
Completed tasks show as "[✓] Task Name"; incomplete tasks revert to "[ ] Task Name".<br />
Delete a Task:<br />
Select a task and click "Delete Task" to remove it.<br />
.


**Troubleshooting**<br />
Error: "No module named tkinter"<br />
Ensure you’re using Python 3.x (not a minimal install without Tkinter). Reinstall Python if needed.<br />
Window Doesn’t Open:<br />
Check for typos in todo_tkinter.py. Ensure window.mainloop() is at the end.<br />
Bad Geometry Error:<br />
Verify window.geometry("400x400") uses a lowercase x.<br />
