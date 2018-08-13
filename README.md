# Scraping from dineout website
https://www.dineout.co.in/bangalore-restaurants


This application uses django 1.11.14, python 3 and Beautiful Soup 4.

Installing django 1.11 on Linux
> Install Python 3

> Set up virtualenv and install Django
$ python3 -m venv myvenv
$ source myvenv/bin/activate

$ python3 -m pip install --upgrade pip
$ pip install django==1.11


Installing Beautiful Soup
$ pip install beautifulsoup4


Running the app 'restaurant'
$ python manage.py runserver

Run application 'restaurant' on your web browser at URL `http://127.0.0.1:8000`. This is the default port unless you change that manually.



Note: 
1. Python script for web scraping is written at /dineout/views.py
2. HTML page for Frontend is at /dineout/templates/dineout/dineout_list.html