-- Employee Database for Harsh's Company
-- This database contains comprehensive employee information including personal details, salaries, and more

-- Create the employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    hire_date DATE,
    department VARCHAR(50),
    job_title VARCHAR(100),
    salary DECIMAL(10,2),
    manager_id INT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Active',
    performance_rating INT CHECK (performance_rating >= 1 AND performance_rating <= 5),
    bonus DECIMAL(10,2) DEFAULT 0.00,
    remarks TEXT
);

-- Insert sample employee data
INSERT INTO employees (employee_id, first_name, last_name, email, phone, hire_date, department, job_title, salary, manager_id, city, state, country, status, performance_rating, bonus, remarks) VALUES
(1, 'Harsh', 'Kumar', 'harsh.kumar@company.com', '+1-555-0101', '2020-01-15', 'Executive', 'CEO', 250000.00, NULL, 'New York', 'NY', 'USA', 'Active', 5, 50000.00, 'Company Founder and CEO'),
(2, 'Priya', 'Sharma', 'priya.sharma@company.com', '+1-555-0102', '2020-02-01', 'HR', 'HR Director', 120000.00, 1, 'New York', 'NY', 'USA', 'Active', 4, 12000.00, 'Handles all HR operations'),
(3, 'Rajesh', 'Patel', 'rajesh.patel@company.com', '+1-555-0103', '2020-03-10', 'IT', 'IT Manager', 95000.00, 1, 'San Francisco', 'CA', 'USA', 'Active', 4, 9500.00, 'Manages IT infrastructure'),
(4, 'Anjali', 'Verma', 'anjali.verma@company.com', '+1-555-0104', '2020-04-05', 'Finance', 'Finance Manager', 100000.00, 1, 'New York', 'NY', 'USA', 'Active', 5, 15000.00, 'Oversees financial operations'),
(5, 'Vikram', 'Singh', 'vikram.singh@company.com', '+1-555-0105', '2020-05-20', 'Sales', 'Sales Manager', 85000.00, 1, 'Chicago', 'IL', 'USA', 'Active', 4, 8500.00, 'Leads sales team'),
(6, 'Kavita', 'Gupta', 'kavita.gupta@company.com', '+1-555-0106', '2020-06-15', 'Marketing', 'Marketing Manager', 80000.00, 1, 'Los Angeles', 'CA', 'USA', 'Active', 4, 8000.00, 'Manages marketing campaigns'),
(7, 'Amit', 'Jain', 'amit.jain@company.com', '+1-555-0107', '2020-07-01', 'IT', 'Senior Developer', 75000.00, 3, 'San Francisco', 'CA', 'USA', 'Active', 4, 7500.00, 'Lead developer'),
(8, 'Sneha', 'Reddy', 'sneha.reddy@company.com', '+1-555-0108', '2020-08-10', 'Finance', 'Accountant', 65000.00, 4, 'New York', 'NY', 'USA', 'Active', 3, 3250.00, 'Handles accounting'),
(9, 'Rohit', 'Mehta', 'rohit.mehta@company.com', '+1-555-0109', '2020-09-05', 'Sales', 'Sales Representative', 55000.00, 5, 'Chicago', 'IL', 'USA', 'Active', 4, 5500.00, 'Top performer in sales'),
(10, 'Pooja', 'Shah', 'pooja.shah@company.com', '+1-555-0110', '2020-10-01', 'Marketing', 'Marketing Specialist', 60000.00, 6, 'Los Angeles', 'CA', 'USA', 'Active', 4, 6000.00, 'Digital marketing expert'),
(11, 'Arun', 'Nair', 'arun.nair@company.com', '+1-555-0111', '2020-11-15', 'IT', 'Junior Developer', 55000.00, 7, 'San Francisco', 'CA', 'USA', 'Active', 3, 2750.00, 'Backend developer'),
(12, 'Meera', 'Iyer', 'meera.iyer@company.com', '+1-555-0112', '2020-12-01', 'HR', 'HR Specialist', 58000.00, 2, 'New York', 'NY', 'USA', 'Active', 4, 5800.00, 'Recruitment specialist'),
(13, 'Suresh', 'Rao', 'suresh.rao@company.com', '+1-555-0113', '2021-01-10', 'Operations', 'Operations Manager', 78000.00, 1, 'Dallas', 'TX', 'USA', 'Active', 4, 7800.00, 'Manages operations'),
(14, 'Divya', 'Chopra', 'divya.chopra@company.com', '+1-555-0114', '2021-02-20', 'Finance', 'Financial Analyst', 70000.00, 4, 'New York', 'NY', 'USA', 'Active', 4, 7000.00, 'Financial planning'),
(15, 'Karan', 'Malhotra', 'karan.malhotra@company.com', '+1-555-0115', '2021-03-15', 'Sales', 'Sales Representative', 52000.00, 5, 'Chicago', 'IL', 'USA', 'Active', 3, 2600.00, 'Field sales'),
(16, 'Nisha', 'Kapoor', 'nisha.kapoor@company.com', '+1-555-0116', '2021-04-01', 'Marketing', 'Content Creator', 55000.00, 6, 'Los Angeles', 'CA', 'USA', 'Active', 4, 5500.00, 'Content marketing'),
(17, 'Rahul', 'Das', 'rahul.das@company.com', '+1-555-0117', '2021-05-10', 'IT', 'System Administrator', 68000.00, 3, 'San Francisco', 'CA', 'USA', 'Active', 4, 6800.00, 'Network administration'),
(18, 'Swati', 'Bose', 'swati.bose@company.com', '+1-555-0118', '2021-06-05', 'Operations', 'Operations Coordinator', 48000.00, 13, 'Dallas', 'TX', 'USA', 'Active', 3, 2400.00, 'Operations support'),
(19, 'Manoj', 'Yadav', 'manoj.yadav@company.com', '+1-555-0119', '2021-07-20', 'HR', 'HR Assistant', 45000.00, 2, 'New York', 'NY', 'USA', 'Active', 3, 2250.00, 'Administrative support'),
(20, 'Ritu', 'Agarwal', 'ritu.agarwal@company.com', '+1-555-0120', '2021-08-15', 'Finance', 'Junior Accountant', 50000.00, 8, 'New York', 'NY', 'USA', 'Active', 3, 2500.00, 'Bookkeeping');

