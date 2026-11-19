// Le seul fichier qui parle au backend Flask.
// Si le format JSON change, on ne modifie que ce fichier.

const API_URL = import.meta.env.VITE_API_URL || "";

// Réponse attendue de POST /api/recommandations :
// {
//   methode1: { nom, temps_ms, resultats: [ { nom, region, score, co2_kg, cout_eur, temps_h, transport } ] },
//   methode2: { ...pareil, message }
// }

// Données de démonstration, utilisées tant que l'API n'est pas joignable.
const DONNEES_DEMO = {
  methode1: {
    nom: "Méthode 1 : les règles",
    temps_ms: 0.3,
    resultats: [
      { nom: "Lille", region: "Nord", score: 0.83, co2_kg: 1.6, cout_eur: 204, temps_h: 2.4, transport: "train" },
      { nom: "Rouen", region: "Normandie", score: 0.8, co2_kg: 0.9, cout_eur: 169, temps_h: 1.5, transport: "train" },
      { nom: "Lac du Der", region: "Grand Est", score: 0.8, co2_kg: 1.4, cout_eur: 150, temps_h: 2.2, transport: "train" },
    ],
  },
  methode2: {
    nom: "Méthode 2 : le sens du texte",
    temps_ms: 1.1,
    message: null,
    resultats: [
      { nom: "Forêt de Fontainebleau", region: "Île-de-France", score: 0.41, co2_kg: 0.4, cout_eur: 169, temps_h: 1, transport: "train" },
      { nom: "Lac du Der", region: "Grand Est", score: 0.3, co2_kg: 1.4, cout_eur: 150, temps_h: 2.2, transport: "train" },
      { nom: "Gérardmer", region: "Vosges", score: 0.27, co2_kg: 2.7, cout_eur: 198, temps_h: 3.7, transport: "train" },
    ],
  },
};

export async function rechercher(parametres) {
  try {
    const reponse = await fetch(`${API_URL}/api/recommandations`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(parametres),
    });
    if (!reponse.ok) throw new Error(`Erreur ${reponse.status}`);
    return { donnees: await reponse.json(), demo: false };
  } catch (erreur) {
    console.warn("API indisponible, données de démonstration :", erreur.message);
    return { donnees: DONNEES_DEMO, demo: true };
  }
}
