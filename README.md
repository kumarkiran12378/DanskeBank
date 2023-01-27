Danske Bank- Library API Powered by Django, DRF

Requirement:
    Python 3


Required packages installation steps:

    1. Install latest Python in your system
    2. Create Virtual Environment: python -m venv virtualenv_name
    3. Activate virtual Environment: source virtualenv_name/bin/activate(linux, mac)
    4. pip install -r requirements.txt

Set up is done to run Django server:
    Django Server run:  python manage.py runserver 8000


GET APIs:
    Listing Books: "http://localhost:8000/api/books/"
    Listing Authors: "http://localhost:8000/api/authors/"
    Listing Genre:  "http://localhost:8000/api/genres/"

POST APIs:
    To create User and Librarian:  "http://localhost:8000/api/users/"
    To Create Author: "http://localhost:8000/api/authors/"
    To Create book: "http://localhost:8000/api/books/"
    To Create genre:  "http://localhost:8000/api/genres/"
