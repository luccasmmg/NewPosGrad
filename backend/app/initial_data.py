#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud.users import create_user
from app.db.crud.post_graduations import create_post_graduation
from app.schemas.base_schemas import UserCreate, PostGraduationCreate
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()

    create_post_graduation(
        db,
        PostGraduationCreate(
            id_unit=5679,
            name="Gestão Pública",
            initials="PPGP",
            sigaa_code=1672,
        )
    )

    create_user(
        db,
        UserCreate(
            email="admin@posgrad.com",
            password="123456",
            first_name="Luccas Mateus",
            last_name="Medeiros Gomes",
            is_active=True,
            is_superuser=True,
            owner_id=1,
        ),
    )

    create_user(
        db,
        UserCreate(
            email="teste@posgrad.com",
            password="123456",
            first_name="Teste",
            last_name="Teste 2",
            is_active=True,
            is_superuser=False,
            owner_id=1,
        ),
    )


if __name__ == "__main__":
    print("Creating superuser admin@posgrad.com")
    print("Creating normal user teste@posgrad.com")
    init()
    print("Superuser created")
    print("Normal user created")
