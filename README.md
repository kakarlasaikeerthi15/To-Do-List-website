# To-Do-List-website
# To-Do List Application

## Overview

This project is a To-Do List application designed to help users manage their daily tasks efficiently. It is developed as application with a Python backend and a user-friendly frontend interface. The main goal is to provide a simple yet functional task management system.

## Purpose

Managing tasks is a fundamental part of productivity. This application aims to:

- Provide an easy-to-use interface for creating, updating, and deleting tasks.
- Allow users to mark tasks as complete or incomplete.
- Enable filtering of tasks based on their status.
- Persist data locally using JSON files to maintain tasks between sessions without the need for a complex database.

## Architecture

- *Backend:* The backend is built using Python, which handles task data management including CRUD (Create, Read, Update, Delete) operations. It reads from and writes to a JSON file to persist task data.
  
- *Frontend:* The frontend is developed with standard web technologies (HTML, CSS, JavaScript). It provides the user interface to interact with tasks, communicating with the backend to reflect changes in real time.

## Data Storage

Instead of using traditional relational databases, this application uses a JSON file to store tasks data. This approach simplifies data persistence and is suitable for lightweight applications or learning purposes.

Each task entry in the JSON file contains:

- A unique identifier (ID)
- Task description
- Completion status (true/false)

## Key Features

- Add new tasks with descriptive text.
- Edit existing tasks to update details.
- Delete tasks that are no longer needed.
- Mark tasks as completed or revert to incomplete.
- Filter tasks to view all, only completed, or only pending tasks.

## Benefits

- Lightweight and easy to deploy.
- Minimal setup with no dependency on external databases.
- Clear separation between backend logic and frontend presentation.
- Suitable as a learning project for development concepts.

## Future Enhancements

- User authentication to support multiple users.
- Use of a database system for scalable data management.
- Integration of task deadlines and reminders.
- Mobile-friendly responsive design improvements.


This project demonstrates practical implementation of CRUD operations, backend-frontend communication, and file-based data persistence using JSON, making it a valuable exercise  fundamentals.
