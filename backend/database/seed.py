
from connection import get_db_connection


def seed_destinations():
    """
    Ajoute des destinations de test si la base est vide.
    """

    connection = get_db_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM destinations")
        count = cursor.fetchone()[0]

        if count > 0:
            print("La base contient déjà des destinations.")
            return

        destinations = [
            (
                "Porto", "Portugal", "Porto",
                "Ville connue pour ses ponts et son centre historique.",
                45.0, 180.0, 2.0,
                "Visite culturelle, gastronomie, promenade"
            ),
            (
                "Grenade", "Espagne", "Grenade",
                "Ville célèbre pour le palais de l'Alhambra.",
                38.0, 160.0, 3.0,
                "Monuments, randonnée, gastronomie"
            ),
            (
                "Lyon", "France", "Lyon",
                "Ville réputée pour son patrimoine et sa gastronomie.",
                25.0, 120.0, 2.0,
                "Musées, gastronomie, promenades"
            ),
            (
                "Amsterdam", "Pays-Bas", "Amsterdam",
                "Ville connue pour ses canaux et ses musées.",
                55.0, 220.0, 4.0,
                "Vélo, musées, canaux"
            ),
            (
                "Bruxelles", "Belgique", "Bruxelles",
                "Capitale européenne riche en histoire et en culture.",
                30.0, 130.0, 1.5,
                "Musées, architecture, gastronomie"
            )
        ]

        cursor.executemany("""
            INSERT INTO destinations (
                name, country, city, description,
                carbon_kg, estimated_price,
                travel_time_hours, activities
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, destinations)

        connection.commit()

        print("5 destinations ajoutées avec succès !")

    finally:
        connection.close()


if __name__ == "__main__":
    seed_destinations()

