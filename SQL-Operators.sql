-- 1) Create table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100),
    grade INT
);

-- 2) Insert sample data
INSERT INTO customers (customer_id, name, city, grade) VALUES
(1, 'Alice',   'New York', 120),
(2, 'Bob',     'Los Angeles',  90),
(3, 'Carol',   'New York',  95),
(4, 'David',   'Chicago',  150),
(5, 'Eve',     'Boston',   110),
(6, 'Frank',   'New York', 105);

-- 3) Customers from New York OR grade > 100
SELECT *
FROM customers
WHERE city = 'New York'
   OR grade > 100
ORDER BY customer_id;

-- 4) Customers from New York AND grade > 100
SELECT *
FROM customers
WHERE city = 'New York'
  AND grade > 100
ORDER BY customer_id;