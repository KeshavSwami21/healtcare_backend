
# 🩺 Healthcare Backend API

## 📄 Project Description

The **Healthcare Backend API** is a secure, scalable, and modular REST API backend built using **Django, Django REST Framework, PostgreSQL, and JWT Authentication**. Designed for healthcare management, it enables:

* User registration and secure login with JWT tokens.
* Authenticated CRUD operations for managing patient and doctor records.
* Patient-doctor mapping to efficiently assign doctors to patients.
* Clean API design following REST principles for seamless frontend or mobile integration.
* Fully documented interactive API exploration using Swagger and ReDoc.
* Dockerized deployment for consistent development and production environments.

This project is ideal for learning, portfolio enhancement, and as a foundation for full-scale healthcare applications requiring a secure, clean, and maintainable backend structure.

---

### 🚀 **Tech Stack & Features**

| 🛠️ **Feature** | **Details** |
|---|---|
| 🖥️ **Backend Framework** | [**Django**](https://www.djangoproject.com/) – A high-level, secure, and scalable Python web framework for rapid backend development |
| ⚙️ **API Layer** | [**Django REST Framework (DRF)**](https://www.django-rest-framework.org/) – Used to build flexible, browsable RESTful APIs |
| 🗄️ **Database** | [**PostgreSQL**](https://www.postgresql.org/) – A reliable, production-grade relational database for structured data |
| 🔐 **Authentication** | JWT-based authentication using `djangorestframework-simplejwt` for secure, stateless, token-based authentication and route protection |
| 📄 **API Documentation** | Integrated **Swagger UI** and **ReDoc** with [`drf-yasg`](https://github.com/axnsan12/drf-yasg) for interactive, auto-generated API documentation and testing |
| 🐳 **Containerization** | **Docker** and **Docker Compose** for consistent local development and scalable production deployment |
| 🚦 **Project Structure** | Clean, scalable Django app layout following **modular best practices** for maintainability |
| 🩺 **Healthcare APIs** | Endpoints for **user registration, login, patient management, doctor management, and patient-doctor mapping** with user-specific access control |
| 🚀 **Production Ready** | Easily deployable on **Render, Railway, AWS, and DigitalOcean**, supporting environment-based configuration for secure deployments |

---

### ✨ **What This Project Provides**

✅ A **secure, scalable REST API backend** for a **Healthcare Application**  
✅ User registration and **JWT-based login/logout** for secure authentication  
✅ Manage **patients** (CRUD, user-specific data)  
✅ Manage **doctors** (CRUD, accessible globally)  
✅ **Assign/unassign doctors to patients** with mapping APIs  
✅ **Interactive API documentation** via Swagger and ReDoc for testing and exploration  
✅ **Dockerized workflow** for seamless local development, CI/CD, and production deployments  
✅ Integrated with **PostgreSQL** for scalable, durable data storage

---

## 📂 Project Structure

```
healthcare-backend/
│
├── api/   # Main Django app for the healthcare backend
│ ├── migrations/   # Database migration files
│ ├── init.py   # Marks the directory as a Python package
│ ├── admin.py  # Admin panel configurations for models
│ ├── apps.py   # App configuration
│ ├── models.py     # Django ORM models for Patient, Doctor, Mapping
│ ├── serializers.py    # DRF serializers to convert model instances to JSON
│ ├── views.py  # API views and logic using DRF generic views
│ ├── urls.py   # App-specific URL routing
│ └── tests.py  # Unit and integration tests (to be implemented)
│
├── healthcare/     # Django project configuration
│ ├── init.py   # Marks the directory as a Python package
│ ├── asgi.py   # ASGI entry point for asynchronous deployments
│ ├── settings.py   # Project-wide settings and configurations
│ ├── urls.py   # Root URL routing, includes app URLs and Swagger
│ └── wsgi.py   # WSGI entry point for production servers like Gunicorn
│
├── Dockerfile  # Instructions for building the backend Docker image
├── docker-compose.yml  # Multi-container orchestration (Django + PostgreSQL)
├── requirements.txt    # List of Python dependencies for the project
├── .env    # Environment variables (SECRET_KEY, DB configs, etc.)
├── manage.py   # Django CLI utility for migrations, server, shell
└── README.md   # Project documentation and usage instructions
```

---

## 🚀 Local Development Setup Guide for Healthcare Backend

Follow these **step-by-step instructions** to set up and run your **Django Healthcare Backend** locally:

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/healthcare-backend.git
cd healthcare-backend
```

Replace `yourusername` with your actual GitHub username.

---

### 2️⃣ Create and Activate a Virtual Environment

Create a virtual environment to isolate dependencies:

```bash
python -m venv venv
```

Activate the environment:

* **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```
* **Windows:**

  ```bash
  venv\Scripts\activate
  ```

You should see `(venv)` in your terminal prompt.

---

### 3️⃣ Install Dependencies

Upgrade `pip` and install all dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your_django_secret_key
DEBUG=True

DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432
```

✅ Replace `your_django_secret_key` with a generated secret key:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
<b> NOTE: Ensure your PostgreSQL database and user are created with matching credentials. </b>


## 🗄️ Installing PostgreSQL

### ✅ Using Official Installer

Download and install PostgreSQL using the official guides:

* **Windows:** [PostgreSQL Windows Installer](https://www.postgresql.org/download/windows/)
* **Linux:** [PostgreSQL Linux Download](https://www.postgresql.org/download/linux/)

Follow the installer instructions and set a password for the `postgres` user during setup. Remember this password, as you will need it to configure your project database.

---

## ⚙️ Setting Up PostgreSQL Database for This Project

1️⃣ Open **pgAdmin** or your preferred PostgreSQL client.

2️⃣ Create a new database:

* Name: `healthcare_db`
* Owner: `postgres` (or the user you configured)

3️⃣ (Optional) Create a dedicated user:

```sql
CREATE USER healthcare_user WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO healthcare_user;
```

4️⃣ Update your `.env` file in the project root:

```
DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432
```

Your PostgreSQL database is now ready to use with your Healthcare Backend project.

---

### 5️⃣ Apply Database Migrations

Apply initial migrations to set up database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Create a Superuser (Optional)

Create a superuser for accessing Django admin:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin username, email, and password.
<b>NOTE: Superuser account in needed in order to access the API documentation through SWAGGER and REDOC.</b>

---

### 7️⃣ Run the Development Server

Start your Django server:

```bash
python manage.py runserver
```

Access your API at: [http://localhost:8000](http://localhost:8000)

---

### 8️⃣ Access Interactive API Documentation

After starting the server, view your live API docs:

* **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
* **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

✅ Use these to test your endpoints and view payload structures interactively.

---

### ✅ Next Steps

* Register and log in using the API to get your JWT token.
* Use the token in headers to test protected endpoints:

  ```
  Authorization: Bearer <your_access_token>
  ```
* Optionally, test with Postman or Swagger before connecting to a frontend or mobile app.

---

## 🐳 Docker Deployment Guide for Healthcare Backend

Ensure **Docker** and **Docker Compose** are installed on your system before proceeding.

---

### 1️⃣ Build and Run Containers

Build your Docker images and start your services using:

```bash
docker-compose up --build
```

This will:

* Build your Django application container based on the `Dockerfile`.
* Pull the PostgreSQL image and initialize the database service.
* Start and link the containers with environment variables defined in your `docker-compose.yml`.

---

### 2️⃣ Verify Running Containers

Check the running containers:

```bash
docker ps
```

You should see containers for `web` (Django) and `db` (PostgreSQL) running.

---

### 3️⃣ API and Database Access

Once running, your services will be available at:

* **Backend API:** [http://localhost:8000](http://localhost:8000)
* **Swagger Docs:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
* **ReDoc Docs:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
* **PostgreSQL:** Accessible on `localhost:5432` for GUI clients like DBeaver, TablePlus, or pgAdmin using the credentials provided in your `.env` or `docker-compose.yml`.

---

### 4️⃣ Common Docker Commands

* **Stop containers without removing:**

  ```bash
  docker-compose stop
  ```

* **Stop and remove containers, networks, volumes:**

  ```bash
  docker-compose down
  ```

* **View logs for all services:**

  ```bash
  docker-compose logs -f
  ```

---

## 📡 API Endpoints

### 🔑 Authentication
- `POST /api/auth/register/` — Register user
- `POST /api/auth/login/` — Login and receive JWT token

### 🩺 Patient Management
- `POST /api/patients/` — Add new patient
- `GET /api/patients/` — Retrieve all user-created patients
- `GET /api/patients/<id>/` — Retrieve specific patient
- `PUT /api/patients/<id>/` — Update patient
- `DELETE /api/patients/<id>/` — Delete patient

### 👨‍⚕️ Doctor Management
- `POST /api/doctors/` — Add new doctor
- `GET /api/doctors/` — Retrieve all doctors
- `GET /api/doctors/<id>/` — Retrieve specific doctor
- `PUT /api/doctors/<id>/` — Update doctor
- `DELETE /api/doctors/<id>/` — Delete doctor

### 🔗 Patient-Doctor Mapping
- `POST /api/appointments/` — Assign doctor to patient
- `GET /api/appointments/` — Retrieve all mappings
- `GET /api/appointments/<patient_id>/` — Retrieve mappings for a patient
- `DELETE /api/appointments/<id>/` — Remove doctor from patient

---

## 📖 API Documentation

Interactive API documentation is available:

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## 🧪 Testing the API (Detailed)

Use **Postman**, **Swagger UI**, or **cURL** to test your Healthcare Backend API securely and systematically.

### 🔑 1️⃣ Register a User

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "email": "test@example.com", "password": "TestPassword123"}'
```

### 🔐 2️⃣ Get JWT Token (Login)

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "TestPassword123"}'
```

This returns your `access` and `refresh` tokens:

```json
{
  "access": "<your_access_token>",
  "refresh": "<your_refresh_token>"
}
```

### 🛡️ 3️⃣ Use JWT Token in Headers

For authenticated requests, add:

```
Authorization: Bearer <your_access_token>
```

### 🩺 4️⃣ Example Authenticated API Endpoints

✅ **Patients:**

* Create: `POST /api/patients/`
* List: `GET /api/patients/`

✅ **Doctors:**

* Create: `POST /api/doctors/`
* List: `GET /api/doctors/`

✅ **Patient-Doctor Mapping:**

* Assign: `POST /api/appointments/`
* List: `GET /api/appointments/`

### 🧩 5️⃣ Using the Provided Postman Collection

* Import the `Postman.Json` collection provided.
* Set `base_url` as `http://127.0.0.1:8000/api` or  `http://0.0.0.0:8000/api` or `loacalhost:8000/api`.
* Register and login to get your `jwt_token`.
* Use `{{jwt_token}}` in authorization headers for all protected routes.
* Test **create, list, and mapping assignments** directly from Postman for structured validation.

---

## 🚀 Next Planned Enhancements

✅ **Rate Limiting:** Secure login and sensitive endpoints against brute-force attacks.

✅ **Email Verification:** Enforce email confirmation during registration for additional security.

✅ **Unit & Integration Tests:** Automate validation of endpoints using Django TestCase and Pytest.

✅ **CI/CD Pipeline:** Automate linting, testing, and deployments to Render, Railway, or AWS.

✅ **Production Deployment Optimization:** With environment-based Docker builds and automatic migrations.

---

## 🚀 Next Planned Enhancements

✅ Rate Limiting: Secure login and sensitive endpoints against brute-force attacks.

✅ Email Verification: Enforce email confirmation during registration for additional security.

✅ Unit & Integration Tests: Automate validation of endpoints using Django TestCase and Pytest.

✅ CI/CD Pipeline: Automate linting, testing, and deployments to Render, Railway, or AWS.

✅ Production Deployment Optimization: With environment-based Docker builds and automatic migrations.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ✉️ Contact

For questions, support, or collaboration:

- **Email:** keshavswami2112@gmail.com
- **LinkedIn:** [keshavswami21](https://linkedin.com/in/keshavswami21)
- **GitHub:** [KeshavSwami21](https://github.com/KeshavSwami21)

---
