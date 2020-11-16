## Managed by python 2.7 venv

### django modules required are already installed in venv
### activate venv by
- `source fyp/bin/activate` from root of this repo
### database used is postgres

to install
 - `pip install -r requirement_file.txt`
 - `brew install postgres`
 - `psql postgres`
 - `CREATE ROLE user WITH LOGIN PASSWORD pass;`
 - `create database cricket_analytics;`
 - `GRANT ALL PRIVILEGES ON DATABASE cricket_analytics TO sheikhhamza012;`
 - in `cricket_analytics/cricket_analytics/settings` change username password for postgres to you own, find "database" in file

### server related work will be in 
` cd cricket_analytics`
### django app means a model 
 - to create `python manage.py startapp appname` creates the folder with mvc files other files can be made too
 - create `urls.py` in folder of this model
 - follow the practice of keeping routes of model in its folder and inculding it in main urls file i-e `cricket_analytics/urls.py`
 - then make it discoverable by adding it in `cricket_analytics/settings` find `installed_apps`

### user authentication is done 
- by python.contrib.authentication it has super user too 
- read about it https://docs.djangoproject.com/en/3.1/topics/auth/default/. 

### after creating app(model) 
- to add field add in model file than run `python manage.py makemigrations`
- then `python manage.py migrate`
- `views` has controller logic 
### run server
- `python manage.py runserver` on http://localhost:8000

### debugging with breakpoint 
 - `import pdb pdb.set_trace() ` add this line anywhere in code

### more reference?
- here is a basic implementation https://github.com/sheikhhamza012/djando_freelance_assignment/
