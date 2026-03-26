-- Table and columns schematic for fraud investigation
-- Table name: employees
-- Columns:
--   employee_id    INT PRIMARY KEY
--   employee_name  VARCHAR(100)
--   company        VARCHAR(100)
--   city           VARCHAR(100)
--   dept           VARCHAR(100)
--   job_title      VARCHAR(100)
--   grade          INT
--   status         VARCHAR(50)
--   remarks        TEXT

-- Create table (run once)
CREATE TABLE IF NOT EXISTS employees (
  employee_id INT PRIMARY KEY,
  employee_name VARCHAR(100),
  company VARCHAR(100),
  city VARCHAR(100),
  dept VARCHAR(100),
  job_title VARCHAR(100),
  grade INT,
  status VARCHAR(50),
  remarks TEXT
);

-- Sample inserts (run once, duplicate keys may fail if rerun)
INSERT OR IGNORE INTO employees (employee_id, employee_name, company, city, dept, job_title, grade, status, remarks) VALUES
  (1, 'Tarun', 'DXC', 'New York', 'Finance', 'Analyst', 110, 'active', 'under fraud review'),
  (2, 'Asha', 'DXC', 'New York', 'IT', 'Developer', 105, 'fraud', 'suspicious payment records'),
  (3, 'Rohan', 'DXC', 'Chicago', 'Support', 'Analyst', 95, 'active', 'clean');

-- 1) Find Tarun at DXC Company
SELECT employee_id, employee_name, company, city, dept, job_title, grade, status, remarks
FROM employees
WHERE company = 'DXC' AND employee_name = 'Tarun';

-- 2) Find DXC employees flagged as fraudulent
SELECT employee_id, employee_name, company, city, dept, job_title, grade, status, remarks
FROM employees
WHERE company = 'DXC' AND (status = 'fraud' OR remarks LIKE '%fraud%');

-- 3) Find DXC employees with grade > 100 (per earlier requirement) and/or known fraud IDs
SELECT employee_id, employee_name, company, city, dept, job_title, grade, status, remarks
FROM employees
WHERE company = 'DXC' AND (grade > 100 OR employee_id IN (101, 102, 103));

-- 4) DXC employees in New York OR grade > 100
SELECT employee_id, employee_name, company, city, dept, job_title, grade, status, remarks
FROM employees
WHERE company = 'DXC'
  AND (city = 'New York' OR grade > 100);

-- 5) DXC employees in New York AND grade > 100
SELECT employee_id, employee_name, company, city, dept, job_title, grade, status, remarks
FROM employees
WHERE company = 'DXC'
  AND city = 'New York'
  AND grade > 100;
