# Chat Project

This project is a chat application that uses WebSockets for real-time communication. Below are the steps to set up and run the project.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Migration](#database-migration)
- [Running the Django Development Server](#running-the-django-development-server)
- [Running the WebSocket Server](#running-the-websocket-server)
- [Accessing the Application APIs](#accessing-the-application-apis)
- [Architecture & Implementation Choices](#architecture--implementation-choices)

## Prerequisites

- Python 3.x
- Django
- Channels

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Thu-Min/chat_app_py.git
   cd chat_project
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

1. Run the initial migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Running the Django Development Server

1. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

## Running the WebSocket Server

1. Start the Channels development server:

   ```bash
   python -m daphne -b 127.0.0.1 -p 8000 chat_project.asgi:application
   ```

## Accessing the Application APIs

1. Open Postman and call APIs from this URL:

   ```
   http://127.0.0.1:8000/api/
   ```

## Architecture & Implementation Choices

### Architecture

The Chat Project follows a typical Django architecture with the addition of Django Channels to handle WebSocket connections for real-time communication. The architecture can be broken down into the following components:

1. **Django Application**: Handles HTTP requests, user authentication, and serves the main application.
2. **Django Channels**: Extends Django to handle WebSockets, enabling real-time communication.
3. **ASGI Server (Daphne)**: Serves as the interface between the Django application and the WebSocket connections.

### Implementation Choices

1. **Django**: Chosen for its robust framework, ease of use, and extensive documentation. It provides a solid foundation for building web applications.
2. **Django Channels**: Selected to add WebSocket support to the Django application, allowing for real-time features such as live chat.
3. **ASGI**: Adopted to support asynchronous communication, which is essential for handling WebSocket connections efficiently.

These choices ensure that the application is scalable, maintainable, and capable of handling real-time communication efficiently.
