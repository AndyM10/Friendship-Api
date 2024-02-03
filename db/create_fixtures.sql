CREATE TABLE IF NOT EXISTS friends (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location POINT,
    friends INTEGER[]
);