-- Useful queries for Harsh to get employee details

-- 1. Get all employee details
SELECT * FROM employees ORDER BY employee_id;

-- 2. Get employee names, departments, and salaries
SELECT first_name, last_name, department, job_title, salary
FROM employees
ORDER BY department, last_name;

-- 3. Get salary statistics
SELECT
    COUNT(*) as total_employees,
    AVG(salary) as average_salary,
    MIN(salary) as min_salary,
    MAX(salary) as max_salary,
    SUM(salary) as total_salary_cost
FROM employees;

-- 4. Get employees by department with salary info
SELECT
    department,
    COUNT(*) as employee_count,
    AVG(salary) as avg_dept_salary,
    MIN(salary) as min_dept_salary,
    MAX(salary) as max_dept_salary
FROM employees
GROUP BY department
ORDER BY avg_dept_salary DESC;

-- 5. Get high earners (salary > 70000)
SELECT first_name, last_name, department, job_title, salary, performance_rating
FROM employees
WHERE salary > 70000
ORDER BY salary DESC;

-- 6. Get employees with their managers
SELECT
    e.first_name || ' ' || e.last_name as employee_name,
    e.department,
    e.job_title,
    m.first_name || ' ' || m.last_name as manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id
ORDER BY e.employee_id;

-- 7. Get employee contact information
SELECT
    first_name,
    last_name,
    email,
    phone,
    city,
    state
FROM employees
ORDER BY last_name, first_name;

-- 8. Get performance summary
SELECT
    performance_rating,
    COUNT(*) as count,
    AVG(salary) as avg_salary_with_rating
FROM employees
GROUP BY performance_rating
ORDER BY performance_rating DESC;

-- 9. Get employees by location
SELECT
    city,
    state,
    COUNT(*) as employee_count,
    AVG(salary) as avg_salary_in_city
FROM employees
GROUP BY city, state
ORDER BY employee_count DESC;

-- 10. Get total compensation (salary + bonus)
SELECT
    first_name,
    last_name,
    department,
    salary,
    bonus,
    (salary + bonus) as total_compensation
FROM employees
ORDER BY total_compensation DESC;