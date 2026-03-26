CREATE TABLE supplier (
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO supplier (SNO, SNAME, STATUS, CITY) VALUES
('S1', 'Smith', 17, 'London'),
('S2', 'Jones', 15, 'Paris'),
('S3', 'Blake', 16, 'Paris'),
('S4', 'Clarke', 18, 'London'),
('S5', 'Adams', 17, 'Athens');

SELECT * FROM supplier;