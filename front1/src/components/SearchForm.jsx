import { useState } from "react";

const VILLES = ["Paris", "Lyon", "Lille", "Marseille"];

export default function SearchForm({ onSubmit, chargement }) {
  const [depart, setDepart] = useState("Paris");
  const [budget, setBudget] = useState(250);
  const [tempsMax, setTempsMax] = useState(4);
  const [texte, setTexte] = useState("");
  const [erreur, setErreur] = useState("");

  function envoyer(evenement) {
    evenement.preventDefault();
    // Vérifications simples avant d'appeler l'API
    if (Number(budget) <= 0) {
      setErreur("Le budget doit être supérieur à 0.");
      return;
    }
    if (Number(tempsMax) <= 0) {
      setErreur("Le temps de trajet doit être supérieur à 0.");
      return;
    }
    setErreur("");
    onSubmit({
      depart,
      budget: Number(budget),
      temps_max_h: Number(tempsMax),
      texte: texte.trim(),
    });
  }

  return (
    <form className="formulaire" onSubmit={envoyer}>
      <label>
        Ville de départ
        <select value={depart} onChange={(e) => setDepart(e.target.value)}>
          {VILLES.map((ville) => (
            <option key={ville}>{ville}</option>
          ))}
        </select>
      </label>

      <label>
        Budget max (€)
        <input type="number" min="0" value={budget} onChange={(e) => setBudget(e.target.value)} />
      </label>

      <label>
        Temps de trajet max (h)
        <input type="number" min="0" step="0.5" value={tempsMax} onChange={(e) => setTempsMax(e.target.value)} />
      </label>

      <label className="large">
        Tes envies (facultatif)
        <input
          type="text"
          placeholder="week-end calme en forêt près d'un lac"
          value={texte}
          onChange={(e) => setTexte(e.target.value)}
        />
      </label>

      {erreur && <p className="erreur large">{erreur}</p>}

      <button type="submit" disabled={chargement}>
        {chargement ? "Recherche..." : "Trouver mon voyage"}
      </button>
    </form>
  );
}
