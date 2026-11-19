from flask import Blueprint, jsonify, request
from backend.app.database.connection import get_db_connection

api_bp = Blueprint('api', __name__)

@api_bp.route('/recommandations', methods=['POST'])
def recommandations():
    data = request.get_json()
    # Ici, vous pouvez traiter les données reçues et générer des recommandations.
    # Pour l'instant, nous renvoyons simplement un exemple de réponse.
    response = {
        "methode2" : { 
        "temps_ms": 1.1,
        "message": None,
        "resultats": [
            { "nom": "Forêt de Fontainebleau", "region": "Île-de-France", "score": 0.41, "co2_kg": 0.4, "cout_eur": 169, "temps_h": 1, "transport": "train" },
            { "nom": "Lac du Der", "region": "Grand Est", "score": 0.3, "co2_kg": 1.4, "cout_eur": 150, "temps_h": 2.2, "transport": "train" },
            { "nom": "Gérardmer", "region": "Vosges", "score": 0.27, "co2_kg": 2.7, "cout_eur": 198, "temps_h": 3.7, "transport": "train" }
            ]
        }
    }
    return jsonify(response)

@api_bp.route("/destinations", methods=["GET"])
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
