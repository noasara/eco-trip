
CREATE TABLE IF NOT EXISTS destinations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    description TEXT,
    carbon_kg REAL NOT NULL DEFAULT 0,
    estimated_price REAL NOT NULL DEFAULT 0,
    travel_time_hours REAL NOT NULL DEFAULT 0,
    activities TEXT
);
