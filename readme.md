# Note Place for Students

## Overview

This platform serves as a note-sharing hub where students can easily share and find study materials. Built with Django and tailored with Tailwind CSS for styling, it creates an engaging and user-friendly interface for education-focused content exchange.

## Features

- User authentication system for secure access.
- Ability to upload and share notes.
- Advanced search functionality with filters to easily find specific notes.
- Direct messaging system for users to communicate.
- Responsive design using Tailwind CSS for a great experience on any device.

## Technologies

- **Frontend:** HTML, Tailwind CSS
- **Backend:** Django with essential dependencies like forms, authentication, etc.
- **Hosting:** AWS EC2 (Ubuntu)
- **Database:** SQL (SQLite/PostgreSQL/MySQL)

## Running the Project on AWS EC2 (Ubuntu)

## Usage

- To upload or search for notes, create an account or log in.
- Use the search bar to filter notes by subject, title, or content.
- To send a message, navigate to a user's profile and click on the message button.

### Prerequisites

- An AWS account
- A running EC2 instance with Ubuntu
- Python 3.8+
- pip
- Virtualenv (recommended)

### Setup and Deployment

1. Connect to your EC2 instance using SSH:

2. Clone the repository onto your EC2 instance:
    git clone [repository URL]

3. Navigate to the project directory:
    cd note-place-for-students

4. Activate the virtual environment:
    source venv/bin/activate

5. Install the project dependencies:
    pip install -r requirements.txt

6. Perform database migrations:
    python manage.py makemigrations
    python manage.py migrate

7. Run the server:
    python manage.py runserver your_ip:8000