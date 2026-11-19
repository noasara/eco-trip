from app import create_app
from database.connection import initialize_database
from routes.destinations import destinations_bp

app = create_app()
app.register_blueprint(destinations_bp)

if __name__ == "__main__":
    initialize_database()
    app.run(host="localhost", port=8000, debug=True)