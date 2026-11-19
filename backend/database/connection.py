
import sqlite3
from pathlib import Path

# Chemin du dossier database
DATABASE_DIR = Path(__file__).resolve().parent

# Chemin du fichier de base de données
DATABASE_PATH = DATABASE_DIR / "ecotrip.db"


def get_db_connection():
    """
    Ouvre une connexion à la base de données SQLite.
    """
    connection = sqlite3.connect(DATABASE_PATH)

    # Permet de récupérer les résultats sous forme de dictionnaires
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Crée les tables à partir du fichier schema.sql.
    """
    schema_path = DATABASE_DIR / "schema.sql"

    connection = get_db_connection()

    with open(schema_path, "r", encoding="utf-8") as file:
        schema = file.read()

    connection.executescript(schema)
    connection.commit()
    connection.close()
