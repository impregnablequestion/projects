DROP TABLE shifts;
DROP TABLE staff;

CREATE TABLE staff(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    min_hours REAL,
    max_hours REAL
);

CREATE TABLE shifts(
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    times VARCHAR(255),
    hours REAL,
    day VARCHAR(255),
    staff_id INT NOT NULL REFERENCES staff(id)
);
