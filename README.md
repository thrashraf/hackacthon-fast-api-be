# FastAPI MySQL Project

A FastAPI application with SQLAlchemy ORM and MySQL integration.

## Setup with Docker Compose

1. Build and start the containers:
```bash
docker compose up --build
```

This will:
- Start the FastAPI application at http://localhost:8000
- Start MySQL database
- Create necessary database and user
- Enable hot-reload for development

Changes to your code will be automatically reflected in the running application.

### Docker Development Commands

- Start the application:
```bash
docker compose up
```

- View logs:
```bash
docker compose logs -f
```

- Rebuild after changing dependencies:
```bash
docker compose up --build
```

- Stop all containers:
```bash
docker compose down
```

### Development Workflow

1. Make changes to your code
2. Changes will be automatically detected and reloaded
3. View the results in your browser at http://localhost:8000
4. Check logs for any errors using `docker compose logs -f`

### Troubleshooting

If you encounter database connection issues:
1. Ensure MySQL is healthy: `docker compose ps`
2. Check MySQL logs: `docker compose logs db`
3. Check app logs: `docker compose logs app`
4. Restart services: `docker compose restart`

## Manual Setup (without Docker)

1. Create a MySQL database:
```sql
CREATE DATABASE fastapi_db;
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
- Copy `.env.example` to `.env`
- Update the MySQL credentials in `.env`

4. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Available Endpoints

- `GET /`: Welcome message
- `POST /api/v1/users/`: Create a new user
- `GET /api/v1/users/`: List all users
- `GET /api/v1/users/{user_id}`: Get a specific user

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application initialization
│   ├── database.py       # Database configuration
│   ├── models/           # SQLAlchemy models
│   │   ├── __init__.py
│   │   └── base.py      # User model
│   ├── schemas/         # Pydantic schemas
│   │   └── __init__.py  # Data validation schemas
│   └── routes/          # API routes
│       └── __init__.py  # User routes
├── .env                 # Environment variables
├── .env.example        # Environment template
└── requirements.txt    # Project dependencies
