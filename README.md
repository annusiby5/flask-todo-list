# flask-todo-list

A simple and modern To-Do List web application built with Flask. This project allows users to add, complete, and delete tasks through an intuitive dark themed interface.

## Features

* Add new tasks
* Mark tasks as completed
* Delete tasks
* Modern dark UI
* Responsive design
* Lightweight and easy to understand
* Built using Flask, HTML, CSS, and Jinja2

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* Jinja2 Templates

## Project Structure

```text
flask-todo-list/
│
├── app.py
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
├── LICENSE
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-todo-list.git
cd flask-todo-list
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

## How It Works

* Enter a task and click **Add**.
* Check the checkbox to mark a task as completed.
* Click the delete button to remove a task.
* Tasks are stored in memory while the application is running.


## Future Improvements

* SQLite database integration
* Task persistence
* Edit existing tasks
* Due dates and priorities
* Search and filter functionality
* Light/Dark mode toggle
* User authentication


## License

This project is open source and available under the MIT License.
