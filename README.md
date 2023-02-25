# hire-app

Normal Style
To Run this app in your local environment 
1) pull the code to the folder you want to run the project "git clone https://github.com/a0123055u/hire-app.git"
2) to avoid mismatch of config use the venv folder given here 
3) to activate venv need to go to "cd venv/bin/"
4) set souce "source ./activate" 
5) go to recruitment_app "cd ../../recruitment_app/" then "pip install -r requirements.txt"
6) python manage.py runserver from recruitment_app folder


Prerequisite:
Python and pip package manager: https://packaging.python.org/en/latest/tutorials/installing-packages/



Docker Style 
sudo docker build --tag python-django-recruitment_app .
sudo docker run --publish 8000:8000 python-django-recruitment_app

Prerequisite:
Install Docker and Docker-Compose into the local machine where one want's to run.

http://127.0.0.1:8000/candidate/list/ #to view all candidate 
http://127.0.0.1:8000/candidate/recuritment/  #to add candidate
http://127.0.0.1:8000/candidate/list/{id}/update #to change status 
