
from flask import Blueprint, jsonify

from database.connection import get_db_connection

# Création d'un groupe de routes consacré aux destinations
destinations_bp = Blueprint("destinations", __name__)


@destinations_bp.route("/api/destinations", methods=["GET"])
def get_destinations():
    """
    Récupère toutes les destinations enregistrées dans SQLite.
    """

    connection = get_db_connection()

    try:
        destinations = connection.execute(
            "SELECT * FROM destinations"
        ).fetchall()

        # Convertir les résultats SQLite en dictionnaires
        results = [dict(destination) for destination in destinations]

        return jsonify({
            "status": "success",
            "count": len(results),
            "data": results
        }), 200

    finally:
        connection.close()
