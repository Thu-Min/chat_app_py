# Chat Project

This project is a chat application that uses WebSockets for real-time communication. Below are the steps to set up and run the project.

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

1. Open Postmand and call APIs from this url:
   ```
   http://127.0.0.1:8000/api/
   ```
