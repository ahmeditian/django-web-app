# Django Web App
A simple web application

### Software Pre-Requisites
- Miniconda or Anaconda

### Installation
1. Clone the Repo
```
git clone https://github.com/ahmeditian/django-web-app.git
```
2. Create Virtual Environment
```
  conda create --name <your_env_name> python=3.6
  conda activate <your_env_name>
```
3. Install the Dependency Packages inside Virtual Environment
```
  pip install -r requirements.txt
```
4. Migrate the SQL dependencies
```
  python manage.py migrate
  python manage.py makemigrations dappx
  python manage.py sqlmigrate dappx 0001
  python manage.py migrate
```
5. Run the Micro Service
```
  python manage.py runserver
```

### Sample Newsfeed 
![alt text](screenshots/newsfeed.PNG)
