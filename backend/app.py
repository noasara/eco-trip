from app import create_app
from app.models.Base import initialize_database

app = create_app()

if __name__ == "__main__":
    initialize_database()
    app.run(host="localhost", port=8000, debug=True)