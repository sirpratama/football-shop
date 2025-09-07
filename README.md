# Football Shop - Django Web Application

**Name:** Muhammad Rafi Nazir Pratama  
**Student ID:** 2406453556  
**Class:** KKI  

## 🌐 PWS Application Link
**Application URL:** [https://muhammad-rafi416-footballshop.pbp.cs.ui.ac.id](https://muhammad-rafi416-footballshop.pbp.cs.ui.ac.id)

---

## 📋 Checklist Implementation Step-by-Step

### 1. Creating a New Django Project
- Created project directory `football-shop`
- Ran `django-admin startproject football_shop .` to create Django project
- Configured virtual environment for dependency isolation

### 2. Creating `main` Application
- Ran `python manage.py startapp main` to create main application
- Added `'main'` to `INSTALLED_APPS` in `settings.py`

### 3. Project Routing Configuration
- Configured `football_shop/urls.py` to include main application URLs
- Added `path('', include('main.urls'))` to urlpatterns
- Created `main/urls.py` with routing to `show_main` view

### 4. Creating `FootballItem` Model
Created model with required attributes:
```python
class FootballItem(models.Model):
    name = models.CharField(max_length=255)           # Item name
    price = models.IntegerField()                     # Item price  
    description = models.TextField()                  # Item description
    thumbnail = models.URLField(max_length=500)       # Item image
    category = models.CharField(max_length=100)       # Item category
    is_featured = models.BooleanField(default=False)  # Featured status
    
    # Additional attributes
    brand = models.CharField(max_length=100, blank=True, null=True)
    stock = models.IntegerField(default=0)
    size = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 5. Creating Function in `views.py`
```python
def show_main(request):
    context = {
        'npm': '2406453556',
        'name': 'Muhammad Rafi Nazir Pratama',
        'class': 'KKI'
    }
    return render(request, "main.html", context)
```

### 6. Creating HTML Template
- Created `main/templates/` directory
- Created `main.html` with responsive design displaying application information
- Used Django template variables to display dynamic data

### 7. Database Migration
- Ran `python manage.py makemigrations` to create migration files
- Ran `python manage.py migrate` to apply migrations to database

### 8. PWS Deployment
- Configured `ALLOWED_HOSTS` with PWS domain
- Committed and pushed to PWS repository
- Accessed application through PWS URL

---

## 🔄 Django Request-Response Diagram

```
┌─────────────────┐    HTTP Request     ┌─────────────────┐
│                 │ ──────────────────► │                 │
│   CLIENT        │                     │  DJANGO SERVER  │
│   (Browser)     │ ◄────────────────── │                 │
└─────────────────┘    HTTP Response    └─────────────────┘
                                                │
                                                ▼
                                    ┌─────────────────┐
                                    │    urls.py      │
                                    │  (URL Routing)  │
                                    │                 │
                                    │ • Pattern match │
                                    │ • Route to view │
                                    └─────────────────┘
                                                │
                                                ▼
                                    ┌─────────────────┐
                                    │    views.py     │
                                    │ (Business Logic)│
                                    │                 │
                                    │ • Process req   │
                                    │ • Query models  │
                                    │ • Prepare data  │
                                    └─────────────────┘
                                                │
                                    ┌───────────┴───────────┐
                                    ▼                       ▼
                        ┌─────────────────┐    ┌─────────────────┐
                        │    models.py    │    │   template.html │
                        │   (Database)    │    │     (View)      │
                        │                 │    │                 │
                        │ • Data models   │    │ • HTML structure│
                        │ • ORM queries   │    │ • Template tags │
                        │ • Database ops  │    │ • Context data  │
                        └─────────────────┘    └─────────────────┘
```

### Component Relationship Explanation:

1. **urls.py**: Receives requests from client and determines which view will handle the request based on URL pattern
2. **views.py**: Executes business logic, interacts with models to fetch/manipulate data, and prepares context for template
3. **models.py**: Defines data structure and interacts with database through Django ORM
4. **template.html**: Receives context from views and renders HTML response sent back to client

---

## ⚙️ Role of `settings.py` in Django Project

`settings.py` is the central configuration file that manages all aspects of Django application:

### 1. **Database Configuration**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 2. **Installed Applications**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'main',
]
```

### 3. **Middleware Configuration**
- Manages middleware order that processes request/response
- Security, authentication, CORS, etc.

### 4. **Template Configuration**
- Manages template directories and template engine
- Context processors for global data

### 5. **Static Files & Media**
- Configuration for CSS, JavaScript, image files
- URLs and directories for static files

### 6. **Security Settings**
- `SECRET_KEY`: Secret key for cryptography
- `DEBUG`: Debug mode (True for development)
- `ALLOWED_HOSTS`: Domains allowed to access the application

### 7. **Internationalization**
- `LANGUAGE_CODE`: Default language
- `TIME_ZONE`: Time zone
- `USE_I18N`, `USE_TZ`: Internationalization settings

---

## 🗄️ How Database Migration Works in Django

### 1. **Migration Concept**
Migration is Django's way to apply model changes (database schema) to the database gradually and in a controlled manner.

### 2. **Migration Process**

#### **Step 1: Creating Migration**
```bash
python manage.py makemigrations
```
- Django compares current models with the last migration
- Creates new migration files in `app/migrations/`
- Files contain required operations (CREATE TABLE, ALTER TABLE, etc.)

#### **Step 2: Applying Migration**
```bash
python manage.py migrate
```
- Runs migration files that haven't been applied
- Changes database structure according to operations in migration files
- Records applied migrations in `django_migrations` table

### 3. **Migration System Benefits**
- **Version Control**: Every database change is recorded and trackable
- **Rollback**: Can revert to previous database versions
- **Team Collaboration**: Synchronizes database changes between developers
- **Deployment**: Automatically applies database changes in production

### 4. **Migration File**
Example migration file:
```python
# 0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    
    operations = [
        migrations.CreateModel(
            name='FootballItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
```

---

## 🤔 Why is Django Chosen for Initial Learning?

### 1. **"Batteries Included" Philosophy**
- Django provides almost everything needed for web development
- Admin interface, ORM, authentication, security features built-in
- Reduces setup and configuration complexity

### 2. **Clear and Organized Structure**
- **MVT Pattern**: Model-View-Template that's easy to understand
- **Project Structure**: Consistent and logical file organization
- **Convention over Configuration**: Reduces confusing decisions

### 3. **Friendly Learning Curve**
- Very comprehensive and high-quality documentation
- Informative and helpful error messages
- Official step-by-step tutorials that are easy to follow

### 4. **Fundamental Web Development Concepts**
Django teaches important concepts such as:
- **HTTP Request/Response cycle**
- **Database modeling and ORM**
- **Template rendering**
- **URL routing**
- **Security best practices**

### 5. **Real-World Ready**
- Used by major companies (Instagram, Pinterest, Mozilla)
- Production-ready features (caching, security, scalability)
- Teaches best practices applicable in industry

### 6. **Python Ecosystem**
- Python as a readable and beginner-friendly language
- Clean and expressive syntax
- Large community and extensive libraries

### 7. **Rapid Development**
- Built-in admin interface for CRUD operations
- Automatic form generation
- Database migrations
- Development server with auto-reload

---

## 💬 Feedback for Tutorial 1 Teaching Assistant

*No Feedback*

---
