This repository has two Django projects:

- **django_tutorial**: includes a database and admin panel
- **django_last_fm**: does not require database setup

1. **Clone the repository**
```bash
   git clone <repository-url>
   cd <repository-name>
```
2. **Move into the project you want to run**
```bash
   cd django_tutorial
   # or
   cd django_last_fm
```
3. **(Optional) Create and activate a virtual environment**

5. **Install dependencies**
```bash
   pip install -r requirements.txt
```
5. **Apply database migrations** *(django_tutorial only)*
```bash
   python manage.py migrate
```
6. **Create an admin user** *(django_tutorial only, needed to access `/admin`)*
```bash
   python manage.py createsuperuser
```
7. **Start the development server**
```bash
   python manage.py runserver
```
Then you can go to http://127.0.0.1:8000/
