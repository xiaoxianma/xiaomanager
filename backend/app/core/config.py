import os

PROJECT_NAME = "xiaomanager"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres@localhost/xiaomanager")

API_V1_STR = "/api/v1"
