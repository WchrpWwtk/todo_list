# Django Todo List Assignment

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Description

This project is a Todo list application that allow users to create, read, update, delete

## Features

- Create new tasks with a title, description, and completion status.
- View a list of all tasks.
- View the details of a specific task.
- Update task details.
- Mark tasks as completed.
- Delete tasks.

## Getting started

### Prerequisites

- Python 3.x installed.
- Docker installed.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/WchrpWwtk/todo_list.git
2. Navigate to the project directory:
   ```bash
   cd todo_list
3. Build and run the Docker containers:
   ```bash
   docker compose up
   ```
   This command will start the Django application, the database defined in the `compose.yml` file.
4. Create a superuser account:
   ```bash
   docker compose exec server python manage.py createsuperuser
5. The Django application should now be running. You can access it at `http://localhost:8000`.

## Usage

### Web Interface

- Access the web-based user interface by opening your browser and going to `http://localhost:8000/`.

### API Endpoints

- The API endpoints are available at `http://localhost:8000/api/tasks/`.
  - `GET /api/tasks/`: List all tasks.
  - `POST /api/tasks/`: Create a new task.
  - `GET /api/tasks/<int:pk>/`: Retrieve a specific task.
  - `PUT /api/tasks/<int:pk>/`: Update a specific task.
  - `DELETE /api/tasks/<int:pk>/`: Delete a specific task.
