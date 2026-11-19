export default function DestinationCard({ destination }) {
  const { nom, co2_kg, cout_eur, temps_h, transport } = destination;
  return (
    <article className="carte">
      <h3>{nom}</h3>
      <ul>
        <li>CO₂ : {co2_kg} kg</li>
        <li>Prix estimé : {cout_eur} €</li>
        <li>Trajet : {temps_h} h ({transport})</li>
      </ul>
    </article>
  );
}
