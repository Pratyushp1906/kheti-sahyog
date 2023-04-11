**Kheti Sahyog**
Kheti Sahyog is a web application built using Django. The website is designed to help farmers by enabling them to rent their spare equipment to other farmers at reasonable rates and vice versa. Additionally, the website allows farmers to purchase new equipment from sellers.

*Getting Started*
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

*Prerequisites*
Python 3.6 or higher
Django 3.0 or higher
PostgreSQL or MySQL (optional)

*Installing*
1.Clone the repository

Create and activate a virtual environment

Install the required packages using the following command:

pip install -r requirements.txt

Set up the database by running the following command:

python manage.py migrate

Create a superuser account by running the following command:

python manage.py createsuperuser

Run the development server using the following command:

python manage.py runserver

The development server should now be accessible at http://localhost:8000/

*Configuration*
The following environment variables need to be set:

SECRET_KEY: Django secret key
DATABASE_URL: URL of the database

*Deployment*
The application can be deployed using a WSGI server such as gunicorn and a reverse proxy such as nginx or Apache.

*Built With*
Django - The web framework used
Bootstrap - The front-end framework used

*Authors*
Name - Kumar Sanskar , Saurabh Kumar Gupta , Pratyush Pandey , Adarsh Kumar

*License*
This project is licensed under the MIT License - see the LICENSE file for details.
