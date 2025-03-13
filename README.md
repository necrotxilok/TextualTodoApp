
# TextualTodoApp

This is a simple TUI application to manage todo lists created with Textual.

<img width="1262" alt="imagen" src="https://github.com/user-attachments/assets/7e61275d-c3df-4514-82a4-891380c84a2e" />


The application allows you to create a list of tasks in JSON format in current
directory. The JSON file will be created only when you add a new task.


Key Bindings:
 a           > Add a new task.
 Up/Down     > Select task in the list.
 Space/Enter > Mark/Unmark task as completed.
 e           > Edit the selected task.
 r           > Remove the selected task.
 ^p          > Textual Command Palette
 q           > Exit the application.



## Dependencies

- [Python3](https://www.python.org/)
- [Textual](https://textual.textualize.io/)
- [PyInstaller](https://pyinstaller.org/en/stable/) (Optional)



## Run the Application

You have to install Python3 in your system and then run this command to install 
Textual Framework:

```bash
pip install textual textual-dev
```

Into the project folder you can run next command to run the project:

```bash
python src/todo.py
```



## Run in Dev Mode

If you want to modify this app and view all logs from Textual Framework you
need to open 2 terminal applications.

In the first terminal, run this command to open the Textual Console:

```bash
textual console
```

In the second one, run this command to open application in development mode:

```bash
textual run --dev src/todo.py
```

Then you will see all events and logs received from the application to the
console.

To detach the console use Ctrl+C.



## Building the App

To create a final executable to run in any other system you need to install 
PyInstaller:

```bash
pip install -U pyinstaller
```

Then you can run this command from project directory:

```bash
pyinstaller src/todo.py -y 
```


And the compiled version of the application will be ready into `dist` folder.



