-- Employee table for Rita's company
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary DECIMAL(10,2)
);

-- Insert sample data
INSERT INTO employees (id, name, department, salary) VALUES
(1, 'Alice', 'HR', 50000.00),
(2, 'Bob', 'IT', 60000.00),
(3, 'Charlie', 'Finance', 55000.00),
(4, 'David', 'IT', 65000.00),
(5, 'Eve', 'HR', 52000.00),
(6, 'Frank', 'Finance', 58000.00);

-- Aggregate queries for Rita

-- 1. Sum of all salaries
SELECT SUM(salary) AS total_salary FROM employees;

-- 2. Average salary
SELECT AVG(salary) AS average_salary FROM employees;

-- 3. Count of distinct departments
SELECT COUNT(DISTINCT department) AS department_count FROM employees;

-- 4. Minimum salary
SELECT MIN(salary) AS min_salary FROM employees;

-- 5. Maximum salary
SELECT MAX(salary) AS max_salary FROM employees;

-- Bonus: All aggregates in one query
SELECT
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    COUNT(DISTINCT department) AS department_count,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM employees;
