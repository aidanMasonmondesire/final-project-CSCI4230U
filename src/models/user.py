from __future__ import annotations
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # Assuming db is initialized in models/__init__.py

class User(db.Model):
    # Assuming your model fields are declared like this
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    favourite_name = db.Column(db.String(80), nullable=True)
    favourite_types = db.Column(db.String(255), nullable=True)  # Store as comma-separated string
    favourite_sprite = db.Column(db.String(255), nullable=True)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def get_favourite_name(self) -> str:
        """Get the name of the favorite Pokémon."""
        return self.favourite_name

    def set_favourite_name(self, name: str) -> None:
        """Set the name of the favorite Pokémon."""
        self.favourite_name = name

    def get_favourite_types(self) -> list:
        """Get the types of the favorite Pokémon as a list."""
        return self.favourite_types.split(',') if self.favourite_types else []

    def set_favourite_types(self, types: list) -> None:
        """Set the types of the favorite Pokémon (expects a list)."""
        if types is None:
            self.favourite_types = ''
        else:
            # Ensure all elements are strings
            self.favourite_types = ','.join(str(t) for t in types)


    def get_favourite_sprite(self) -> str:
        """Get the sprite of the favorite Pokémon."""
        return self.favourite_sprite

    def set_favourite_sprite(self, sprite: str) -> None:
        """Set the sprite of the favorite Pokémon."""
        self.favourite_sprite = sprite
