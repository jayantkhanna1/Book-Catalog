# Django Book Catalog Application

This is a simple book catalog application built with Django. It allows users to search for books by ISBN, and save them to a personal collection. The application also includes user authentication and authorization features, with passwords hashed for security.

## Requirements

- Python 3.x
- Django 3.x

## Installation

1. Clone the repository: `git clone https://github.com/jayantkhanna1/Book-Catalog.git`
2. Install virtualenv: `pip install virtualenv`
3. Create a virtual environment: `python -m venv ve`
4. Activate the virtual environment: `.\ve\Scripts\activate` . For Linux/MacOS, use `source ve/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the database migrations: `python manage.py makemigrations`
6. Migrate database: `python manage.py migrate`
8. Create a superuser account (optional): `python manage.py createsuperuser`
9. Start the development server: `python manage.py runserver`
10. To access the admin panel, first create a superuser account (see step 8). Then, navigate to http://localhost:8000/admin/ in a web browser and log in with your superuser account.


## Usage

1. Navigate to http://localhost:8000/ in a web browser
2. Log in with an existing account. If no accounts exist, create a new account by going to http://localhost:8000/admin/ and creating a new user with SHA-512 hased password
3. To search for a book in your collection enter any string matching with that books name or author in the search bar on the homepage
3. To search for a new book, Click on new book, enter an ISBN in the search bar and press Enter
5. Click the "Add" button to add the book to your personal collection
6. To remove a book from your collection, click the "Remove" button. (Looks like a dustbin)
7. To Logout, click the "Logout" button on the top right corner of the page.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
