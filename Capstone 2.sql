-- Customer and Product Database for Harish's Company
-- This database contains comprehensive customer information, products, and export details

-- Create customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    customer_type VARCHAR(20),
    credit_limit DECIMAL(10,2),
    status VARCHAR(20) DEFAULT 'Active'
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2),
    stock_quantity INT,
    supplier VARCHAR(100),
    description TEXT
);

-- Create exports table (linking customers, products, and export countries)
CREATE TABLE IF NOT EXISTS exports (
    export_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    export_country VARCHAR(50),
    quantity INT,
    export_date DATE,
    total_value DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample customer data
INSERT INTO customers (customer_id, customer_name, contact_person, email, phone, city, state, country, customer_type, credit_limit, status) VALUES
(1, 'Apple Inc.', 'Tim Cook', 'tim.cook@apple.com', '+1-408-996-1010', 'Cupertino', 'CA', 'USA', 'Corporate', 5000000.00, 'Active'),
(2, 'Amazon Corp', 'Andy Jassy', 'andy.jassy@amazon.com', '+1-206-266-1000', 'Seattle', 'WA', 'USA', 'Corporate', 3000000.00, 'Active'),
(3, 'Microsoft Corporation', 'Satya Nadella', 'satya@microsoft.com', '+1-425-882-8080', 'Redmond', 'WA', 'USA', 'Corporate', 4000000.00, 'Active'),
(4, 'Alphabet Inc.', 'Sundar Pichai', 'sundar@alphabet.com', '+1-650-253-0000', 'Mountain View', 'CA', 'USA', 'Corporate', 3500000.00, 'Active'),
(5, 'Oracle Corporation', 'Safra Catz', 'safra@oracle.com', '+1-650-506-7000', 'Austin', 'TX', 'USA', 'Corporate', 2500000.00, 'Active'),
(6, 'Adobe Systems', 'Shantanu Narayen', 'shantanu@adobe.com', '+1-408-536-6000', 'San Jose', 'CA', 'USA', 'Corporate', 2000000.00, 'Active'),
(7, 'Cisco Systems', 'Chuck Robbins', 'chuck@cisco.com', '+1-408-526-4000', 'San Jose', 'CA', 'USA', 'Corporate', 1800000.00, 'Active'),
(8, 'Intel Corporation', 'Pat Gelsinger', 'pat@intel.com', '+1-408-765-8080', 'Santa Clara', 'CA', 'USA', 'Corporate', 2200000.00, 'Active'),
(9, 'NVIDIA Corporation', 'Jensen Huang', 'jensen@nvidia.com', '+1-408-486-2000', 'Santa Clara', 'CA', 'USA', 'Corporate', 2800000.00, 'Active'),
(10, 'Qualcomm Inc.', 'Cristiano Amon', 'cristiano@qualcomm.com', '+1-858-587-1121', 'San Diego', 'CA', 'USA', 'Corporate', 1500000.00, 'Active'),
(11, 'Tesla Inc.', 'Elon Musk', 'elon@tesla.com', '+1-650-681-5000', 'Austin', 'TX', 'USA', 'Corporate', 3200000.00, 'Active'),
(12, 'Meta Platforms', 'Mark Zuckerberg', 'mark@meta.com', '+1-650-543-4800', 'Menlo Park', 'CA', 'USA', 'Corporate', 3800000.00, 'Active'),
(13, 'Netflix Inc.', 'Ted Sarandos', 'ted@netflix.com', '+1-408-540-3700', 'Los Gatos', 'CA', 'USA', 'Corporate', 1200000.00, 'Active'),
(14, 'PayPal Holdings', 'Dan Schulman', 'dan@paypal.com', '+1-402-935-2050', 'San Jose', 'CA', 'USA', 'Corporate', 1600000.00, 'Active'),
(15, 'eBay Inc.', 'Jamie Iannone', 'jamie@ebay.com', '+1-408-376-7400', 'San Jose', 'CA', 'USA', 'Corporate', 1400000.00, 'Active');

-- Insert sample product data
INSERT INTO products (product_id, product_name, category, unit_price, stock_quantity, supplier, description) VALUES
(1, 'Wireless Router', 'Networking', 299.99, 500, 'Cisco Systems', 'High-speed wireless router for enterprise use'),
(2, 'Graphics Card GTX 3080', 'Hardware', 699.99, 200, 'NVIDIA', 'High-performance graphics card for gaming and AI'),
(3, 'SSD 1TB', 'Storage', 149.99, 1000, 'Samsung', 'Fast solid-state drive for data storage'),
(4, 'Laptop Core i7', 'Computers', 1299.99, 300, 'Dell', 'Business laptop with Intel Core i7 processor'),
(5, 'Smartphone Pro', 'Mobile', 999.99, 800, 'Apple', 'Latest smartphone with advanced features'),
(6, 'Cloud Server License', 'Software', 499.99, 1500, 'Microsoft', 'Annual license for cloud server access'),
(7, 'Security Software Suite', 'Software', 299.99, 600, 'Symantec', 'Comprehensive cybersecurity solution'),
(8, 'Database Management System', 'Software', 999.99, 400, 'Oracle', 'Enterprise database management system'),
(9, 'Video Editing Software', 'Software', 599.99, 350, 'Adobe', 'Professional video editing and production suite'),
(10, 'IoT Sensors', 'Electronics', 49.99, 2000, 'Texas Instruments', 'Smart sensors for IoT applications'),
(11, 'Solar Panels', 'Energy', 399.99, 150, 'Tesla', 'High-efficiency solar panels for renewable energy'),
(12, 'Payment Gateway API', 'Software', 199.99, 800, 'PayPal', 'Secure payment processing API'),
(13, 'Streaming Platform License', 'Software', 799.99, 250, 'Netflix', 'Annual license for streaming platform'),
(14, 'AI Development Kit', 'Hardware', 299.99, 400, 'NVIDIA', 'Development kit for AI and machine learning'),
(15, 'E-commerce Platform', 'Software', 699.99, 300, 'eBay', 'Complete e-commerce solution platform');

-- Insert sample export data
INSERT INTO exports (export_id, customer_id, product_id, export_country, quantity, export_date, total_value) VALUES
(1, 1, 5, 'China', 1000, '2024-01-15', 999990.00),
(2, 1, 5, 'Japan', 500, '2024-02-20', 499995.00),
(3, 2, 12, 'India', 200, '2024-01-10', 39998.00),
(4, 2, 12, 'Brazil', 150, '2024-03-05', 29998.50),
(5, 3, 6, 'Germany', 300, '2024-02-15', 149997.00),
(6, 3, 6, 'France', 250, '2024-03-10', 124997.50),
(7, 4, 9, 'United Kingdom', 100, '2024-01-25', 59999.00),
(8, 4, 9, 'Australia', 80, '2024-02-28', 47999.20),
(9, 5, 8, 'Canada', 50, '2024-03-01', 49999.50),
(10, 5, 8, 'Mexico', 75, '2024-03-15', 74999.25),
(11, 6, 9, 'South Korea', 120, '2024-01-30', 71998.80),
(12, 6, 9, 'Singapore', 90, '2024-02-25', 53999.10),
(13, 7, 1, 'Netherlands', 200, '2024-02-10', 59998.00),
(14, 7, 1, 'Sweden', 150, '2024-03-08', 44998.50),
(15, 8, 2, 'Taiwan', 100, '2024-01-20', 69999.00),
(16, 8, 2, 'Malaysia', 80, '2024-02-15', 55999.20),
(17, 9, 2, 'Thailand', 120, '2024-03-01', 83998.80),
(18, 9, 14, 'Vietnam', 150, '2024-03-10', 44998.50),
(19, 10, 10, 'Israel', 500, '2024-02-05', 24999.50),
(20, 10, 10, 'UAE', 300, '2024-03-12', 14999.70),
(21, 11, 11, 'Norway', 200, '2024-01-18', 79998.00),
(22, 11, 11, 'Denmark', 150, '2024-02-22', 59998.50),
(23, 12, 13, 'Ireland', 80, '2024-03-05', 63999.20),
(24, 12, 13, 'Portugal', 60, '2024-03-18', 47999.40),
(25, 13, 13, 'New Zealand', 50, '2024-02-08', 39999.50),
(26, 13, 13, 'South Africa', 40, '2024-03-02', 31999.60),
(27, 14, 12, 'Switzerland', 100, '2024-01-28', 19999.00),
(28, 14, 12, 'Austria', 80, '2024-02-20', 15999.20),
(29, 15, 15, 'Finland', 70, '2024-03-08', 48999.30),
(30, 15, 15, 'Poland', 60, '2024-03-20', 41999.40);

-- Useful queries for Harish

-- 1. Customers whose name starts with 'A'
SELECT customer_id, customer_name, contact_person, city, country, customer_type
FROM customers
WHERE customer_name LIKE 'A%'
ORDER BY customer_name;

-- 2. Customers whose name contains 'or'
SELECT customer_id, customer_name, contact_person, city, country, customer_type
FROM customers
WHERE customer_name LIKE '%or%'
ORDER BY customer_name;

-- 3. Customers whose name starts with 'A' OR contains 'or'
SELECT customer_id, customer_name, contact_person, city, country, customer_type
FROM customers
WHERE customer_name LIKE 'A%' OR customer_name LIKE '%or%'
ORDER BY customer_name;

-- 4. Products purchased by customers whose name starts with 'A'
SELECT DISTINCT
    c.customer_name,
    p.product_name,
    p.category,
    p.unit_price,
    e.quantity,
    e.export_country,
    e.total_value
FROM customers c
JOIN exports e ON c.customer_id = e.customer_id
JOIN products p ON e.product_id = p.product_id
WHERE c.customer_name LIKE 'A%'
ORDER BY c.customer_name, p.product_name;

-- 5. Products purchased by customers whose name contains 'or'
SELECT DISTINCT
    c.customer_name,
    p.product_name,
    p.category,
    p.unit_price,
    e.quantity,
    e.export_country,
    e.total_value
FROM customers c
JOIN exports e ON c.customer_id = e.customer_id
JOIN products p ON e.product_id = p.product_id
WHERE c.customer_name LIKE '%or%'
ORDER BY c.customer_name, p.product_name;

-- 6. Export countries for customers whose name starts with 'A'
SELECT DISTINCT
    c.customer_name,
    e.export_country,
    COUNT(e.export_id) as total_exports,
    SUM(e.total_value) as total_export_value
FROM customers c
JOIN exports e ON c.customer_id = e.customer_id
WHERE c.customer_name LIKE 'A%'
GROUP BY c.customer_name, e.export_country
ORDER BY c.customer_name, total_export_value DESC;

-- 7. Export countries for customers whose name contains 'or'
SELECT DISTINCT
    c.customer_name,
    e.export_country,
    COUNT(e.export_id) as total_exports,
    SUM(e.total_value) as total_export_value
FROM customers c
JOIN exports e ON c.customer_id = e.customer_id
WHERE c.customer_name LIKE '%or%'
GROUP BY c.customer_name, e.export_country
ORDER BY c.customer_name, total_export_value DESC;

-- 8. Complete export details for qualifying customers
SELECT
    c.customer_name,
    c.contact_person,
    c.city,
    c.country as customer_country,
    p.product_name,
    p.category,
    e.export_country,
    e.quantity,
    e.export_date,
    e.total_value
FROM customers c
JOIN exports e ON c.customer_id = e.customer_id
JOIN products p ON e.product_id = p.product_id
WHERE c.customer_name LIKE 'A%' OR c.customer_name LIKE '%or%'
ORDER BY c.customer_name, e.export_date DESC;

-- 9. Summary statistics for qualifying customers
SELECT
    COUNT(DISTINCT c.customer_id) as qualifying_customers,
    COUNT(DISTINCT p.product_id) as products_sold,
    COUNT(DISTINCT e.export_country) as export_countries,
    SUM(e.total_value) as total_export_value,
    AVG(e.total_value) as avg_export_value
FROM customers c
JOIN exports e ON c.customer_id = e.customer_id
JOIN products p ON e.product_id = p.product_id
WHERE c.customer_name LIKE 'A%' OR c.customer_name LIKE '%or%';

-- 10. Top products by export value for qualifying customers
SELECT
    p.product_name,
    p.category,
    SUM(e.total_value) as total_export_value,
    SUM(e.quantity) as total_quantity
FROM customers c
JOIN exports e ON c.customer_id = e.customer_id
JOIN products p ON e.product_id = p.product_id
WHERE c.customer_name LIKE 'A%' OR c.customer_name LIKE '%or%'
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_export_value DESC;