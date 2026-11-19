import DestinationCard from "./DestinationCard.jsx";

export default function ResultsList({ donnees }) {
  return (
    <div className="colonne">
      <h2>{donnees.nom}</h2>
      <p className="temps">
        {donnees.resultats.length} résultat(s), calculé en {donnees.temps_ms} ms
      </p>
      {donnees.resultats.length === 0 ? (
        <p>{donnees.message || "Aucune destination ne correspond."}</p>
      ) : (
        donnees.resultats.map((destination) => (
          <DestinationCard key={destination.nom} destination={destination} />
        ))
      )}
    </div>
  );
}
