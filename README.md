# Yatube
Yandex educational project. Python Developer course (backend).
### Description
A blog which uses SQL-lite database and Django ORM for accessing it. The functions of registration, authorization and password change have been implemented, as well as creating your own page, adding posts with pictures, editing and deleting them, creating groups with posts, commenting and following other users. Display of posts of particular groups, authors the user follows, and user’s own posts in the feed has been enabled. Test coverage (Unittest) has been implemented.
### Social network for publishing personal diaries.
Users will be able to visit other people's pages, subscribe to authors and comment on their posts.
### Technologies
Python 3.7
Django 2.2.19
### Running a project in dev mode
- Clone the repository and go to it on the command line:
```
git clone git@github.com:nasttolm/api_final_yatube.git
```
cd yatube

- Install and activate the virtual environment

for Linux or macOS:
```
python3 -m venv venv
```
source venv/bin/activate

for Windows:
```
python3 -m venv env
```
source env/bin/activate

- Install dependencies from requirements.txt file
```
pip install -r requirements.txt

- Create a superuser:
```
python3 manage.py createsuperuser.

- In the folder with the manage.py file, run the command:
```
python3 manage.py runserver
```
### Authors
Anastasia Tolmacheva
