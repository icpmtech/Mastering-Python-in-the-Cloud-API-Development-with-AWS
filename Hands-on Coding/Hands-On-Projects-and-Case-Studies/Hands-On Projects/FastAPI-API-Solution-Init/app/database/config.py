import os


TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": "fastapi_db", #os.environ.get("db_name"),
                "host": "127.0.0.1",
                "password": "Nl^mD-6gXc2B", #os.environ.get("postgres_password"),
                "port": 5432,
                "user": "admin", #os.environ.get("postgres_user"),
            },
        },
    },
    "apps": {
        "models": {
            "models": [
                "app.database.models", 
                "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}