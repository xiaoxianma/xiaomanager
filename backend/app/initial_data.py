#!/usr/bin/env python3
import sys

sys.path.insert(0, ".")

from app.db.crud.user import create_user
from app.db.schemas.user import UserCreate
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="admin@xiaomanager.com",
            password="123456",
            is_active=True,
            is_superuser=True,
        ),
    )


if __name__ == "__main__":
    print("Creating superuser admin@xiaomanager.com")
    init()
    print("Superuser created")
