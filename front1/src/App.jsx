import { useState } from "react";
import SearchForm from "./components/SearchForm.jsx";
import ResultsList from "./components/ResultsList.jsx";
import { rechercher } from "./api.js";

export default function App() {
  const [chargement, setChargement] = useState(false);
  const [resultats, setResultats] = useState(null);
  const [demo, setDemo] = useState(false);

  async function lancerRecherche(parametres) {
    setChargement(true);
    const { donnees, demo } = await rechercher(parametres);
    setResultats(donnees);
    setDemo(demo);
    setChargement(false);
  }

  return (
    <main className="page">
      <header>
        <h1>Eco Trip 🌍✈️</h1>
        <p>Voyagez loin, pesez léger.</p>
      </header>

      <SearchForm onSubmit={lancerRecherche} chargement={chargement} />

      {demo && (
        <p className="bandeau">
          L'API n'est pas joignable : ce sont des données de démonstration.
        </p>
      )}

      {resultats && (
        <section className="colonnes">
          <ResultsList donnees={resultats.methode1} />
          <ResultsList donnees={resultats.methode2} />
        </section>
      )}

      {/* Le dashboard comparatif (Front 2) viendra ici. */}
    </main>
  );
}
