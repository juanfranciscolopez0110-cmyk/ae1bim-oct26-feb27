from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Base de datos SQLite local
engine = create_engine("sqlite:///clinicas_veterinarias.sqlite", echo=False)

# Fábrica de sesiones
Session = sessionmaker(bind=engine)