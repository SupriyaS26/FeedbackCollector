# FeedbackCollector
A simple Flask app that collects anonymous feedback and stores it in a SQLite database.

## Features

- Submit anonymous feedback
- View all feedback in an admin view
- Export feedback as CSV

## Tech Stack

- Python + Flask
- SQLite
- HTML (Jinja2 templating)

## Setup Instructions

```bash
git clone https://github.com/SupriyaS26/FeedbackCollector.git
cd feedback-collector
python -m venv venv
venv\Scripts\activate    # On Windows
pip install -r requirements.txt
python app.py
Visit http://127.0.0.1:5000
