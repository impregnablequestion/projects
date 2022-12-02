DROP TABLE shifts;
DROP TABLE staff;

CREATE TABLE staff(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE shifts(
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    times VARCHAR(255),
    hours INT NOT NULL,
    day VARCHAR(255),
    staff_id INT NOT NULL REFERENCES staff(id)
);
